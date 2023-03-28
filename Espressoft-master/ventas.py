# se importan todos los componentes de la ui generada automaticamente
# ventas_ui.py se genera automaticamente al guardar el .ui en QT Designer y al utilizar el comando:
# pyuic5 -x (ruta_archivo.ui) -o (ruta_archivo_a_generar_ui.py)
# despues de -x va la ruta del archivo .ui que se quiere transformar y despues de -o (output) va la ruta del archivo que se va a generar
# Ejemplo (usando rutas relativas):
# pyuic5 -x ventas.ui -o ventas_ui.py
from ventas_ui import *
from controlador_grafica_ventas import *
from controlador_ventana_importar_datos import ControladorVentanaImportarDatos
from controlador_menu_lateral import ControladorMenuLateral
import empleados
import datetime

# se crea una clase que representa a la ventana principal, la cual hereda de la clase general del widget QMainWindows
# y tambien hereda de la clase que se genera automaticamente para la ui de la ventana principal (MainWindows)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        # con esto se agregan las fuentes custom para que se puedan usar aqui en los stylesheets con CSS
        QtGui.QFontDatabase.addApplicationFont(
            'resources/fonts/Montserrat-Regular.ttf')

        # setupUi genera la interfaz con todos los componentes hechos en QT Designer, se le pasa self
        # como el propio objeto de MainWindow
        self.setupUi(self)

        # el stacked widget es como un componente que permite tener varias paginas en el mismo lugar
        # de este modo las paginas de cada una de las opciones como ventas totales diarias, mensuales, empleados...
        # pertenecen al stacked widget y estas se cambian cuando se presiona el boton de su opcion correspondiente
        # al principio va a aparecer una "pagina" por defecto cuando no se ha seleccionado ninguna opcion
        self.stacked_widget_paginas.setCurrentWidget(self.pagina_por_defecto)

        # se instancia el controlador de la ventana de importar datos, el cual le agrega la funcionalidad a esa ventana
        # se le pasa como argumento la ventana principal, MainWindow
        ControladorVentanaImportarDatos(self)

        # se instancia el controlador del menu lateral, el cual le agrega funcionalidad a este, pasandole como
        # argumento la ventana principal, MainWindow
        ControladorMenuLateral(self)

        self.asignar_tipo_empleado_a_labels()

        self.asignar_fecha_actual_y_fecha_maxima_a_selectores_de_fecha_diarios()

        """
        Esto es solo para probar las graficas, se debe de quitar o cambiar
        """

        estilizar_grafica(self.grafica_ventas_totales_diarias,
                          "Ventas totales diarias")
        estilizar_grafica(self.grafica_ventas_totales_mensuales,
                          "Ventas totales mensuales")
        estilizar_grafica(self.grafica_ventas_totales_anuales,
                          "Ventas totales anuales")
        estilizar_grafica(self.grafica_ventas_individuales_diarias,
                          "Ventas individuales diarias")
        estilizar_grafica(
            self.grafica_ventas_individuales_mensuales, "Ventas individuales mensuales")
        estilizar_grafica(self.grafica_ventas_individuales_anuales,
                          "Ventas individuales anuales")

        self.boton_generar_ventas_totales_diarias.clicked.connect(lambda: dibujar_grafica(self.grafica_ventas_totales_diarias, [
                                                                  '3:00 pm - 4:00 pm', '4:00 pm - 5:00 pm', '5:00 pm - 6:00 pm', '6:00 pm - 7:00 pm', '7:00 pm - 8:00 pm', '8:00 pm - 9:00 pm']))
        self.boton_generar_ventas_totales_mensuales.clicked.connect(lambda: dibujar_grafica(self.grafica_ventas_totales_mensuales, [
                                                                    'Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sept', 'Oct', 'Nov', 'Dic']))
        # tanto ventas individuales diarias, como ventas totales diarias no tienen un boton de generar, por lo que se
        # intuye que se generan automaticamente al cargar la ventana
        dibujar_grafica(self.grafica_ventas_totales_anuales, ['2020', '2021'])

        self.boton_generar_ventas_individuales_diarias.clicked.connect(lambda: dibujar_grafica(self.grafica_ventas_individuales_diarias, [
                                                                       '3:00 pm - 4:00 pm', '4:00 pm - 5:00 pm', '5:00 pm - 6:00 pm', '6:00 pm - 7:00 pm', '7:00 pm - 8:00 pm', '8:00 pm - 9:00 pm']))
        self.boton_generar_ventas_individuales_mensuales.clicked.connect(lambda: dibujar_grafica(
            self.grafica_ventas_individuales_mensuales, ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sept', 'Oct', 'Nov', 'Dic']))
        dibujar_grafica(self.grafica_ventas_individuales_anuales, [
                        '2019', '2020', '2021', '2022', '2023'])

    def asignar_tipo_empleado_a_labels(self):
        """
        A todas las ventanas que tengan un label con el tipo de empleado, les asigna el tipo de empleado del empleado que hizo login.
        """
        labels_tipo_empleado = [
            self.label_tipo_usuario_ventas_totales_diarias,
            self.label_tipo_usuario_ventas_totales_mensuales,
            self.label_tipo_usuario_ventas_totales_anuales,
            self.label_tipo_usuario_ventas_individuales_diarias,
            self.label_tipo_usuario_ventas_individuales_mensuales,
            self.label_tipo_usuario_ventas_individuales_anuales,
            self.label_tipo_usuario_empleados,
            self.label_tipo_usuario_importar_datos,
            self.label_tipo_usuario_agregar_usuario,
            self.label_tipo_usuario_editar_usuario
        ]

        # se obtiene al tipo de empleado loggeado, primero obteniendo al objeto empleado, luego su atributo tipo_empleado
        # y finalmente se pasa a mayusculas
        tipo_empleado_loggeado = empleados.obtener_usuario_loggeado().tipo_empleado.upper()
        for label in labels_tipo_empleado:
            # a cada label/etiqueta se le asigna ese tipo de empleado
            label.setText(tipo_empleado_loggeado)

    def asignar_fecha_actual_y_fecha_maxima_a_selectores_de_fecha_diarios(self):
        """
        Asigna una fecha actual y una fecha maxima a los selectores donde se puede seleccionar por dia
        (Ventas individuales diarias y Ventas totales diarias).
        """
        selectores_fecha_diarios = [
            self.fecha_seleccionada_ventas_individuales_diarias, self.fecha_seleccionada_ventas_totales_diarias]
        for selector in selectores_fecha_diarios:
            # le pone como fecha por defecto, el dia actual
            selector.setDate(datetime.datetime.now())
            # le pone como fecha maxima, el dia actual
            selector.setMaximumDate(datetime.datetime.now())


if __name__ == "__main__":
    print("Este archivo no se ejecuta directamente")
