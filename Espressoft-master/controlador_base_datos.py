from mysql.connector import connect,Error
from PyQt5.QtWidgets import QTableWidgetItem

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
        print('xd')
        c = conn.cursor()
        numero = int(numero)
        c.execute("SELECT * FROM empleados WHERE empleado_id = {} AND contrasenia = '{}'".format(numero,password))
        rows = c.fetchall()
        conn.close()
        return True if len(rows) > 0 else False
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False

def crear_conexion():
    conn = connect(host='localhost', user='expressoft_admin', password='lewylzzvmA2023/',database='expressoft', port=3306)
    return conn

if __name__ == "__main__":
    print("Este archivo no se ejecuta directamente")