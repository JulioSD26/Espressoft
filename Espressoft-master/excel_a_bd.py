from mysql.connector import connect, Error
import pandas as pd
import datetime

"""
Para que el archivo de ventas se importe correctamente es necesario que cumpla con las siguientes caracteristicas:
- La hoja en que se encuentra la información debe de llamarse "Hoja1" 
- En el primer renglon se debe de indicar los nombres de las columnas   "venta_id", "total", "fecha", "hora", "empleado_id" sin espacios y en minusculas
- Debe cuidar que los datos de cada renglon cumplan con lo siguiente:
* "venta_id" -> Solo puede tener datos que sean números
* "total" -> Solo puede tener datos que sean números
* "fecha" -> Debe de tener formato de fecha dado por excel o bien puede estar escrito de la siguiente manera "año-mes-dia". Por ejemplo: "2015-01-29"
* "hora" -> Debe de tener formato de hora dado por excel o bien puede estar escrito de la siguiente manera "hora:minutos" en formato de 24 horas. Por ejemplo: "16:40"
* "empleado_id" -> Solo puede tener datos que sean números 
Si algún renglon no cuenta con este formato, se le notificará el número de renglón y el archivo no se importará.

"""


def crear_conexion():
    try:
        conn = connect(host='localhost',
                       user='expressoft_admin',
                       password='lewylzzvmA2023/',
                       database='expressoft',
                       port=3306)
    except Error as err:
        print("Algo salio mal: {}".format(err))

    return conn


def leer_excel(archivo):
    try:
        df = pd.read_excel(archivo, sheet_name='Hoja1')
        return df
    except Exception as e:
        print("Algo salio mal al leer el archivo {}: {}".format(archivo, e))


def insertar_datos_en_tabla_empleados(hoja):
    lista_id = hoja['empleado_id']
    lista_tipo_empleado = hoja['tipo_empleado']
    lista_contrasenia = hoja['contrasenia']
    lista_nombre = hoja['nombre']
    lista_apellido_paterno = hoja['apellido_paterno']
    lista_apellido_materno = hoja['apellido_materno']
    lista_estatus = hoja['estatus']
    lista_numero_telefono = hoja['numero_telefono']
    lista_correo = hoja['correo']

    conn = crear_conexion()
    for (id, tipo_empleado, contrasenia, nombre, apellido_paterno, apellido_materno, estatus, numero_telefono, correo) in zip(lista_id, lista_tipo_empleado, lista_contrasenia, lista_nombre, lista_apellido_paterno, lista_apellido_materno, lista_estatus, lista_numero_telefono, lista_correo):
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO empleados (empleado_id, tipo_empleado, contrasenia, nombre, apellido_paterno, apellido_materno,estatus, telefono, email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (id, tipo_empleado, contrasenia, nombre, apellido_paterno, apellido_materno, estatus, numero_telefono, correo))

    conn.commit()
    conn.close()


def insertar_datos_en_tabla_venta(archivo):
    try:
        hoja = leer_excel(archivo)
    except Exception as error:
        return [False, "Algo salio mal al leer el archivo {}: {}".format(archivo, error)]
    validacion_excel = es_formato_excel_ventas_correcto(hoja)
    # el primer elemento indica si el formato del excel es correcto o no, si lo es su valor será True.
    # si el formato no es correcto
    if not validacion_excel[0]:
        # se sale de la función regresando un False y el mensaje asociado
        return [False, validacion_excel[1]]
    # si el formato fue correcto, continua
    lista_total = hoja['total']
    lista_fecha = hoja['fecha']
    lista_hora = hoja['hora']
    lista_empleado_id = hoja['empleado_id']
    try:
        conn = crear_conexion()
        cursor = conn.cursor()
    except Error as err:
        return [False, 'Imposible conectar a la base de datos: {}'.format(err)]
    renglon = 2
    for (total, fecha, hora, empleado_id) in zip(lista_total, lista_fecha, lista_hora, lista_empleado_id):

        try:
            cursor.execute(
                "INSERT INTO venta ( total, fecha, hora, empleado_id) VALUES (%s,%s,%s,%s)",
                (total, fecha, hora, empleado_id))
        except Error as err:
            # aunque se hayan hecho las validaciones arriba, es probable que pueda ocurrir un fallo al estar insertando los datos
            # como que se vaya el internet o algo así, por lo que aunque con las validaciones anteriores se trataba de prevenir que
            # si el formato fallaba en algun renglon, no se insertara ningun dato en el excel, para que no fuera tedioso para el usuario
            # tener que modificar el excel y quitar las filas que ya habian sido insertadas, modificando las que tenian formato incorrecto
            return [False, f'Algo salio mal: {err} \nEl error se produjo al tratar de insertar el renglon {renglon} en la base de datos.']
        renglon += 1
        if renglon % 100 == 0:
            conn.commit()

    conn.commit()
    conn.close()
    # si todo salió bien
    return [True, f"El archivo: {archivo} se importó correctamente a la base de datos"]


def es_formato_excel_ventas_correcto(hoja_ventas):
    """
    Checa que un excel dado cumpla con el formato correcto para insertarse en la tabla de venta.
    Regresa una lista, su primer elemento puede ser True o False, si es True, entonces el formato del excel
    es correcto completamente, en caso contrario será False. El segundo elemento es un mensaje detallado.
    """

    # se valida si los nombres de las columnas en el encabezado son los correspondientes al formato
    # se aplican clausulas de guarda
    if not validar_encabezado_excel_venta(hoja_ventas):
        return [False, "Los nombres de las columnas en el encabezado deben de aparecer y tener el siguiente orden: \ntotal fecha hora empleado_id"]
    
    # se valida si el excel que se esta subiendo para importar, ya se ha subido anteriormente
    # con esta funcion se van a checar los primeros 10 registros del excel para ver si ya se encuentran en la base de datos.
    # se pueden poner hasta len(hoja_ventas) registros para checar todo el excel, pero puede que con 10 sea suficiente
    # por que entre mas se chequen, mas se va a tardar el programa en validar cada uno, aunque este parametro
    # es modificable
    if esta_el_excel_ya_subido_en_la_bd(hoja_ventas, 10):
        return [False, "Mientras se procesaba el Excel, se encontraron registros/filas que ya se encuentran en la base de datos.\nEs muy probable que estés tratando de importar un archivo Excel ya importado, por favor asegurate si ese archivo ya ha sido importado por ti o alguien más."]
    lista_total = hoja_ventas['total']
    lista_fecha = hoja_ventas['fecha']
    lista_hora = hoja_ventas['hora']
    lista_empleado_id = hoja_ventas['empleado_id']
    renglon = 2
    validacion_integridad_id_empleados = validar_integridad_id_empleados(
        lista_empleado_id)
    # se checa la integridad de las id de empleados en el excel de ventas, respecto a la tabla de empleados
    # validacion_integridad_id_empleados[0] es si la integridad es correcta: True o False
    # validacion_integridad_id_empleados[1] es el mensaje detallado
    if not validacion_integridad_id_empleados[0]:
        # esta lista luego se va a usar para mostrar los correspondientes mensajes al usuario en la interfaz
        return [False, validacion_integridad_id_empleados[1]]
    # se "recorre" cada fila con las columnas restantes por validar (en este punto ya se validaron las id de empleados)
    for (total, fecha, hora) in zip(lista_total, lista_fecha, lista_hora):
        # se valida el formato de la celda de total
        if not es_formato_total_correcto(total):
            return [False, f"El renglón {renglon} no cumple con el formato estipulado.\nEl total '{total}' en ese renglón no cumple el formato."]
        # se valida el formato de la celda de fecha
        if not es_formato_fecha_correcto(fecha):
            return [False, f"El renglón {renglon} no cumple con el formato estipulado.\nLa fecha '{fecha}' en ese renglón no cumple el formato."]
        # se valida el formato de la celda de hora
        if not es_formato_hora_correcto(hora):
            return [False, f"El renglón {renglon} no cumple con el formato estipulado.\nLa hora '{hora}' en ese renglón no cumple el formato."]
        # el contador de renglon aumenta si el formato de la fila/renglon entera fue correcto
        renglon += 1
    # si el excel de ventas cuenta con el formato correcto completamente
    return [True, "Formato correcto del excel de ventas"]


def validar_encabezado_excel_venta(hoja_ventas):
    """
    Valida que el excel leído tenga como encabezado las columnas: total, fecha, hora, empleado_id
    """
    # se obtiene una lista con los nombres de las columnas de encabezado
    columnas_encabezado = hoja_ventas.columns.values
    # se checa si el tamanio de la lista obtenida anteriormente es menor a 4, si lo es se regresa False
    # si el excel tuviera mas de 4 columnas, se le podría permitir al usuario, pero las primeras 4 columnas
    # tienen que seguir la segunda validación que viene abajo
    if len(columnas_encabezado) < 4:
        return False
    # se checa que los primeros 4 nombres de columnas correspondan al formato correcto
    if columnas_encabezado[0] != "total" or columnas_encabezado[1] != "fecha" or columnas_encabezado[2] != "hora" or columnas_encabezado[3] != "empleado_id":
        return False
    # el formato es correcto, se regresa True
    return True


def esta_el_excel_ya_subido_en_la_bd(hoja_ventas, cantidad_de_registros_a_checar):
    """
    Valida si un excel de ventas dado ya ha sido importado a la base de datos.
    Recibe como argumento la hoja de excel de ventas y la cantidad de registros/filas, los cuales se van 
    a checar en la base de datos.
    """
    contador_registros_repetidos = 0
    contador_registros_checados = 0
    try:
        conn = crear_conexion()
        cursor = conn.cursor()
        # se va a recorrer todo el excel, pero mas abajo el for se va a detener cuando se llegue a la cantidad_de_registros_a_checar
        # esto es asi para evitar errores como que se cantidad_de_registros_a_checar sea mayor a la cantidad de registros que
        # el excel tenga
        for i in range(len(hoja_ventas)):
            # se van obteniendo las filas/registros del excel
            fila = hoja_ventas.iloc[i]
            # se ejecuta una query con los datos del registro/fila del excel
            query = f'SELECT total, fecha, hora, empleado_id FROM venta WHERE total = {fila["total"]} AND fecha = "{fila["fecha"]}" AND hora = "{fila["hora"]}" AND empleado_id = "{fila["empleado_id"]}";'
            cursor.execute(query)
            registro = cursor.fetchone()
            contador_registros_checados += 1
            # si se encontro por lo menos un registro con esos datos en la base de datos
            if registro is not None:
                contador_registros_repetidos += 1
            # para detener el for si se llega a la cantidad_de_registros_a_checar
            if i == cantidad_de_registros_a_checar - 1:
                break
        conn.close()
    except Error as err:
        return [False, f"Algo salió mal al tratarse de conectar a la base de datos: {err}"]
    # esto es para ver si un cuarto de los registros checados son menores o iguales a los registros repetidos encontrados
    # si, es asi entonces se regresa True indicando que hay uno o mas registros repetidos.
    # esto es modificable y solo esta por si se diera la casualidad de que a lo mejor un empleado hizo una venta con
    # el mismo total, en la misma fecha y hora.
    # aunque puede ser cambiado modificando la formula o directamente si se encontro un solo registro repetido, ya 
    # dar por hecho que ese excel ya se importo y regresar, True
    if (contador_registros_checados / 4) <= contador_registros_repetidos:
        return True
    return False

def es_formato_total_correcto(total):
    """
    Valida que el formato de una celda de total dada, sea correcto.
    """
    # en la base de datos, total no puede ser nulo (NOT NULL), por lo que en esta primera validación se checa eso
    # se checa que la celda del total no sea None.
    # con "total != total" se valida que total no sea un NaN (Not a Number), este truco se puede encontrar en https://towardsdatascience.com/5-methods-to-check-for-nan-values-in-in-python-3f21ddd17eed
    # se checa también que total sea una instancia de int o de float, lo que indicaría que se trata de un número
    # las validaciones están hechas como clausulas de guarda, de modo que se prioriza la negación para hacer un return temprano si algo sale mal
    if total == None or total != total or isinstance(total, (int, float)) == False:
        return False

    # en la base de datos, total es un tipo de dato DECIMAL(10, 2), por lo que la parte entera
    # solo puede tomar hasta 8 digitos (10 - 2), mientras quie la parte decimal puede tomar hasta 2 digitos -> https://dev.mysql.com/doc/refman/5.7/en/precision-math-decimal-characteristics.html
    # en la validacion anterior se checaba que total no estuviera vacío y que fuera un numero, por lo que aqui
    # se toma en cuenta eso para pasarlo a string y que no esté vacío.
    # se separa al total con su punto decimal, si es que lo tiene.
    parte_entera_y_decimal = str(total).split(".")
    # si solo tiene la parte entera y no se especificó un decimal, parte_entera_y_decimal será una lista con un elemento,
    # mientras que si el total si tiene decimal, entonces parte_entera_y_decimal será una lista con 2 elementos

    # se obtiene solo la parte entera
    parte_entera = parte_entera_y_decimal[0]
    # se checa que la parte entera no sobrepase los 8 digitos
    if (len(parte_entera) <= 8) == False:
        # si los sobrepasa, se regresa falso
        return False

    # luego si se especificó decimal en total, entonces parte_entera_y_decimal tiene 2 elementos
    if len(parte_entera_y_decimal) == 2:
        parte_decimal = parte_entera_y_decimal[1]
        # se checa que la parte decimal no sobrepase los 2 digitos
        if (len(parte_decimal) <= 2) == False:
            # si los sobrepasa, se regresa falso
            return False
    # luego si las validaciones fueron correctas, entonces el formato de total es correcto y se regresa True
    return True


def es_formato_fecha_correcto(fecha):
    """
    Valida que el formato de una celda de fecha dada, sea correcto.
    """
    # el formato estipulado es YYYY-MM-DD y como vienen estructurados en los excel
    formato_fecha = "%Y-%m-%d"
    try:
        # se formatea la fecha dada, si no ocurre ningun error durante esta transformación,
        # entonces el formato de fecha es correcto
        objeto_fecha = datetime.datetime.strptime(fecha, formato_fecha)
        return True
    # si la fecha dada no se pudo formatear, ocasionando un error, entonces su formato era incorrecto
    except:
        return False


def es_formato_hora_correcto(hora):
    """
    Valida que el formato de una celda de hora dada, sea correcto.
    """
    # el formato estipulado es hh:mm y como vienen estructurados en los excel
    formato_hora = "%H:%M"
    try:
        # se formatea la hora dada, si no ocurre ningun error durante esta transformación,
        # entonces el formato de hora es correcto
        objeto_fecha = datetime.datetime.strptime(hora, formato_hora)
        return True
    # si la hora dada no se pudo formatear, ocasionando un error, entonces su formato era incorrecto
    except:
        return False


def validar_integridad_id_empleados(lista_empleado_id):
    """
    Valida que las id de empleados que se encuentren en los archivos excel de ventas, se encuentren
    en la tabla de empleados en la base de datos, asegurando su integridad.
    Regresa una lista con 2 elementos, el primer puede ser True o False e indica si la integridad está presente,
    el segundo es un mensaje detallado.
    """
    # a la lista de id de empleados obtenida de la hoja de excel, se le convierte en un set
    # para quitar elementos duplicados y luego se vuelve a convertir en lista
    lista_empleado_id_sin_duplicados = list(set(lista_empleado_id))
    try:
        conn = crear_conexion()
        cursor = conn.cursor()
        # se obtienen todos los id de empleados distintos de la tabla de empleados
        cursor.execute("SELECT DISTINCT empleado_id FROM empleados")
        lista_tuplas_empleado_id_en_bd = cursor.fetchall()
        conn.close()
    except Error as err:
        return [False, f"Algo salió mal al tratarse de conectar a la base de datos: {err}"]
    lista_empleado_id_en_bd = []
    # de la consulta se obtiene una lista de tuplas, por lo que de esas tuplas solo se obtiene su primer elemento
    # que es el id de empleado
    for tupla in lista_tuplas_empleado_id_en_bd:
        # las id se transforman a string para evitar que se puedan obtener numeros enteros y luego tener problemas al comparar más abajo
        lista_empleado_id_en_bd.append(str(tupla[0]))

    for empleado_id in lista_empleado_id_sin_duplicados:
        # se checa si cada id de empleado en la hoja del excel no se encuentra en la tabla de empleados
        # la id de empleado de esta lista se transforma a string para compararla con el otro string de empleado id ya convertido
        if str(empleado_id) not in lista_empleado_id_en_bd:
            # si no se encuentra, se regresa una lista, con su primer elemento siendo False y el segundo siendo un mensaje detallado
            return [False, f"Mientras se procesaba el Excel, se encontró un id de empleado ({empleado_id}) que no se encuentra registrado en la base de datos (tabla empleados).\nAgregue a ese usuario."]
    # si se validó la integridad de todos los id de empleados, entonces se regresa True y un mensaje de formato correcto
    return [True, "Todo salió bien, formato correcto"]


if __name__ == '__main__':
    # El metodo recibe la ruta del archivo y devuelve un diccionario de listas en donde la llave es la columna
    # y la lista contiene los datos de esa columna
    """
    hoja_ventas_2021 = leer_excel(
        'Espressoft-master/documentos_excel/ventas/ventas-2021.xlsx')
    hoja_ventas_2022 = leer_excel(
        'Espressoft-master/documentos_excel/ventas/ventas-2022.xlsx')
    """
    # print(hoja_ventas_2021)
    # Se inserta los datos del archivo a la base de datos a la que se haya hecho conexion
    # insertar_datos_en_tabla_venta(hoja_ventas_2021)
    # insertar_datos_en_tabla_venta(hoja_ventas_2022)
    hoja_empleados = leer_excel(
        'documentos_excel\empleados\empleado.xlsx')
    insertar_datos_en_tabla_empleados(hoja_empleados)
