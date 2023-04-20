from mysql.connector import connect,Error
import pandas as pd

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

        conn = connect(host='aws.connect.psdb.cloud', 
                    user='kksbcwupr5oabxfhvsbo', 
                    password='pscale_pw_1i1temoDzMNj32Mvrq8JtuA9PZzdWy0lFyNNIcB92f',
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
        print("Algo salio mal al leer el archivo {}: {}".format(archivo,e))
    
         
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
    for (id, tipo_empleado, contrasenia, nombre, apellido_paterno, apellido_materno, estatus, numero_telefono, correo) in zip(lista_id, lista_tipo_empleado,lista_contrasenia,lista_nombre,lista_apellido_paterno,lista_apellido_materno,lista_estatus,lista_numero_telefono,lista_correo):
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO empleados (empleado_id, tipo_empleado, contrasenia, nombre, apellido_paterno, apellido_materno,estatus, telefono, email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (id, tipo_empleado, contrasenia, nombre, apellido_paterno, apellido_materno, estatus, numero_telefono,correo))
            
    conn.commit()
    conn.close()

def insertar_datos_en_tabla_venta(hoja):
    
    lista_total = hoja['total']
    lista_fecha = hoja['fecha']
    lista_hora = hoja['hora']
    lista_empleado_id = hoja['empleado_id']
    try:
        conn = crear_conexion()
        cursor = conn.cursor()
    except Error as err:
        print('Imposible conectar a la base de datos: {}'.format(err))

    renglon = 2
    query = "INSERT INTO venta ( total, fecha, hora, empleado_id) VALUES"
    for ( total, fecha, hora, empleado_id) in zip( lista_total, lista_fecha, lista_hora, lista_empleado_id):
        query += " ({},'{}','{}','{}'),".format( str(total), str(fecha), str(hora), str(empleado_id))
    query = query[:-1]
    query = query + ";"
    
    try:
        cursor.execute(query)
    except Error as err:
        print('Algo salio mal: {}'.format(err))
        print('Hay un dato en el renglon {} con formato diferente al solicitado'.format(renglon))
        

            
    conn.commit()
    conn.close()
    """
    for ( total, fecha, hora, empleado_id) in zip( lista_total, lista_fecha, lista_hora, lista_empleado_id):
        
        try:
            cursor.execute(
                "INSERT INTO venta ( total, fecha, hora, empleado_id) VALUES (%s,%s,%s,%s)",
                ( total, fecha, hora, empleado_id))
        except Error as err:
            print('Algo salio mal: {}'.format(err))
            print('Hay un dato en el renglon {} con formato diferente al solicitado'.format(renglon))
            break
        renglon += 1
        if renglon % 100 == 0:
            conn.commit()
            
    conn.commit()
    conn.close()"""
       
if __name__=='__main__':
    #El metodo recibe la ruta del archivo y devuelve un diccionario de listas en donde la llave es la columna
    # y la lista contiene los datos de esa columna
    #hoja_empleados = leer_excel('Espressoft-master/documentos_excel/empleados/empleado.xlsx')
    hoja_ventas_2021 = leer_excel('Espressoft-master/documentos_excel/ventas/ventas-2021.xlsx')
    #hoja_ventas_2022 = leer_excel('Espressoft-master/documentos_excel/ventas/ventas-2022.xlsx')
    #print(hoja_ventas_2021)
    #Se inserta los datos del archivo a la base de datos a la que se haya hecho conexion
    insertar_datos_en_tabla_venta(hoja_ventas_2021)
    #insertar_datos_en_tabla_venta(hoja_ventas_2022)
    #insertar_datos_en_tabla_empleados(hoja_empleados)
    #insertar_datos_en_tabla_empleados(hoja)


