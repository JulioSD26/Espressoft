from mysql.connector import connect,Error
import pandas as pd



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
       
if __name__=='__main__':
    hoja = leer_excel('Espressoft-master/documentos_excel/empleados/empleado.xlsx')
    print(hoja)
    #insertar_datos_en_tabla_empleados(hoja)


