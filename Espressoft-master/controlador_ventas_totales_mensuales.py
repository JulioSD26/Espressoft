from controlador_general_ventas import insertar_datos_empleado_en_los_labels, crear_diccionario_totales_por_mes, calcular_porcentaje_de_ventas, obtener_total_de_ventas, obtener_periodos_con_menos_y_mas_ventas_mensuales, obtener_meta_ventas
from controlador_grafica_ventas import dibujar_grafica, limpiar_grafica
from controlador_tabla_ventas import llenar_datos_tabla, limpiar_tabla
from controlador_base_datos import crear_conexion
from PyQt5.QtWidgets import QMessageBox


class ControladorVentasTotalesMensuales():
    """
    Este controlador se va a encargar de darle funcionalidad a la ventana de ventas individuales mensuales.
    """

    def __init__(self, ventana_principal):

        # al boton buscar de esta ventana de ventas se le agrega la funcionalidad de insertar los 
        # datos de empleado en los labels correspondientes a esa ventana, 
        # para esta ventana de ventas individuales mensuales, sus labels correspondientes son:

        # ventana_principal.label_num_empleado_ventas_individuales_diarias_2
        # ventana_principal.label_nombre_ventas_individuales_diarias_2
        # ventana_principal.label_estatus_ventas_individuales_diarias_2
        # tambien se pasa el campo correspodiente a esa ventana que es:
        # ventana_principal.campo_num_empleado_ventas_individuales_diarias_2.text()
        # en todos se hace referencia a la ventana_principal MainWindow porque es la que contiene
        # a todos los componentes
        
        ventana_principal.boton_generar_ventas_totales_mensuales.clicked.connect(lambda: self.insertar_datos_ventana_ventas_totales_mensuales(
            ventana_principal,
            ventana_principal.combobox_ventas_totales_mensuales.currentText()
            ))


    def insertar_datos_ventana_ventas_totales_mensuales(self, ventana_principal, fecha):
        """
        Esta funcion tiene el proposito de llenar la ventana de ventas totales mensuales con los datos de ventas obtenidos,
        dependiendo del ano.
        Llena la grafica, tabla y labels correspondientes
        """
        datos_ventas, titulo_mensaje, mensaje = self.obtener_datos_ventas_totales_mensuales(fecha)
        if datos_ventas is None:
            dialogo = QMessageBox(ventana_principal)
            dialogo.setWindowTitle(titulo_mensaje)
            dialogo.setText(mensaje)
            dialogo.setIcon(QMessageBox.Warning)
            # si no se encontraron datos o algo salio mal, entonces se resetean los datos de esta ventana
            # para que no aparezcan los de la generacion de datos anterior
            self.resetear_datos_ventana_ventas_totales_mensuales(ventana_principal)
            boton_ok = dialogo.exec()
            return
        
        # si no ocurrio ningun error y se obtuvieron datos de ventas
        # se crea el diccionario de intervalos meses y totales con los datos de ventas
        diccionario_meses_y_totales = crear_diccionario_totales_por_mes(datos_ventas)

        # se dibuja la grafica con los datos del diccionario
        dibujar_grafica(ventana_principal.grafica_ventas_totales_mensuales, diccionario_meses_y_totales)

        # esta funcion calcular_porcentaje_de_ventas() falta implementarse para la tercera iteracion, se le pasa cualquier argumento
        ventana_principal.label_porcentaje_ventas_totales_mensuales.setText(calcular_porcentaje_de_ventas(obtener_total_de_ventas(diccionario_meses_y_totales.values()), obtener_meta_ventas(5)))

        # se le cambia el texto al label que indica el año
        ventana_principal.label_mes_ventas_totales_mensuales.setText(fecha)

        # se llena la tabla con los datos del diccionario
        llenar_datos_tabla(ventana_principal.tabla_ventas_totales_mensuales, diccionario_meses_y_totales)
        
        # se le asigna el total al label de total, cuando se le asigna un texto a un label siempre tiene que ser un str o si no marca error
        ventana_principal.label_total_ventas_totales_mensuales.setText(f"${str(obtener_total_de_ventas(diccionario_meses_y_totales.values()))}")

        mes_mas_ventas, mes_menos_ventas = obtener_periodos_con_menos_y_mas_ventas_mensuales(diccionario_meses_y_totales)

        ventana_principal.label_mes_mas_ventas_totales_mensuales.setText(str(mes_menos_ventas))
        ventana_principal.label_mes_menos_ventas_totales_mensuales.setText(str(mes_mas_ventas))


    def obtener_datos_ventas_totales_mensuales(self, year):
        """
        Dado un id de empleado y un año, regresa las ventas correspondientes a cada mes del año.
        Si todo salio bien, regresa una tupla, un titulo de mensaje y un mensaje asociado.
        """
        try:
            conn = crear_conexion()
            cursor = conn.cursor()
            cursor.execute(f'SELECT total, fecha FROM venta WHERE fecha LIKE "{year}%"')
            ventas = cursor.fetchall()
            if len(ventas) == 0:
                return None, "No se encontraron ventas", f"No se encontraron ventas para el año {year}."
            conn.close()
        except:
            return None, "Error", "Algo salió mal mientras se trataba de consultar a la base de datos."
        return ventas, "", ""

    def resetear_datos_ventana_ventas_totales_mensuales(self, ventana_principal):
        """
        Resetea todos los datos de la ventana de ventas individuales diarias, exceptuando los del empleado.
        """
        limpiar_grafica(ventana_principal.grafica_ventas_totales_mensuales)
        ventana_principal.label_porcentaje_ventas_totales_mensuales.setText("--.--%")
        ventana_principal.label_mes_ventas_totales_mensuales.setText("----")
        limpiar_tabla(ventana_principal.tabla_ventas_totales_mensuales)
        ventana_principal.label_total_ventas_totales_mensuales.setText("$--.--")
        ventana_principal.label_mes_mas_ventas_totales_mensuales.setText("----")
        ventana_principal.label_mes_menos_ventas_totales_mensuales.setText("----")