from controlador_base_datos import crear_conexion
from otros import formatear_hora_a_formato_12_horas, crear_intervalo_de_horas, obtener_hora_restados_sus_minutos, llenar_horas_vacias_intervalos_de_horas
from PyQt5.QtWidgets import QMessageBox

# Esta funcion se podria reutilizar para todas las ventanas de ventas individuales
def obtener_datos_empleado(id_empleado):
    """
    Recibe como parametro un id de empleado dado y regresa 2 datos:
    El primero es una tupla con 5 datos que representa los datos del empleado relevantes para mostrar,
    el segundo es un mensaje en caso de que haya salido un error.
    Si ocurrio un error se regresa None como primer dato y un mensaje asociado, 
    en caso contrario se regresa al empleado y un mensaje vacio
    """
    # si el campo de id de empleado esta vacio
    if id_empleado == "":
        return None, "Por favor escribe un número de empleado en el campo correspondiente."
    try:
        conn = crear_conexion()
        cursor = conn.cursor()
        # se obtienen los datos del empleado
        cursor.execute(f'SELECT empleado_id, nombre, apellido_paterno, apellido_materno, estatus FROM empleados WHERE empleado_id = "{id_empleado}"')
        empleado = cursor.fetchone()
        # si no se encontro a un empleado con esa id
        if empleado is None:
            return None, "No se encontró a un empleado con ese número de empleado"
        conn.close()
    except:
        return None, "Algo salio mal mientras se realizaba la consulta a la base de datos."
    # si todo salio bien y se encontro a un empleado con esa id
    return empleado, ""


# Esta funcion se podria reutilizar para todas las ventanas de ventas individuales
def insertar_datos_empleado_en_los_labels(ventana_principal, id_empleado, label_id_empleado, label_nombre_empleado, label_estatus_empleado):
    """
    Se encarga de insertar los datos de empleado en los labels correspondientes a cada ventana de ventas individuales.
    Recibe como parametro la ventana principal MainWindow, el id de empleado buscado y los labels correspondientes a la ventana de ventas individuales:
    label_id_empleado, label_nombre_empleado y label_estatus_empleado.
    Regresa True si todo salio bien y se encontro al empleado, en caso contrario regresa False.
    """
    empleado, mensaje = obtener_datos_empleado(id_empleado)
    if empleado is None:
        dialogo = QMessageBox(ventana_principal)
        dialogo.setWindowTitle("Error")
        dialogo.setText(mensaje)
        dialogo.setIcon(QMessageBox.Warning)
        boton_ok = dialogo.exec()
        return False
    # si se obtuvo a un empleado sin error, se actualizan los labels
    # empleado era una tupla con 6 datos, siendo:
    # empleado[0] = id del empleado
    # empleado[1] = nombre empleado
    # empleado[2] = apellido paterno empleado
    # empleado[3] = apellido materno empleado
    # empleado[4] = estatus empleado
    label_id_empleado.setText(empleado[0])
    label_nombre_empleado.setText(f"{empleado[1]} {empleado[2]} {empleado[3]}")
    # se asigna Activo o Inactivo, segun se haya obtenido un 1 o un 0 del campo de estatus del empleado
    label_estatus_empleado.setText("Activo" if empleado[4] == 1 else "Inactivo")
    return True


# Esta funcion se podria reutilizar para las ventanas de ventas individuales diarias y ventas totales diarias
def crear_diccionario_intervalos_de_horas_y_totales(datos_ventas):
        """
        Dados los datos de ventas (una lista de tuplas, donde el primer elemento es el total y el segundo la hora),
        regresa un diccionario con el intervalo de horas en el que se realizo cada venta como llave y como valor su total.
        En el proceso se agregan intervalos de horas que no aparecian entre la hora inicial y la hora final, con un total de 0.
        La forma del diccionario regresado es como la siguiente:
        {'11:00 AM - 12:00 PM': 1550.32, '12:00 PM - 01:00 PM': 0, '01:00 PM - 02:00 PM': 0, '02:00 PM - 03:00 PM': 0, '03:00 PM - 04:00 PM': 893.0, '04:00 PM - 05:00 PM': 0, '05:00 PM - 06:00 PM': 345.0, '06:00 PM - 07:00 PM': 752.0, '07:00 PM - 08:00 PM': 0, '08:00 PM - 09:00 PM': 200.0}
        """
        # se genera la lista de horas con los segundos elementos de cada tupla (dato[1]) en la lista de datos_ventas,
        # a cada uno de ellos se los formatea al formato de 12 horas y se les "quitan"/restan sus minutos para luego ser insertados en la lista
        lista_horas = [obtener_hora_restados_sus_minutos(formatear_hora_a_formato_12_horas(dato[1])) for dato in datos_ventas]
        # a la lista anterior se le agregan aquellas horas que no estaban presentes entre la hora inicial/primera hora y la hora final / ultima hora, segun el orden
        lista_horas_con_vacios_llenados = llenar_horas_vacias_intervalos_de_horas(lista_horas)
        # se crea un diccionario que como llaves va a tener los elementos de la tupla anterior transformados en intervalos (si la hora era 03:00 PM, la llave sera 03:00 PM - 04:00 PM)
        #  y todas ellas van a tener un valor inicial de 0, que representara su total
        diccionario_intervalo_de_horas_y_sus_totales = {crear_intervalo_de_horas(hora): 0 for hora in lista_horas_con_vacios_llenados}
        # se recorre la lista de tuplas de datos_ventas
        for dato in datos_ventas:
            # el total se transforma a float, porque de la base de datos se obtiene un objeto Decimal.decimal(numero)
            total = float(dato[0])
            hora_formateada = formatear_hora_a_formato_12_horas(dato[1])
            # se crea la llave para el diccionario con la hora que se vaya obteniendo, como se mencionaba anteriormente
            # si la hora_formateada es 02:00 PM, entonces llave_diccionario sera 02:00 PM - 03:00 PM
            llave_diccionario = crear_intervalo_de_horas(hora_formateada)
            # si ese intervalo ya se encuentra en el diccionario previante creado
            # entonces que se vayan sumando/acumulando sus totales obtenidos en ese intervalo
            # luego de otro modo si una hora no aparece, como las que se generaron con llenar_horas_vacias_intervalos_de_horas(),
            # entonces su total se mantiene en 0, que es lo que se busca
            if llave_diccionario in diccionario_intervalo_de_horas_y_sus_totales:
                diccionario_intervalo_de_horas_y_sus_totales[llave_diccionario] += total
        # print("diccionario_intervalo_de_horas_y_sus_totales:", diccionario_intervalo_de_horas_y_sus_totales)
        return diccionario_intervalo_de_horas_y_sus_totales

# Esta funcion no la reutilicen ni se ocupa pero no queria ser el unico sin una B(
def crear_diccionario_meses_y_totales(meses_ventas):
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    meses_formateados = []
    for tupla in meses_ventas:
        mes = meses[tupla[0]-1] # restamos 1 para obtener el índice correcto en la lista de meses
        ventas = tupla[1]
        meses_formateados.append((mes, ventas))
    return meses_formateados


# Esta funcion se podria reutilizar para las ventanas de ventas individuales anuales y ventas totales anuales
def crear_diccionario_anios_y_totales(datos_ventas):
    """
    Dados los datos de ventas (una lista de tuplas, donde el primer elemento es el total y el segundo el anio),
    regresa un diccionario con el anio en el que se realizo cada venta como llave y como valor su total.
    """
    diccionario_anios_y_totales = {}
    for dato in datos_ventas:
        total = float(dato[0])
        anio = dato[1]
        diccionario_anios_y_totales[anio] = total
    return diccionario_anios_y_totales



# Esta funcion podria ser reutilizada para todas las ventanas de ventas.
# todavia no esta implementada porque es para la tercera iteracion.
# de momento regresa "--.--%" que es el valor que tiene antes de que se calcule algo
def calcular_porcentaje_de_ventas(total_ventas, meta_ventas):
    # aqui irian todos los calculos
    porcentaje_de_ventas = "--.--%"
    return porcentaje_de_ventas


# Esta funcion podria ser reutilizada para todas las ventanas de ventas
def obtener_total_de_ventas(totales: list):
    """
    Recibe como parametro una lista de totales, los cuales podrian ser los valores de un diccionario
    que asocie un periodo de tiempo con su total.
    Regresa la suma de todos esos totales y redondeados a 2 decimales.
    """
    # se redondea a 2 decimales, porque cuando se empiezan a sumar los floats, aunque todos tengan
    # 2 decimales o menos, empiezan a obtenerse decimales muy grandes
    return round(sum(totales), 2)


# Esta funcion podria ser reutilizada para todas las ventanas de ventas
def obtener_periodos_con_menos_y_mas_ventas(diccionario_datos: dict):
    """
    Recibe como parametro un diccionario de datos, donde sus llaves son sus periodos de tiempo
    y sus valores son sus totales correspondientes.
    Regresa 2 valores, el primero siendo el periodo con menos ventas y el segundo el periodo con mas ventas.
    """
    periodos_de_tiempo = list(diccionario_datos.keys())
    # inicialmente a ambos periodos se les asigna como maximo y minimo el primer elemento/llave/periodo del diccionario
    # para este punto ya tiene que estar validado que el diccionario no tiene que estar vacio
    periodo_con_menos_ventas = periodos_de_tiempo[0]
    periodo_con_mas_ventas = periodos_de_tiempo[0]
    # se va recorriendo cada periodo en los periodos de tiempo
    for periodo in periodos_de_tiempo:
        # se va obteniendo el total de cada periodo
        total_del_periodo = diccionario_datos[periodo]
        # si ese total es menor al total del periodo con menos ventas
        if total_del_periodo < diccionario_datos[periodo_con_menos_ventas]:
            # entonces periodo con menos ventas ahora se convierte en ese periodo
            periodo_con_menos_ventas = periodo
        # misma logica que la anterior, solo que para el periodo con mas ventas
        if total_del_periodo > diccionario_datos[periodo_con_mas_ventas]:
            periodo_con_mas_ventas = periodo
    return periodo_con_menos_ventas, periodo_con_mas_ventas

# Usare mi propio metodo no me da confianza que pueda agarrar un valor 0 en los meses
# Obtener mes con mas y menos ventas que sean distintos a 0
def obtener_meses_mas_y_menos_ventas(meses_ventas):
    # Ordenamos la lista de ventas de mayor a menor
    meses_ventas.sort(key=lambda x: x[1], reverse=True)

    # Buscamos el mes con más ventas
    mes_mas_ventas = None
    max_ventas = 0
    for mes, ventas in meses_ventas:
        if ventas > max_ventas:
            max_ventas = ventas
            mes_mas_ventas = mes
        else:
            break

    # Buscamos el mes con menos ventas (diferente de 0)
    mes_menos_ventas = None
    min_ventas = float('inf')
    for mes, ventas in meses_ventas:
        if ventas == 0:
            continue
        if ventas < min_ventas:
            min_ventas = ventas
            mes_menos_ventas = mes

    return mes_mas_ventas, mes_menos_ventas


