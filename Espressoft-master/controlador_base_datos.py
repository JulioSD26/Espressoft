import re
from mysql.connector import connect,Error
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from empleados import asignar_empleado_loggeado
from conectar_a_bd import crear_conexion_nube, crear_conexion_local


def llenar_tabla_empleados(tableWidget, sqlquery=""):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        sqlquery = "SELECT CONCAT(nombre,' ',apellido_paterno,' ',apellido_materno) as nombre_completo, empleado_id, tipo_empleado, estatus FROM empleados ORDER BY CAST(empleado_id as signed)" if sqlquery == "" else sqlquery
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
                  "estatus FROM empleados) as empleados2 WHERE nombre_completo LIKE '%{}%' ORDER BY CAST(empleado_id as signed)".format(nombre)))
    llenar_tabla_empleados(tableWidget, sqlquery)

def obtener_empleado(empleado_id):
    global busqueda_empleado
    if empleado_id == "":
        busqueda_empleado = []
    else:
        try:
            conn = crear_conexion()
            c = conn.cursor()
            c.execute("SELECT * FROM empleados WHERE empleado_id = {}".format(empleado_id))
            rows = c.fetchall()
            conn.close()
            if rows == []:
                busqueda_empleado = []
            else:
                busqueda_empleado = rows[0]
        except Error as err:
            print("Algo salio mal: {}".format(err))

def vacia_campos(label_numero, label_nombre, label_apellido_paterno, label_apellido_materno, label_correo, label_telefono, label_tipo_empleado, label_estatus, label_password, label_mensaje):
    label_numero.setText("")
    label_tipo_empleado.setCurrentText("empleado")
    label_password.setText("")
    label_nombre.setText("")
    label_apellido_paterno.setText("")
    label_apellido_materno.setText("")
    label_estatus.setCurrentText("activo")
    label_telefono.setText("")
    label_correo.setText("")
    label_mensaje.setText("")

def llena_campos(label_numero, label_nombre, label_apellido_paterno, label_apellido_materno, label_correo, label_telefono, label_tipo_empleado, label_estatus, label_password, label_mensaje):
    if busqueda_empleado == []:
        label_mensaje.setText("No se encontro el empleado")
    else:
        label_mensaje.setText("")
        label_numero.setText(str(busqueda_empleado[0]))
        label_tipo_empleado.setCurrentText(busqueda_empleado[1])
        label_password.setText(busqueda_empleado[2])
        label_nombre.setText(busqueda_empleado[3])
        label_apellido_paterno.setText(busqueda_empleado[4])
        label_apellido_materno.setText(busqueda_empleado[5])
        label_estatus.setCurrentText('activo' if busqueda_empleado[6] == 1 else 'inactivo')
        label_telefono.setText(busqueda_empleado[7])
        label_correo.setText(busqueda_empleado[8])

def cambia_campo_contrasena(combo_tipo, campo_password):
    if combo_tipo.currentText() == "empleado":
        campo_password.setVisible(False)
        campo_password.setText("")
        campo_password.setEnabled(False)
    else:
        campo_password.setVisible(True)
        campo_password.setEnabled(True) 

def agregar_empleado(empleado_id, nombre, apellido_paterno, apellido_materno, correo, telefono, tipo_empleado, estatus, password, label_mensaje, ventana_principal):
    if valida_datos(empleado_id, nombre, apellido_paterno, apellido_materno, correo, telefono, tipo_empleado, password, label_mensaje):
        try:
            conn = crear_conexion()
            c = conn.cursor()
            if estatus == 'activo':
                estatus = 1
            else:
                estatus = 0
            c.execute("INSERT INTO empleados (empleado_id, nombre, apellido_paterno, apellido_materno, email, telefono, tipo_empleado, estatus, contrasenia) VALUES ('{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(empleado_id, nombre, apellido_paterno, apellido_materno, correo, telefono, tipo_empleado, estatus, password))
            conn.commit()
            conn.close()
            dialogo = QMessageBox(ventana_principal)
            label_mensaje.setText("Empleado agregado correctamente")
            dialogo.setWindowTitle("Recordatorio")
            dialogo.setText("Recuerda modificar la ventana de meta ventas")
            dialogo.setIcon(QMessageBox.Warning)
            boton_ok = dialogo.exec()
            # se sale de la función
            return True
        except Error as err:
            print("Algo salio mal: {}".format(err))
            return False
    
def editar_empleado(empleado_id, nombre, apellido_paterno, apellido_materno, correo, telefono, tipo_empleado, estatus, password, label_mensaje, ventana_principal):
    if valida_datos_editar(empleado_id, nombre, apellido_paterno, apellido_materno, correo, telefono, tipo_empleado, password, label_mensaje):
        try:
            conn = crear_conexion()
            c = conn.cursor()
            if estatus == 'activo':
                estatus = 1
            else:
                estatus = 0
            c.execute("UPDATE empleados SET nombre = '{}', apellido_paterno = '{}', apellido_materno = '{}', email = '{}', telefono = '{}', tipo_empleado = '{}', estatus = '{}', contrasenia = '{}' WHERE empleado_id = {}".format(nombre, apellido_paterno, apellido_materno, correo, telefono, tipo_empleado, estatus, password, empleado_id))
            conn.commit()
            conn.close()
            dialogo = QMessageBox(ventana_principal)
            label_mensaje.setText("Empleado editado correctamente")
            dialogo.setWindowTitle("Recordatorio")
            dialogo.setText("Recuerda modificar la ventana de meta ventas")
            dialogo.setIcon(QMessageBox.Warning)
            boton_ok = dialogo.exec()
            return True
        except Error as err:
            print("Algo salio mal: {}".format(err))
            return False

def valida_datos(empleado_id, nombre, apellido_paterno, apellido_materno, correo, telefono, tipo_empleado, password, label_mensaje):
    if empleado_id == "":
        label_mensaje.setText("El numero de empleado no puede estar vacio")
        return False
    elif nombre == "":
        label_mensaje.setText("El nombre no puede estar vacio")
        return False
    elif apellido_paterno == "":
        label_mensaje.setText("El apellido paterno no puede estar vacio")
        return False
    elif apellido_materno == "":
        label_mensaje.setText("El apellido materno no puede estar vacio")
        return False
    elif correo == "":
        label_mensaje.setText("El correo no puede estar vacio")
        return False
    elif telefono == "":
        label_mensaje.setText("El telefono no puede estar vacio")
        return False
    elif password == "" and tipo_empleado != "empleado":
        label_mensaje.setText("La contraseña no puede estar vacia")
        return False
    elif verifica_usuario(empleado_id) == True:
        label_mensaje.setText("El numero de empleado ya existe")
        return False
    elif validar_correo(correo) == False:
        label_mensaje.setText("Formato de correo incorrecto")
        return False
    elif validar_telefono(telefono) == False:
        label_mensaje.setText("Formato de telefono incorrecto")
        return False
    elif verifica_correo(correo) == True:
        label_mensaje.setText("El correo ya existe")
        return False
    elif verifica_telefono(telefono) == True:
        label_mensaje.setText("El telefono ya existe")
        return False
    else:
        return True

def valida_datos_editar(empleado_id, nombre, apellido_paterno, apellido_materno, correo, telefono, tipo_empleado, password, label_mensaje):
    if nombre == "":
        label_mensaje.setText("El nombre no puede estar vacio")
        return False
    elif apellido_paterno == "":
        label_mensaje.setText("El apellido paterno no puede estar vacio")
        return False
    elif apellido_materno == "":
        label_mensaje.setText("El apellido materno no puede estar vacio")
        return False
    elif correo == "":
        label_mensaje.setText("El correo no puede estar vacio")
        return False
    elif telefono == "":
        label_mensaje.setText("El telefono no puede estar vacio")
        return False
    elif password == "" and tipo_empleado != "empleado":
        label_mensaje.setText("La contraseña no puede estar vacia")
        return False
    elif validar_correo(correo) == False:
        label_mensaje.setText("Formato de correo incorrecto")
        return False
    elif validar_telefono(telefono) == False:
        label_mensaje.setText("Formato de telefono incorrecto")
        return False
    elif verifica_correo_editar(correo, empleado_id) == True:
        label_mensaje.setText("El correo ya existe")
        return False
    elif verifica_telefono_editar(telefono, empleado_id) == True:
        label_mensaje.setText("El telefono ya existe")
        return False
    else:
        return True

def obtener_ultimo_empleado_id(label):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT COUNT(empleado_id) FROM empleados")
        rows = c.fetchall()
        conn.close()
        num = 0
        num += int(rows[0][0])+1
        label.setText(str(num))
    except Error as err:
        print("Algo salio mal: {}".format(err))

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
    
def verifica_correo(entrada):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT email FROM empleados WHERE email = '{}'".format(entrada))
        rows = c.fetchall()
        conn.close()
        if len(rows) > 0:
            return True
        else:
            return False
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False

def verifica_correo_editar(entrada, empleado_id):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT email FROM empleados WHERE email = '{}'".format(entrada))
        rows = c.fetchall()
        conn.close()
        if len(rows) > 0:
            conn = crear_conexion()
            c = conn.cursor()
            c.execute("SELECT email FROM empleados WHERE empleado_id ='{}'".format(empleado_id))
            rows = c.fetchall()
            conn.close()
            if rows[0][0] == entrada:
                return False
            else:
                return True
        else:
            return False
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False
    

def validar_correo(correo):
    # Definir la expresión regular para validar el formato de un correo electrónico
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    # Realizar la validación utilizando la expresión regular y el método search de re
    resultado = re.search(patron, correo)
    # Devolver True si el correo electrónico es válido, False en caso contrario
    return resultado is not None

def verifica_telefono(entrada):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT telefono FROM empleados WHERE telefono = '{}'".format(entrada))
        rows = c.fetchall()
        conn.close()
        if len(rows) > 0:
            return True
        else:
            return False
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False

def verifica_telefono_editar(entrada, empleado_id):
    try:
        conn = crear_conexion()
        c = conn.cursor()
        c.execute("SELECT telefono FROM empleados WHERE telefono = '{}'".format(entrada))
        rows = c.fetchall()
        conn.close()
        if len(rows) > 0:
            conn = crear_conexion()
            c = conn.cursor()
            c.execute("SELECT telefono FROM empleados WHERE empleado_id ='{}'".format(empleado_id))
            rows = c.fetchall()
            conn.close()
            if rows[0][0] == entrada:
                return False
            else:
                return True
        else:
            return False
    except Error as err:
        print("Algo salio mal: {}".format(err))
        return False

def validar_telefono(telefono):
    patron = r'^\+?1?\d{9,15}$'
    resultado = re.match(patron, telefono)
    if resultado:
        return True
    else:
        return False

def crear_conexion():

    return crear_conexion_local()




if __name__ == "__main__":
    print("Este archivo no se ejecuta directamente")