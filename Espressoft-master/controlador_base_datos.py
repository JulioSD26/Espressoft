from mysql.connector import connect,Error
from PyQt5.QtWidgets import QTableWidgetItem
from empleados import asignar_empleado_loggeado

def llenar_tabla_empleados(tableWidget, sqlquery=""):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        sqlquery = "SELECT CONCAT(nombre,' ',apellido_paterno,' ',apellido_materno) as nombre_completo, empleado_id, tipo_empleado, estatus FROM empleados" if sqlquery == "" else sqlquery
        c.execute(sqlquery)
        rows = c.fetchall()
        
        tableWidget.setRowCount(0)

        for row in rows:
            rowPosition = tableWidget.rowCount()
            tableWidget.insertRow(rowPosition)
            tableWidget.setItem(rowPosition, 0, QTableWidgetItem(row[0]))
            tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(row[1])))
            tableWidget.setItem(rowPosition, 2, QTableWidgetItem(row[2]))
            tableWidget.setItem(rowPosition, 3, QTableWidgetItem('Activo' if row[3] == 1 else 'Inactivo'))
        
        conn.close()
    except Error as err:
        print("Algo salio mal: {}".format(err))

def buscar_empleados(tableWidget, nombre):
    sqlquery="".join(("SELECT * FROM (SELECT CONCAT(nombre,' ',apellido_paterno,' ',apellido_materno) as nombre_completo, empleado_id, tipo_empleado, ", 
                  "estatus FROM empleados) as empleados2 WHERE nombre_completo LIKE '%{}%'".format(nombre)))
    llenar_tabla_empleados(tableWidget, sqlquery)

def verifica_login(numero,password):
    try:
        conn = crear_conexion()
        
        c = conn.cursor()
        # ahora el num empleado es un varchar, no necesita convertirse a entero
        numero = numero
        c.execute("SELECT empleado_id, tipo_empleado FROM empleados WHERE empleado_id = '{}' AND contrasenia = '{}'".format(numero,password))
        rows = c.fetchall()
        
        conn.close()
        if len(rows) > 0:
            # en teoria rows deberia de regresar solo una fila si los datos son correctos, por lo que se accede a su unico elemento, que es el primero
            # de ahi, se obtiene una tupla, que de momento es la id del empleado y su tipo
            empleado = rows[0]
            # se le pasa esa tupla a la siguiente funcion para crear una instancia de un empleado loggeado
            asignar_empleado_loggeado(empleado)
            return True
        else:
            return False
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False
    
def verifica_usuario(numero):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT empleado_id FROM empleados WHERE empleado_id = '{}'".format(numero))
        rows = c.fetchall()
        conn.close()
        if len(rows) > 0:
            return True
        else:
            return False
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False

def crear_conexion():

    conn = connect(host='us-west.connect.psdb.cloud', 
                   user='o7rlpqw42yyyof54jxn9', 
                   password='pscale_pw_bkBPzdSi5wMSbrWf1d1GCydQPX6a6FGvRJJAwqol7tZ',
                   database='expressoft', 
                   port=3306)


    return conn




if __name__ == "__main__":
    print("Este archivo no se ejecuta directamente")