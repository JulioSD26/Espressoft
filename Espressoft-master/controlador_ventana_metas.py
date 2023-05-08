from controlador_base_datos import crear_conexion
from PyQt5.QtWidgets import QMessageBox


class ControladorVentanaMetas():
    """
    Este controlador se va a encargar de darle funcionalidad a la ventana de metas.
    """

    def __init__(self, ventana_principal):
        self.colocar_datos_ventana_metas(ventana_principal)

        ventana_principal.boton_guardar_meta_ventas.clicked.connect(lambda: self.actualizar_metas_diarias(ventana_principal,ventana_principal.campo_meta_diaria_por_empleado.text()))

    def colocar_datos_ventana_metas(self, ventana_principal):
        """
        Coloca los datos de la tabla metas en las etiquetas correspondientes de la ventana de metas.
        """
        try:
            conn = crear_conexion()
            cursor = conn.cursor()
            # Seleccionar las metas correspondientes al empleado
            cursor.execute(f'SELECT meta_ventas FROM metas WHERE descripcion = "Metas diarias individuales"')
            meta_diaria_emp = cursor.fetchone()[0]
            cursor.execute(f'SELECT meta_ventas FROM metas WHERE descripcion = "Metas mensuales individuales"')
            meta_mensual_emp = cursor.fetchone()[0]
            cursor.execute(f'SELECT meta_ventas FROM metas WHERE descripcion = "Metas anuales individuales"')
            meta_anual_emp = cursor.fetchone()[0]
            cursor.execute(f'SELECT meta_ventas FROM metas WHERE descripcion = "Metas diarias totales"')
            meta_diaria_total = cursor.fetchone()[0]
            cursor.execute(f'SELECT meta_ventas FROM metas WHERE descripcion = "Metas mensuales totales"')
            meta_mensual_total = cursor.fetchone()[0]
            cursor.execute(f'SELECT meta_ventas FROM metas WHERE descripcion = "Metas anuales totales"')
            meta_anual_total = cursor.fetchone()[0]
            conn.close()
        except:
            ventana_principal.label_meta_diaria_empleado.setText("Error al obtener las metas")
            ventana_principal.label_meta_mensual_empleado.setText("Error al obtener las metas")
            ventana_principal.label_meta_anual_empleado.setText("Error al obtener las metas")
            ventana_principal.label_meta_diaria_total.setText("Error al obtener las metas")
            ventana_principal.label_meta_mensual_total.setText("Error al obtener las metas")
            ventana_principal.label_meta_anual_total.setText("Error al obtener las metas")
            return
        
        ventana_principal.label_meta_diaria_empleado.setText("${:,.2f}".format(meta_diaria_emp))
        ventana_principal.label_meta_mensual_empleado.setText("${:,.2f}".format(meta_mensual_emp))
        ventana_principal.label_meta_anual_empleado.setText("${:,.2f}".format(meta_anual_emp))
        ventana_principal.label_meta_diaria_total.setText("${:,.2f}".format(meta_diaria_total))
        ventana_principal.label_meta_mensual_total.setText("${:,.2f}".format(meta_mensual_total))
        ventana_principal.label_meta_anual_total.setText("${:,.2f}".format(meta_anual_total))

    def actualizar_metas_diarias(self, ventana_principal, meta_diaria_por_empleado_texto):
        try:
            conn = crear_conexion()
            cursor = conn.cursor()
            # convertir el valor de las metas diarias de texto a flotante
            meta_diaria_por_empleado = float(meta_diaria_por_empleado_texto)
            # actualizar las metas en la base de datos
            cursor.execute(f'UPDATE metas SET meta_ventas={meta_diaria_por_empleado} WHERE descripcion="Metas diarias individuales"')
            cursor.execute(f'UPDATE metas SET meta_ventas={meta_diaria_por_empleado*24} WHERE descripcion="Metas mensuales individuales"')
            cursor.execute(f'UPDATE metas SET meta_ventas={meta_diaria_por_empleado*24*12} WHERE descripcion="Metas anuales individuales"')
            # obtener el número de empleados activos
            cursor.execute('SELECT COUNT(*) FROM empleados WHERE estatus=1')
            num_empleados_activos = cursor.fetchone()[0]
            # actualizar las metas totales en la base de datos
            cursor.execute(f'UPDATE metas SET meta_ventas={meta_diaria_por_empleado*num_empleados_activos} WHERE descripcion="Metas diarias totales"')
            cursor.execute(f'UPDATE metas SET meta_ventas={meta_diaria_por_empleado*num_empleados_activos*24} WHERE descripcion="Metas mensuales totales"')
            cursor.execute(f'UPDATE metas SET meta_ventas={meta_diaria_por_empleado*num_empleados_activos*24*12} WHERE descripcion="Metas anuales totales"')
            conn.commit()
            conn.close()
            # llamar a la función de colocar los datos después de actualizar las metas
            self.colocar_datos_ventana_metas(ventana_principal)
        except:
            QMessageBox.showerror("Error", "Algo salió mal mientras se trataba de actualizar las metas en la base de datos.")
