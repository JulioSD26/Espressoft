from mysql.connector import connect
from PyQt5.QtWidgets import QTableWidgetItem

def llenar_tabla_empleados(tableWidget, sqlquery=""):
    try:
        conn = connect(host='localhost', user='root', password='',database='expressoft', port=3306)
        c = conn.cursor()
        sqlquery = "SELECT CONCAT(nombre,' ',apellido_paterno,' ',apellido_materno), empleado_id, tipo_empleado, estatus FROM empleados" if sqlquery == "" else sqlquery
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
    except:
        print("Error al conectar a la base de datos")

def buscar_empleados(tableWidget, nombre):
    sqlquery="".join(("SELECT * FROM (SELECT CONCAT(nombre,' ',apellido_paterno,' ',apellido_materno) as nombrec, empleado_id, tipo_empleado, ", 
                  "estatus FROM empleados) as empleados2 WHERE nombrec LIKE '%{}%'".format(nombre)))
    llenar_tabla_empleados(tableWidget, sqlquery)