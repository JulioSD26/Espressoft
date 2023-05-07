from controlador_general_ventas import insertar_datos_empleado_en_los_labels, crear_diccionario_anios_y_totales, calcular_porcentaje_de_ventas, obtener_total_de_ventas, obtener_periodos_con_menos_y_mas_ventas, obtener_meta_ventas, obtener_diccionario_anios_porcentajes
from controlador_grafica_ventas import dibujar_grafica, limpiar_grafica
from controlador_tabla_ventas import llenar_datos_tabla, limpiar_tabla
from controlador_base_datos import crear_conexion
from otros import obtener_fecha_actual, obtener_fecha_actual_formato_espaniol
from PyQt5.QtWidgets import QMessageBox


class ControladorVentasTotalesAnuales():
    """
        este controlador se va a encargar de darle funcionalidad a la ventana de ventas totales anuales
    """
    
    def __init__(self, ventana_principal):
        ventana_principal.boton_ventas_totales_anuales.clicked.connect(lambda: self.insertar_datos_ventana_ventas_totales_anuales(
            ventana_principal
        ))
        # a este label se le asigna la fecha actual
        ventana_principal.label_fecha_en_curso_ventas_totales_anuales.setText(obtener_fecha_actual_formato_espaniol())
        

    def obtener_datos_ventas_totales_anuales(self):
        """
        Regresa las ventas en los distintos anios.
        Si todo salio bien, regresa una tupla, un titulo de mensaje y un mensaje asociado.
        """
        try:
            conn = crear_conexion()
            cursor = conn.cursor()
            # se agrupan los totales por anios y se ordenan por anio
            cursor.execute(f'SELECT SUM(total), YEAR(fecha) FROM venta GROUP BY YEAR(fecha) ORDER BY YEAR(fecha)')
            ventas = cursor.fetchall()
            print("las ventas totales son: ", ventas)
            if len(ventas) == 0:
                return None, "No se encontraron ventas", f"No se encontraron ventas."
            conn.close()
        except:
            return None, "Error", "Algo salió mal mientras se trataba de consultar a la base de datos."
        return ventas, "", ""
    
    def insertar_datos_ventana_ventas_totales_anuales(self, ventana_principal):
        """
        Esta funcion tiene el proposito de llenar la ventana de ventas totales anuales con los datos de ventas obtenidos,
        Llena la grafica, tabla y labels correspondientes
        """

        datos_ventas, titulo_mensaje, mensaje = self.obtener_datos_ventas_totales_anuales()
        if datos_ventas is None:
            dialogo = QMessageBox(ventana_principal)
            dialogo.setWindowTitle(titulo_mensaje)
            dialogo.setText(mensaje)
            dialogo.setIcon(QMessageBox.Warning)
            # si no se encontraron datos o algo salio mal, entonces se resetean los datos de esta ventana
            # para que no aparezcan los de la generacion de datos anterior
            boton_ok = dialogo.exec()
            return
        # si no ocurrio ningun error y se obtuvieron datos de ventas
        # se crea el diccionario de anios y totales con los datos de ventas
        diccionario_anios_y_totales = crear_diccionario_anios_y_totales(datos_ventas)
        # se dibuja la grafica con los datos del diccionario
        dibujar_grafica(ventana_principal.grafica_ventas_totales_anuales, diccionario_anios_y_totales)

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

        # la meta de ventas de ventas totales mensuales
        meta_ventas = obtener_meta_ventas(6)
        diccionario_anios_porcentajes = obtener_diccionario_anios_porcentajes(diccionario_anios_y_totales, meta_ventas)

        # se llena la tabla con los datos del diccionario
        llenar_datos_tabla(ventana_principal.tabla_ventas_totales_anuales, diccionario_anios_y_totales, diccionario_anios_porcentajes)

        # luego se vuelve a quitar el anio en curso, aunque este tenga ventas, es para
        # sacar el total sin incluir el total del anio en curso, ese total va a ser agregado al final
        # con la variable total_anio_en_curso
        diccionario_anios_y_totales.pop(anio_en_curso)
        total_ventas_sin_incluir_anio_en_curso = obtener_total_de_ventas(diccionario_anios_y_totales.values())
        # se le asigna el total al label de total, cuando se le asigna un texto a un label siempre tiene que ser un str o si no marca error
        ventana_principal.label_total_ventas_totales_anuales.setText(f"${str(total_ventas_sin_incluir_anio_en_curso)}")

        anio_menos_ventas, anio_mas_ventas = obtener_periodos_con_menos_y_mas_ventas(diccionario_anios_y_totales)
        
        ventana_principal.label_anio_menos_ventas_totales_anuales.setText(str(anio_menos_ventas))
        ventana_principal.label_anio_mas_ventas_totales_anuales.setText(str(anio_mas_ventas))

        ventana_principal.label_ventas_anio_en_curso_ventas_totales_anuales.setText(f"${str(total_anio_en_curso)}")

        # aqui finalmente se suman el total del anio en curso y los totales de los otros anios
        ventana_principal.label_ventas_totales_anio_actual_incluido_ventas_totales_anuales.setText(f"${str(total_ventas_sin_incluir_anio_en_curso + total_anio_en_curso)}")
        
        
if __name__ == '__main__':
    print("Este archivo no se ejecuta directamente")