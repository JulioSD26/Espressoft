from controlador_general_ventas import crear_diccionario_intervalos_de_horas_y_totales, calcular_porcentaje_de_ventas, obtener_total_de_ventas, obtener_periodos_con_menos_y_mas_ventas
from controlador_grafica_ventas import dibujar_grafica, limpiar_grafica
from controlador_tabla_ventas import llenar_datos_tabla, limpiar_tabla
from controlador_base_datos import crear_conexion
from otros import formatear_dia_a_formato_dia_mes_anio
from PyQt5.QtWidgets import QMessageBox


class ControladorVentasTotalesDiarias():
    """
    Este controlador se va a encargar de darle funcionalidad a la ventana de ventas totales diarias.
    """

    def __init__(self, ventana_principal):
        
        # al boton de generar ventas en esta ventana se le agrega el evento de insertar datos a esta ventana,
        # ademas de la ventana principal se le pasan como argumento:
        # ventana_principal.label_num_empleado_ventas_totales_diarias.text() -> id del empleado
        # ventana_principal.fecha_seleccionada_ventas_totales_diarias.date().toPyDate() -> fecha seleccionada ya convertida
        ventana_principal.boton_generar_ventas_totales_diarias.clicked.connect(lambda: self.insertar_datos_ventana_ventas_totales_diarias(
            ventana_principal,
            ventana_principal.fecha_seleccionada_ventas_totales_diarias.date().toPyDate()
            ))


    def insertar_datos_ventana_ventas_totales_diarias(self, ventana_principal, fecha):
        """
        Esta funcion tiene el proposito de llenar la ventana de ventas totales diarias con los datos de ventas obtenidos,
        dependiendo del id del empleado y la fecha.
        Llena la grafica, tabla y labels correspondientes
        """
        datos_ventas, titulo_mensaje, mensaje = self.obtener_datos_ventas_totales_diarias(fecha)
        if datos_ventas is None:
            dialogo = QMessageBox(ventana_principal)
            dialogo.setWindowTitle(titulo_mensaje)
            dialogo.setText(mensaje)
            dialogo.setIcon(QMessageBox.Warning)
            # si no se encontraron datos o algo salio mal, entonces se resetean los datos de esta ventana
            # para que no aparezcan los de la generacion de datos anterior
            self.resetear_datos_ventana_ventas_totales_diarias(ventana_principal)
            boton_ok = dialogo.exec()
            return
        # si no ocurrio ningun error y se obtuvieron datos de ventas
        # se crea el diccionario de intervalos de horas y totales con los datos de ventas
        diccionario_intervalos_de_horas_y_totales = crear_diccionario_intervalos_de_horas_y_totales(datos_ventas)
        # se dibuja la grafica con los datos del diccionario
        dibujar_grafica(ventana_principal.grafica_ventas_totales_diarias, diccionario_intervalos_de_horas_y_totales)
        # esta funcion calcular_porcentaje_de_ventas() falta implementarse para la tercera iteracion, se le pasa cualquier argumento
        ventana_principal.label_porcentaje_ventas_totales_diarias.setText(calcular_porcentaje_de_ventas(0, 0))
        # se le cambia el texto al label que indica el dia, formateando la fecha a dia/mes/anio
        ventana_principal.label_dia_ventas_totales_diarias.setText(formatear_dia_a_formato_dia_mes_anio(fecha))
        # se llena la tabla con los datos del diccionario
        llenar_datos_tabla(ventana_principal.tabla_ventas_totales_diarias, diccionario_intervalos_de_horas_y_totales)
        # se le asigna el total al label de total, cuando se le asigna un texto a un label siempre tiene que ser un str o si no marca error
        ventana_principal.label_total_ventas_totales_diarias.setText(f"${str(obtener_total_de_ventas(diccionario_intervalos_de_horas_y_totales.values()))}")

        intervalo_horas_menos_ventas, intervalo_horas_mas_ventas = obtener_periodos_con_menos_y_mas_ventas(diccionario_intervalos_de_horas_y_totales)
        
        ventana_principal.label_hora_menos_ventas_totales_diarias.setText(str(intervalo_horas_menos_ventas))
        ventana_principal.label_hora_mas_ventas_totales_diarias.setText(str(intervalo_horas_mas_ventas))



    def obtener_datos_ventas_totales_diarias(self, fecha):
        try:
            conn = crear_conexion()
            cursor = conn.cursor()
            cursor.execute(f'SELECT total, hora FROM venta WHERE fecha = "{fecha}"')
            ventas = cursor.fetchall()
            if len(ventas) == 0:
                return None, "No se encontraron ventas", f"No se encontraron ventas en la fecha {formatear_dia_a_formato_dia_mes_anio(fecha)}."
            conn.close()
        except:
            return None, "Error", "Algo salió mal mientras se trataba de consultar a la base de datos."
        return ventas, "", ""
    

    def resetear_datos_ventana_ventas_totales_diarias(self, ventana_principal):
        """
        Resetea todos los datos de la ventana de ventas totales diarias, exceptuando los del empleado.
        """
        limpiar_grafica(ventana_principal.grafica_ventas_totales_diarias)
        ventana_principal.label_porcentaje_ventas_totales_diarias.setText("--.--%")
        ventana_principal.label_dia_ventas_totales_diarias.setText("--/--/--")
        limpiar_tabla(ventana_principal.tabla_ventas_totales_diarias)
        ventana_principal.label_total_ventas_totales_diarias.setText("$--.--")
        ventana_principal.label_hora_menos_ventas_totales_diarias.setText("--:-- pm - --:-- pm")
        ventana_principal.label_hora_mas_ventas_totales_diarias.setText("--:-- pm - --:-- pm")