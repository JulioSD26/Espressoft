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
from controlador_ventas_individuales_diarias import ControladorVentasIndividualesDiarias
from controlador_ventas_individuales_mensuales import ControladorVentasIndividualesMensuales
from controlador_ventas_totales_diarias import ControladorVentasTotalesDiarias
from controlador_ventas_totales_mensuales import ControladorVentasTotalesMensuales
from controlador_ventas_individuales_anuales import ControladorVentasIndividualesAnuales
from controlador_ventas_totales_anuales import ControladorVentasTotalesAnuales
from controlador_base_datos import *
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

        # al presionar el boton busca empleados, se manda a llamar al metodo buscar_empleados() que busca en la tabla de empleados
        self.boton_buscar_empleados.clicked.connect(lambda: buscar_empleados(
            self.tabla_empleados, self.campo_nombre_empleado_empleados.text()))

        self.boton_agregar_usuario.clicked.connect(lambda: vacia_campos(self.label_numero_empleado_agregar, self.campo_nombre_empleado_agregar, self.campo_apellido_paterno_agregar, self.campo_apellido_materno_agregar, self.campo_correo_empleado_agregar, 
                                                                        self.campo_numero_telefono_agregar, self.comboBox_tipo_empleado_agregar, self.comboBox_estatus_empleado_agregar, self.campo_contrasena_empleado_agregar, self.label_mensaje_agregar))
        self.boton_agregar_usuario.clicked.connect(lambda: obtener_ultimo_empleado_id(self.label_numero_empleado_agregar))

        # al presionar el boton de agregar, se manda a llamar al metodo agregar_empleado()
        self.boton_agregar_empleado_agregar.clicked.connect(lambda: agregar_empleado(self.label_numero_empleado_agregar.text(), self.campo_nombre_empleado_agregar.text(), self.campo_apellido_paterno_agregar.text(), self.campo_apellido_materno_agregar.text(
        ), self.campo_correo_empleado_agregar.text(), self.campo_numero_telefono_agregar.text(), self.comboBox_tipo_empleado_agregar.currentText(), self.comboBox_estatus_empleado_agregar.currentText(), self.campo_contrasena_empleado_agregar.text(), self.label_mensaje_agregar))
        self.boton_agregar_empleado_agregar.clicked.connect(lambda: vacia_campos(self.label_numero_empleado_agregar, self.campo_nombre_empleado_agregar, self.campo_apellido_paterno_agregar, self.campo_apellido_materno_agregar,
                                                            self.campo_correo_empleado_agregar, self.campo_numero_telefono_agregar, self.comboBox_tipo_empleado_agregar, self.comboBox_estatus_empleado_agregar, self.campo_contrasena_empleado_agregar, self.label_mensaje_editar))
        self.boton_agregar_empleado_agregar.clicked.connect(lambda: obtener_ultimo_empleado_id(self.label_numero_empleado_agregar))

        # al presionar el boton de buscar usuario se manda a llamar al metodo obtener_empleado_seleccionado() que obtiene el empleado seleccionado y llena los campos de texto
        self.boton_buscar_empleados_editar.clicked.connect(
            lambda: obtener_empleado(self.campo_busca_numero_empleado_editar.text()))
        self.boton_buscar_empleados_editar.clicked.connect(lambda: vacia_campos(self.label_numero_empleado_editar, self.campo_nombre_empleado_editar, self.campo_apellido_paterno_editar, self.campo_apellido_materno_editar,
                                                            self.campo_correo_empleado_editar, self.campo_numero_telefono_editar, self.comboBox_tipo_empleado_editar, self.comboBox_estatus_empleado_editar, self.campo_contrasena_empleado_editar, self.label_mensaje_editar))
        self.boton_buscar_empleados_editar.clicked.connect(lambda: llena_campos(self.label_numero_empleado_editar, self.campo_nombre_empleado_editar, self.campo_apellido_paterno_editar, self.campo_apellido_materno_editar,
                                                           self.campo_correo_empleado_editar, self.campo_numero_telefono_editar, self.comboBox_tipo_empleado_editar, self.comboBox_estatus_empleado_editar, self.campo_contrasena_empleado_editar, self.label_mensaje_editar))

        # al presionar el boton de guardar, se manda a llamar al metodo editar_empleado()
        self.boton_guardar_empleados_editar.clicked.connect(lambda: editar_empleado(self.label_numero_empleado_editar.text(), self.campo_nombre_empleado_editar.text(), self.campo_apellido_paterno_editar.text(), self.campo_apellido_materno_editar.text(
        ), self.campo_correo_empleado_editar.text(), self.campo_numero_telefono_editar.text(), self.comboBox_tipo_empleado_editar.currentText(), self.comboBox_estatus_empleado_editar.currentText(), self.campo_contrasena_empleado_editar.text(), self.label_mensaje_agregar))

        # se instancia el controlador de la ventana de importar datos, el cual le agrega la funcionalidad a esa ventana
        # se le pasa como argumento la ventana principal, MainWindow
        ControladorVentanaImportarDatos(self)

        # se instancia el controlador del menu lateral, el cual le agrega funcionalidad a este, pasandole como
        # argumento la ventana principal, MainWindow
        ControladorMenuLateral(self)

        # se instancia el controlador de ventas individuales diarias para darle funcionalidad a su ventana correspondiente
        ControladorVentasIndividualesDiarias(self)

        # se instancia el controlador de ventas totales diarias para darle funcionalidad a su ventana correspondiente
        ControladorVentasTotalesDiarias(self)

        # se instancia el controlador de ventas individuales mensuales para darle funcionalidad a su ventana correspondiente
        ControladorVentasIndividualesMensuales(self)

        # se instancia el controlador de ventas totales mensuales para darle funcionalidad a su ventana correspondiente
        ControladorVentasTotalesMensuales(self)

        # se instancia el controlador de ventas individuales anuales para darle funcionalidad a su ventana correspondiente
        ControladorVentasIndividualesAnuales(self)

        ControladorVentasTotalesAnuales(self)

        self.asignar_tipo_empleado_a_labels()

        self.asignar_fecha_actual_y_fecha_maxima_a_selectores_de_fecha_diarios()

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

        self.asignar_tipo_empleado_a_labels()

        self.asignar_fecha_actual_y_fecha_maxima_a_selectores_de_fecha_diarios()

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

        """
        Esto es para probar, se debe de cambiar.
        Los datos son de prueba.
        """
        """
        self.boton_generar_ventas_totales_diarias.clicked.connect(lambda: dibujar_grafica(self.grafica_ventas_totales_diarias, {
            '11:00 AM - 12:00 PM': 1550.32, 
            '12:00 PM - 01:00 PM': 0, 
            '01:00 PM - 02:00 PM': 0, 
            '02:00 PM - 03:00 PM': 0, 
            '03:00 PM - 04:00 PM': 893.0, 
            '04:00 PM - 05:00 PM': 0, 
            '05:00 PM - 06:00 PM': 345.0, 
            '06:00 PM - 07:00 PM': 752.0, 
            '07:00 PM - 08:00 PM': 0, 
            '08:00 PM - 09:00 PM': 200.0
            }))
        
        self.boton_generar_ventas_totales_mensuales.clicked.connect(lambda: dibujar_grafica(self.grafica_ventas_totales_mensuales, {
            'Ene': 1000, 
            'Feb': 2221.2, 
            'Mar': 891.3, 
            'Abr': 900, 
            'May': 1226.9, 
            'Jun': 1231, 
            'Jul': 3001, 
            'Ago': 713.90, 
            'Sept': 1236.08, 
            'Oct': 2831.87, 
            'Nov': 1220.98, 
            'Dic': 550.55
            }))
        # ventas totales anuales, no tiene un boton que genere los datos o busque a un empleado, por lo que se
        # intuye que se generan automaticamente al cargar la ventana
        dibujar_grafica(self.grafica_ventas_totales_anuales, {
            '2021': 15018.32,
            '2022': 22134.67
        })

        self.boton_generar_ventas_individuales_mensuales.clicked.connect(lambda: dibujar_grafica(
            self.grafica_ventas_individuales_mensuales, {
            'Ene': 1000, 
            'Feb': 2221.2, 
            'Mar': 891.3, 
            'Abr': 900, 
            'May': 1226.9, 
            'Jun': 1231, 
            'Jul': 3001, 
            'Ago': 713.90, 
            'Sept': 1236.08, 
            'Oct': 2831.87, 
            'Nov': 1220.98, 
            'Dic': 550.55
            }))
        
        self.boton_buscar_ventas_individuales_anuales.clicked.connect(lambda: dibujar_grafica(self.grafica_ventas_individuales_anuales, {
            '2020': 7850.12,
            '2021': 15018.32,
            '2022': 22134.67,
            '2023': 16012
        }))
        """

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
