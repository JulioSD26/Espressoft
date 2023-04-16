from controlador_general_ventas import insertar_datos_empleado_en_los_labels, crear_diccionario_anios_y_totales, calcular_porcentaje_de_ventas, obtener_total_de_ventas, obtener_periodos_con_menos_y_mas_ventas
from controlador_grafica_ventas import dibujar_grafica, limpiar_grafica
from controlador_tabla_ventas import llenar_datos_tabla, limpiar_tabla
from controlador_base_datos import crear_conexion
from otros import obtener_fecha_actual, obtener_fecha_actual_formato_espaniol
from PyQt5.QtWidgets import QMessageBox


class ControladorVentasIndividualesAnuales():
    """
    Este controlador se va a encargar de darle funcionalidad a la ventana de ventas individuales anuales.
    """

    def __init__(self, ventana_principal):
        
        # el boton de buscar en esta ventana, va a buscar al empleado y al mismo tiempo generar los datos,
        # a diferencia de otras ventanas como la de ventas individuales diarias donde habia un boton aparte de generar
        # se le agrega el evento de insertar datos a esta ventana,
        # ademas de la ventana principal se le pasan como argumento:
        # ventana_principal.label_num_empleado_ventas_individuales_anuales.text() -> id del empleado
        ventana_principal.boton_buscar_ventas_individuales_anuales.clicked.connect(lambda: self.insertar_datos_ventana_ventas_individuales_anuales(ventana_principal, ventana_principal.campo_num_empleado_ventas_individuales_anuales.text()))

        # a este label se le asigna la fecha actual
        ventana_principal.label_fecha_en_curso_ventas_individuales_anuales.setText(obtener_fecha_actual_formato_espaniol())


    def insertar_datos_ventana_ventas_individuales_anuales(self, ventana_principal, id_empleado):
        """
        Esta funcion tiene el proposito de llenar la ventana de ventas individuales anuales con los datos de ventas obtenidos,
        dependiendo del id del empleado y el anio seleccionado.
        Llena la grafica, tabla y labels correspondientes
        """

        # se insertan los datos de empleado en sus labels correspondientes y se guarda
        # el valor booleano obtenido de esa operacion
        datos_empleado_encontrados_correctamente = insertar_datos_empleado_en_los_labels(
            ventana_principal, 
            ventana_principal.campo_num_empleado_ventas_individuales_anuales.text(), 
            ventana_principal.label_num_empleado_ventas_individuales_anuales,
            ventana_principal.label_nombre_ventas_individuales_anuales,
            ventana_principal.label_estatus_ventas_individuales_anuales
        )
        # si no se encontro al empleado o algo salio mal, se sale de la funcion
        if not datos_empleado_encontrados_correctamente:
            return

        datos_ventas, titulo_mensaje, mensaje = self.obtener_datos_ventas_individuales_anuales(id_empleado)
        if datos_ventas is None:
            dialogo = QMessageBox(ventana_principal)
            dialogo.setWindowTitle(titulo_mensaje)
            dialogo.setText(mensaje)
            dialogo.setIcon(QMessageBox.Warning)
            # si no se encontraron datos o algo salio mal, entonces se resetean los datos de esta ventana
            # para que no aparezcan los de la generacion de datos anterior
            self.resetear_datos_ventana_ventas_individuales_anuales(ventana_principal)
            boton_ok = dialogo.exec()
            return
        # si no ocurrio ningun error y se obtuvieron datos de ventas
        # se crea el diccionario de anios y totales con los datos de ventas
        diccionario_anios_y_totales = crear_diccionario_anios_y_totales(datos_ventas)
        # se dibuja la grafica con los datos del diccionario
        dibujar_grafica(ventana_principal.grafica_ventas_individuales_anuales, diccionario_anios_y_totales)
        # esta funcion calcular_porcentaje_de_ventas() falta implementarse para la tercera iteracion, se le pasa cualquier argumento
        ventana_principal.label_porcentaje_ventas_individuales_anuales.setText(calcular_porcentaje_de_ventas(0, 0))
        
        # se obtiene el anio en curso
        anio_en_curso = obtener_fecha_actual().year
        # se le asigna un valor inicial de 0 al total del anio en curso
        total_anio_en_curso = 0
        # si hay ventas registradas en el anio en curso
        if anio_en_curso in diccionario_anios_y_totales:
            # se remueve ese anio del diccionario y se obtiene su valor asociado
            total_anio_en_curso = diccionario_anios_y_totales.pop(anio_en_curso)
        # luego si tenia ese anio o no, de todos modos se le pone "En proceso"
        diccionario_anios_y_totales[anio_en_curso] = "En proceso"
        # se llena la tabla con los datos del diccionario
        llenar_datos_tabla(ventana_principal.tabla_ventas_individuales_anuales, diccionario_anios_y_totales)
        # luego se vuelve a quitar el anio en curso, aunque este tenga ventas, es para
        # sacar el total sin incluir el total del anio en curso, ese total va a ser agregado al final
        # con la variable total_anio_en_curso
        diccionario_anios_y_totales.pop(anio_en_curso)
        total_ventas_sin_incluir_anio_en_curso = obtener_total_de_ventas(diccionario_anios_y_totales.values())
        # se le asigna el total al label de total, cuando se le asigna un texto a un label siempre tiene que ser un str o si no marca error
        ventana_principal.label_total_ventas_individuales_anuales.setText(f"${str(total_ventas_sin_incluir_anio_en_curso)}")

        anio_menos_ventas, anio_mas_ventas = obtener_periodos_con_menos_y_mas_ventas(diccionario_anios_y_totales)
        
        ventana_principal.label_anio_menos_ventas_individuales_anuales.setText(str(anio_menos_ventas))
        ventana_principal.label_anio_mas_ventas_individuales_anuales.setText(str(anio_mas_ventas))

        ventana_principal.label_ventas_anio_en_curso_ventas_individuales_anuales.setText(f"${str(total_anio_en_curso)}")

        # aqui finalmente se suman el total del anio en curso y los totales de los otros anios
        ventana_principal.label_ventas_totales_anio_actual_incluido_ventas_individuales_anuales.setText(f"${str(total_ventas_sin_incluir_anio_en_curso + total_anio_en_curso)}")



    def obtener_datos_ventas_individuales_anuales(self, id_empleado):
        """
        Dado un id de empleado, regresa sus ventas correspondientes en los distintos anios.
        Si todo salio bien, regresa una tupla, un titulo de mensaje y un mensaje asociado.
        """
        try:
            conn = crear_conexion()
            cursor = conn.cursor()
            # se agrupan los totales por anios y se ordenan por anio
            cursor.execute(f'SELECT COUNT(total), YEAR(fecha) FROM venta WHERE empleado_id = "{id_empleado}" GROUP BY YEAR(fecha) ORDER BY YEAR(fecha)')
            ventas = cursor.fetchall()
            if len(ventas) == 0:
                return None, "No se encontraron ventas", f"No se encontraron ventas para el empleado con id {id_empleado}."
            conn.close()
        except:
            return None, "Error", "Algo salió mal mientras se trataba de consultar a la base de datos."
        return ventas, "", ""
    

    def resetear_datos_ventana_ventas_individuales_anuales(self, ventana_principal):
        """
        Resetea todos los datos de la ventana de ventas individuales anuales, exceptuando los del empleado.
        """
        limpiar_grafica(ventana_principal.grafica_ventas_individuales_anuales)
        ventana_principal.label_porcentaje_ventas_individuales_anuales.setText("--.--%")
        limpiar_tabla(ventana_principal.tabla_ventas_individuales_anuales)
        ventana_principal.label_total_ventas_individuales_anuales.setText("$--.--")
        ventana_principal.label_anio_menos_ventas_individuales_anuales.setText("----")
        ventana_principal.label_anio_mas_ventas_individuales_anuales.setText("----")
        ventana_principal.label_ventas_anio_en_curso_ventas_individuales_anuales.setText("$--.--")
        ventana_principal.label_ventas_totales_anio_actual_incluido_ventas_individuales_anuales.setText("$--.--")