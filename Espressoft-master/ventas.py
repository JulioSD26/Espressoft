# se importan todos los componentes de la ui generada automaticamente
# ventas_ui.py se genera automaticamente al guardar el .ui en QT Designer y al utilizar el comando:
# pyuic5 -x (ruta_archivo.ui) -o (ruta_archivo_a_generar_ui.py)
# despues de -x va la ruta del archivo .ui que se quiere transformar y despues de -o (output) va la ruta del archivo que se va a generar
# Ejemplo (usando rutas relativas):
# pyuic5 -x ventas.ui -o ventas_ui.py
from ventas_ui import *
from controlador_grafica_ventas import *
from controlador_base_datos import *
import empleados
import datetime

# se crea una clase que representa a la ventana principal, la cual hereda de la clase general del widget QMainWindows
# y tambien hereda de la clase que se genera automaticamente para la ui de la ventana principal (MainWindows)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        
        # con esto se agregan las fuentes custom para que se puedan usar aqui en los stylesheets con CSS
        QtGui.QFontDatabase.addApplicationFont('resources/fonts/Montserrat-Regular.ttf')

        # setupUi genera la interfaz con todos los componentes hechos en QT Designer, se le pasa self
        # como el propio objeto de MainWindow
        self.setupUi(self)

        """
        ESTADOS DE INICIO
        """
        # el nombre que se le haya dado al componente en QT Designer, es el nombre que se utiliza para acceder 
        # a ese componente aqui, como atributo del objeto que lo contiene (MainWindow)
        # Ejemplo: Si en QT Designer a un boton se le puso el nombre "opciones_ventas_totales", para acceder
        # a ese componente desde aqui, se usaria algo como "self.opciones_ventas_totales" y con eso se puede
        # operar con el componente, como agregarle eventos o personalizarlo

       
        # en QT Designer hay un widget que contiene a los botones Ventas diarias, Ventas mensuales y Ventas anuales
        # para las ventas totales y otro para las ventas individuales respectivamente.
        # QT Designer no deja ocultar widgets/componentes al inicio de la aplicacion, por lo que aqui se ocultan
        # manualmente al principio usando el metodo .setHidden() y luego se muestran cuando se presionan los botones
        # desplegables de Ventas totales y/o Ventas individuales

        self.opciones_ventas_totales.setHidden(True)

        self.opciones_ventas_individuales.setHidden(True)

        # el stacked widget es como un componente que permite tener varias paginas en el mismo lugar
        # de este modo las paginas de cada una de las opciones como ventas totales diarias, mensuales, empleados...
        # pertenecen al stacked widget y estas se cambian cuando se presiona el boton de su opcion correspondiente
        # al principio va a aparecer una "pagina" por defecto cuando no se ha seleccionado ninguna opcion
        self.stacked_widget_paginas.setCurrentWidget(self.pagina_por_defecto)

        """
        EVENTOS: PRESIONAR UN BOTON
        """

        # mediante el atributo clicked de un boton (QButtonPush) y usando el metodo .connect(), se puede asociar
        # una funcion al boton cuando este se presione.
        # por defecto, la funcion/metodo solo se puede pasar con su nombre sin parentesis (sin parametros), por que si no se estaria llamando cada
        # vez que inicia la aplicacion, para eso se utiliza una funcion lambda que si lo permite

        # los botones que pueden desplegar mas botones, estan constituidos de 2 botones que realizan la misma funcion, un boton que contiene el texto
        # del boton (por ejemplo Ventas totales) y otro que contiene el icono desplegable (el triangulito), cuando se presiona uno de estos 2,
        # "despliegan" los botones que le corresponden (por ejemplo si se presiona el boton Ventas totales o su boton correspondiente desplegable, este va a desplegar a 
        # los botones Ventas diarias, Ventas mensuales, Ventas anuales, que en realidead es el widget que los contiene) 

        # son 2 botones separados y no estan juntos en un solo boton (texto e icono), porque era complicado acomodarlos responsivamente para que el boton
        # de texto siempre estuviera pegado al borde izquierdo del menu lateral y el boton desplegable cerca del borde derecho del menu lateral
        self.boton_ventas_totales.clicked.connect(lambda: self.ocultar_mostrar_opciones(self.boton_ventas_totales, self.boton_ventas_totales_desplegable, self.opciones_ventas_totales))
        self.boton_ventas_totales_desplegable.clicked.connect(lambda: self.ocultar_mostrar_opciones(self.boton_ventas_totales, self.boton_ventas_totales_desplegable, self.opciones_ventas_totales))

        self.boton_ventas_individuales.clicked.connect(lambda: self.ocultar_mostrar_opciones(self.boton_ventas_individuales, self.boton_ventas_individuales_desplegable, self.opciones_ventas_individuales))
        self.boton_ventas_individuales_desplegable.clicked.connect(lambda: self.ocultar_mostrar_opciones(self.boton_ventas_individuales, self.boton_ventas_individuales_desplegable, self.opciones_ventas_individuales))

        # el boton de empleados no es un boton desplegable, por lo que solo se le asocia el metodo agregar_quitar_borde_izquierdo_boton() el cual al
        # presionarse simplemente se le agrega el borde izquierdo
        self.boton_empleados.clicked.connect(lambda: self.agregar_quitar_borde_izquierdo_boton(self.boton_empleados, True))

        # al presionar el boton de empleados manda a llamar al metodo llenar_tabla_empleados() que llena la tabla de empleados
        self.boton_empleados.clicked.connect(lambda: llenar_tabla_empleados(self.tabla_empleados))

        # al presionar el boton busca empleados, se manda a llamar al metodo buscar_empleados() que busca en la tabla de empleados
        self.boton_buscar_empleados.clicked.connect(lambda: buscar_empleados(self.tabla_empleados, self.campo_nombre_empleado_empleados.text()))

        # el boton para cerrar la aplicacion
        self.boton_cerrar.clicked.connect(self.cerrar)

        # a los botones que son desplegados por sus botones desplegables "padres", se les asigna un mismo evento en comun
        # Un boton desplegable padre seria Ventas totales, mientras que sus botones desplegados serian Ventas diarias, mensuales y anuales, 
        # asi como para el boton desplegable padre Ventas individuales
        botones_desplegados_totales =  [self.boton_ventas_totales_diarias, self.boton_ventas_totales_mensuales, self.boton_ventas_totales_anuales]
        self.agregar_evento_estilizar_seleccion_a_botones_desplegados(botones_desplegados_totales)

        botones_desplegados_individuales = [self.boton_ventas_individuales_diarias, self.boton_ventas_individuales_mensuales, self.boton_ventas_individuales_anuales]
        self.agregar_evento_estilizar_seleccion_a_botones_desplegados(botones_desplegados_individuales)

        # esta lista va a ser util para saber que botones pueden tener un borde izquierdo al ser presionados ellos o alguno de sus botones desplegados hijos
        self.botones_con_posible_borde_izquierdo = [self.boton_ventas_totales, self.boton_ventas_individuales, self.boton_empleados]
        # a los botones de esta lista ya se les habia agregado un evento, sin embargo es posible agregar mas de un evento
        # a los botones, en este caso se les va a agregar el evento de quitar negritas a los botones desplegados hijos, cuando
        # sean presionados
        for boton in self.botones_con_posible_borde_izquierdo:
            # se le pasa un None para que al momento de evaluar, este metodo le quite las negritas a todos los botones
            # desplegados hijos y no deje a alguno en negritas.
            boton.clicked.connect(lambda: self.quitar_negritas_a_otros_botones(None))


        # este diccionario va a guardar la relacion entre los botones desplegables padre (Ventas totales y Ventas individuales) y sus
        # botones desplegados hijos (Ventas diarias, Ventas mensuales y Ventas anuales)
        # tiene la estructura: {boton_desplegable_padre_1: [boton_desplegado_hijo_1, boton_desplegado_hijo2, ...], boton_desplegable_padre_2: [...]}
        self.diccionario_relacion_botones_desplegables_y_desplegados = {
            self.boton_ventas_totales: botones_desplegados_totales,
            self.boton_ventas_individuales: botones_desplegados_individuales
        }


        # este diccionario va a guardar la relacion entre el boton de opciones seleccionado en el menu lateral
        # y su pagina correspondiente en el stacked widget
        self.relacion_botones_opciones_y_su_pagina_correspondiente = {
            self.boton_ventas_totales_diarias: self.pagina_ventas_totales_diarias,
            self.boton_ventas_totales_mensuales: self.pagina_ventas_totales_mensuales,
            self.boton_ventas_totales_anuales: self.pagina_ventas_totales_anuales,
            self.boton_ventas_individuales_diarias: self.pagina_ventas_individuales_diarias,
            self.boton_ventas_individuales_mensuales: self.pagina_ventas_individuales_mensuales,
            self.boton_ventas_individuales_anuales: self.pagina_ventas_individuales_anuales,
            self.boton_empleados: self.pagina_empleados
        }
        
        # a los botones de opciones que eran las llaves del diccionario relacion_botones_opciones_y_su_pagina_correspondiente,
        # se les agrega el eventp de cambiar la pagina en el stacked widget correspondiente al boton seleccionado
        for boton_opcion in self.relacion_botones_opciones_y_su_pagina_correspondiente:
            boton_opcion.clicked.connect(self.cambiar_pagina_al_seleccionar_opcion)


        
        self.asignar_tipo_empleado_a_labels()


        self.asignar_fecha_actual_y_fecha_maxima_a_selectores_de_fecha_diarios()


        """
        Esto es solo para probar las graficas, se debe de quitar o cambiar
        """
        
        estilizar_grafica(self.grafica_ventas_totales_diarias, "Ventas totales diarias")
        estilizar_grafica(self.grafica_ventas_totales_mensuales, "Ventas totales mensuales")
        estilizar_grafica(self.grafica_ventas_totales_anuales, "Ventas totales anuales")
        estilizar_grafica(self.grafica_ventas_individuales_diarias, "Ventas individuales diarias")
        estilizar_grafica(self.grafica_ventas_individuales_mensuales, "Ventas individuales mensuales")
        estilizar_grafica(self.grafica_ventas_individuales_anuales, "Ventas individuales anuales")


        

        self.boton_generar_ventas_totales_diarias.clicked.connect(lambda: dibujar_grafica(self.grafica_ventas_totales_diarias, ['3:00 pm - 4:00 pm', '4:00 pm - 5:00 pm', '5:00 pm - 6:00 pm', '6:00 pm - 7:00 pm', '7:00 pm - 8:00 pm', '8:00 pm - 9:00 pm']))
        self.boton_generar_ventas_totales_mensuales.clicked.connect(lambda: dibujar_grafica(self.grafica_ventas_totales_mensuales, ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sept', 'Oct', 'Nov', 'Dic']))
        # tanto ventas individuales diarias, como ventas totales diarias no tienen un boton de generar, por lo que se
        # intuye que se generan automaticamente al cargar la ventana
        dibujar_grafica(self.grafica_ventas_totales_anuales, ['2020', '2021'])

        self.boton_generar_ventas_individuales_diarias.clicked.connect(lambda: dibujar_grafica(self.grafica_ventas_individuales_diarias, ['3:00 pm - 4:00 pm', '4:00 pm - 5:00 pm', '5:00 pm - 6:00 pm', '6:00 pm - 7:00 pm', '7:00 pm - 8:00 pm', '8:00 pm - 9:00 pm']))
        self.boton_generar_ventas_individuales_mensuales.clicked.connect(lambda: dibujar_grafica(self.grafica_ventas_individuales_mensuales, ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sept', 'Oct', 'Nov', 'Dic']))
        dibujar_grafica(self.grafica_ventas_individuales_anuales, ['2019', '2020', '2021', '2022', '2023'])

    def ocultar_mostrar_opciones(self, boton_texto, boton_desplegable_correspondiente, widget_opciones):
        """
        Oculta o Muestra los widgets que contienen a botones que aparecen al ser desplegados por su boton_texto o boton_desplegable_correspondiente, de modo que da el efecto de un desplegable.
        Recibe como parametros el "boton_texto" que es el boton que contiene texto (Ventas totales o Ventas individuales), el boton_desplegable_correspondiente (los cuales pueden presionarse para cumplir la misma funcion)
        y el widget que se va a ocultar o mostrar.
        """
        # se checa si el widget ya se encuentra oculto (al iniciar la aplicacion va a empezar oculto)
        if widget_opciones.isHidden():
            # como se encuentra oculto y se presiono uno de los 2 botones para mostrarlo, entonces el boton que contiene al icono desplegable, se "voltea",
            # cambiando la imagen (para que de un efecto de desplegable)
            boton_desplegable_correspondiente.setIcon(QtGui.QIcon('resources/img/icono_desplegable_volteado.png'))
            # se le agrega el borde izquierdo blanco que aparece en el disenio al boton que contiene el texto
            self.agregar_quitar_borde_izquierdo_boton(boton_texto, True)
        else:
            # si no se encuentra oculto y se presiono uno de los 2 botones para mostrarlo, entonces el boton que contiene al icono desplegable, vuelve
            # a su estado "normal" cambiando a la imagen original
            boton_desplegable_correspondiente.setIcon(QtGui.QIcon('resources/img/icono_desplegable.png'))
            # se le quita el borde izquierdo al boton que contiene el texto
            self.agregar_quitar_borde_izquierdo_boton(boton_texto, False)
        # finalmente el widget de opciones/botones se oculta o muestra, dependiendo de si se encuentra oculto o no
        # si el widget esta oculto, entonces widget_opciones.isHidden() = True, por lo que:
        # widget_opciones.setHidden(not True)
        # widget_opciones.setHidden(False)  ----> Se muestra
        # si el widget no esta oculto, entonces widget_opciones.isHidden() = False, por lo que:
        # widget_opciones.setHidden(not False)
        # widget_opciones.setHidden(True)  ----> Se oculta
        widget_opciones.setHidden(not widget_opciones.isHidden())


    def agregar_quitar_borde_izquierdo_boton(self, boton, agregar: bool):
        """
        Agrega o quita el borde izquierdo (es de color blanco como en el disenio) de un boton determinado.
        Recibe como parametros el boton a agregar o quitar borde izquierdo y un booleano agregar, que si es True, entonces se agrega, en caso contrario se quita
        """
        if agregar:
            # se modifica la hoja de estilos del boton, manteniendo los atributos que ya tenia y agregandole la propiedad border-left
            # ademas se pone en negritas al boton desplegable padre (font-weight: bold;)
            boton.setStyleSheet(
                """
                QPushButton {
                    color: rgb(255, 255, 255);
                    font-family: 'Montserrat';
                    font-style: normal;
                    font-weight: bold;
                    font-size: 16px;
                    border: none;
                    padding: 10px;
                    border-left: 3px solid white;
                }
            """
            )
            # se le quita el borde izquierdo a los demas botones
            self.quitar_borde_izquierdo_a_otros_botones(boton)
        else:
            # se le quita la propiedad border-left
            # ademas se le quita las negritas al boton desplegable padre (font-weight: 400;)
            boton.setStyleSheet(
                """
                QPushButton {
                    color: rgb(255, 255, 255);
                    font-family: 'Montserrat';
                    font-style: normal;
                    font-weight: 400;
                    font-size: 16px;
                    border: none;
                    padding: 10px;
                }
            """
            )


    def quitar_borde_izquierdo_a_otros_botones(self, boton_presionado):
        """
        Quita el borde izquierdo a los botones que no sean el ultimo boton_presionado.
        Recibe como parametro el boton_presionado, el cual es el unico que va a mantener el borde izquierdo
        """
        for boton in self.botones_con_posible_borde_izquierdo:
            if boton is not boton_presionado:
                # se le quita el borde izquierdo a todos los botones que puedan tener borde izquierdo y que no son el boton_presionado
                self.agregar_quitar_borde_izquierdo_boton(boton, False)

    
    def agregar_evento_estilizar_seleccion_a_botones_desplegados(self, botones_desplegados):
        """
        Agrega el evento/metodo estilizar_seleccion() a una lista de botones desplegados.
        Recibe como parametro una lista de botones desplegados pertenecientes a un boton desplegable padre.
        """
        # mediante la referencia del objeto se asignan los eventos
        for boton in botones_desplegados:
            boton.clicked.connect(self.estilizar_seleccion)

        
    def obtener_boton_desplegable_padre(self, boton_desplegado):
        """
        Regresa al boton desplegable padre, dado un boton_desplegado hijo.
        """
        # se recorren los elementos del diccionario que tiene la relacion entre los botones desplegables padre y los botones desplegados hijos.
        # donde la llave es boton_desplegable_padre y su valor es una lista "botones_desplegados_hijos".
        for boton_desplegable_padre, botones_desplegados_hijos in self.diccionario_relacion_botones_desplegables_y_desplegados.items():
            # si el boton desplegado hijo se encuentra entre los hijos del boton desplegable padre, entonces se regresa al boton desplegable padre
            if boton_desplegado in botones_desplegados_hijos:
                #print(boton_desplegable_padre.text())
                #print(boton_desplegado.text())
                return boton_desplegable_padre



    def estilizar_seleccion(self):
        """
        Pone en negritas al boton desplegado hijo de un boton desplegable padre, quitandole esta propiedad a los
        otros botones desplegados hijos y agregandole el borde izquierdo al boton desplegable padre correspondiente.
        """
        # self.sender() representa al widget que mando la señal (signal), en este caso seran
        # los botones desplegados
        # print(self.sender().text())
        # con self.sender() se puede saber que boton es el que fue presionado y llamó a este evento
        boton_desplegado_seleccionado = self.sender()
        # se le quita las negritas al texto de los botones que no sean el boton desplegado seleccionado
        self.quitar_negritas_a_otros_botones(boton_desplegado_seleccionado)

        # se pone en negritas (bold) el texto del boton desplegado seleccionado
        # boton_desplegado_seleccionado.setStyleSheet('color: rgb(255, 255, 255);' 'font: 75 12pt "Times New Roman";' 'border: none;' 'font-weight: bold;')
        boton_desplegado_seleccionado.setStyleSheet(
            """
            QPushButton {
                color: rgb(255, 255, 255);
                font-family: 'Montserrat';
                font-style: normal;
                font-weight: bold;
                font-size: 16px;
                border: none;
            }
            """
        )
        # se obtiene al boton desplegable padre del boton desplegado seleccionado
        boton_desplegable_padre = self.obtener_boton_desplegable_padre(boton_desplegado_seleccionado)
        # al boton desplegable padre se le agrega el borde izquierdo, mientras que a los otros se les quita 
        self.agregar_quitar_borde_izquierdo_boton(boton_desplegable_padre, True)


    def quitar_negritas_a_otros_botones(self, boton_desplegado_seleccionado):
        """
        Modifica el atributo font-weight, asignandolo a font-weight: 400; (de modo que pierde el valor bold) de una lista de botones desplegados que no sean el boton desplegado seleccionado que se recibe como parametro.
        """
        # se obtienen las listas de botones desplegados del diccionario de relacion entre los botones desplegables padre y los botones desplegados hijos.
        listas_botones_desplegados = self.diccionario_relacion_botones_desplegables_y_desplegados.values()
        # por cada lista en las listas de botones desplegados
        for lista_botones_desplegados in listas_botones_desplegados:
            for boton_desplegado in lista_botones_desplegados:
                # si el boton desplegado no es el boton desplegado seleccionado.
                # aqui es importante usar el is y no el ==, porque el primero checa por referencia, mientras que el segundo checa por valor
                if boton_desplegado is not boton_desplegado_seleccionado:
                    # se le modifica el font-weight a 400
                    boton_desplegado.setStyleSheet(
                        """
                        QPushButton {
                            color: rgb(255, 255, 255);
                            font-family: 'Montserrat';
                            font-style: normal;
                            font-weight: 400;
                            font-size: 16px;
                            border: none;
                        }
                        """
                    )

    
    def cambiar_pagina_al_seleccionar_opcion(self):
        """
        Cambia la pagina/pantalla del stack widget que contiene la informacion, graficas y/o estadisticas de la opcion seleccionada por el boton correspondiente.
        """
        # se obtiene al boton que mando la senial, como por ejemplo el boton de opcion Ventas totales diarias o el boton de opcion Empleados
        boton_opcion_seleccionado = self.sender()
        # se obtiene el valor (pagina correspondiente del boton de opciones seleccionado) del diccionario de la relacion entre botones de opciones y su pagina correspondiete
        pagina_a_mostrar = self.relacion_botones_opciones_y_su_pagina_correspondiente.get(boton_opcion_seleccionado)
        # al stacked widget se le asigna la pagina a mostrar que se haya elegido al presionar su boton de opciones,
        # dando el efecto de que se cambio la pantalla
        self.stacked_widget_paginas.setCurrentWidget(pagina_a_mostrar)

    
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
            self.label_tipo_usuario_empleados
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
        selectores_fecha_diarios = [self.fecha_seleccionada_ventas_individuales_diarias, self.fecha_seleccionada_ventas_totales_diarias]
        for selector in selectores_fecha_diarios:
            # le pone como fecha por defecto, el dia actual
            selector.setDate(datetime.datetime.now())
            # le pone como fecha maxima, el dia actual
            selector.setMaximumDate(datetime.datetime.now())



    
    def cerrar(self):
        """
        Cierra la aplicacion.
        """
        self.close()


if __name__ == "__main__":
    print("Este archivo no se ejecuta directamente")