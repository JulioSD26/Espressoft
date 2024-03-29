# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventas.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1352, 914)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/img/icono_cafe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu_lateral = QtWidgets.QFrame(self.centralwidget)
        self.menu_lateral.setMaximumSize(QtCore.QSize(300, 16777215))
        self.menu_lateral.setStyleSheet("#menu_lateral {\n"
"    background-color: rgb(65, 107, 191);\n"
"}")
        self.menu_lateral.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_lateral.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_lateral.setObjectName("menu_lateral")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu_lateral)
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo_cafe_indigo = QtWidgets.QLabel(self.menu_lateral)
        self.logo_cafe_indigo.setMinimumSize(QtCore.QSize(89, 89))
        self.logo_cafe_indigo.setMaximumSize(QtCore.QSize(89, 89))
        self.logo_cafe_indigo.setText("")
        self.logo_cafe_indigo.setPixmap(QtGui.QPixmap("resources/img/icono_cafe.png"))
        self.logo_cafe_indigo.setScaledContents(True)
        self.logo_cafe_indigo.setWordWrap(False)
        self.logo_cafe_indigo.setObjectName("logo_cafe_indigo")
        self.verticalLayout_2.addWidget(self.logo_cafe_indigo, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, -1, 4, -1)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.boton_ventas_totales = QtWidgets.QPushButton(self.menu_lateral)
        self.boton_ventas_totales.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.boton_ventas_totales.setAutoFillBackground(False)
        self.boton_ventas_totales.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"    padding: 10px;\n"
"}")
        self.boton_ventas_totales.setObjectName("boton_ventas_totales")
        self.horizontalLayout_3.addWidget(self.boton_ventas_totales, 0, QtCore.Qt.AlignRight)
        self.boton_ventas_totales_desplegable = QtWidgets.QToolButton(self.menu_lateral)
        self.boton_ventas_totales_desplegable.setStyleSheet("border: none;")
        self.boton_ventas_totales_desplegable.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/img/icono_desplegable.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_ventas_totales_desplegable.setIcon(icon1)
        self.boton_ventas_totales_desplegable.setObjectName("boton_ventas_totales_desplegable")
        self.horizontalLayout_3.addWidget(self.boton_ventas_totales_desplegable)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.opciones_ventas_totales = QtWidgets.QWidget(self.menu_lateral)
        self.opciones_ventas_totales.setStyleSheet("")
        self.opciones_ventas_totales.setObjectName("opciones_ventas_totales")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.opciones_ventas_totales)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(80, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.boton_ventas_totales_diarias = QtWidgets.QPushButton(self.opciones_ventas_totales)
        self.boton_ventas_totales_diarias.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.boton_ventas_totales_diarias.setAutoFillBackground(False)
        self.boton_ventas_totales_diarias.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"}")
        self.boton_ventas_totales_diarias.setObjectName("boton_ventas_totales_diarias")
        self.verticalLayout_4.addWidget(self.boton_ventas_totales_diarias, 0, QtCore.Qt.AlignRight)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.boton_ventas_totales_mensuales = QtWidgets.QPushButton(self.opciones_ventas_totales)
        self.boton_ventas_totales_mensuales.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.boton_ventas_totales_mensuales.setAutoFillBackground(False)
        self.boton_ventas_totales_mensuales.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"}\n"
"")
        self.boton_ventas_totales_mensuales.setObjectName("boton_ventas_totales_mensuales")
        self.verticalLayout_4.addWidget(self.boton_ventas_totales_mensuales, 0, QtCore.Qt.AlignRight)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.boton_ventas_totales_anuales = QtWidgets.QPushButton(self.opciones_ventas_totales)
        self.boton_ventas_totales_anuales.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.boton_ventas_totales_anuales.setAutoFillBackground(False)
        self.boton_ventas_totales_anuales.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"}\n"
"")
        self.boton_ventas_totales_anuales.setObjectName("boton_ventas_totales_anuales")
        self.verticalLayout_4.addWidget(self.boton_ventas_totales_anuales, 0, QtCore.Qt.AlignRight)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addWidget(self.opciones_ventas_totales)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, 4, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.boton_ventas_individuales = QtWidgets.QPushButton(self.menu_lateral)
        self.boton_ventas_individuales.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.boton_ventas_individuales.setAutoFillBackground(False)
        self.boton_ventas_individuales.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"    padding: 10px;\n"
"}")
        self.boton_ventas_individuales.setObjectName("boton_ventas_individuales")
        self.horizontalLayout_4.addWidget(self.boton_ventas_individuales, 0, QtCore.Qt.AlignRight)
        self.boton_ventas_individuales_desplegable = QtWidgets.QToolButton(self.menu_lateral)
        self.boton_ventas_individuales_desplegable.setStyleSheet("border: none;")
        self.boton_ventas_individuales_desplegable.setText("")
        self.boton_ventas_individuales_desplegable.setIcon(icon1)
        self.boton_ventas_individuales_desplegable.setObjectName("boton_ventas_individuales_desplegable")
        self.horizontalLayout_4.addWidget(self.boton_ventas_individuales_desplegable)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.opciones_ventas_individuales = QtWidgets.QWidget(self.menu_lateral)
        self.opciones_ventas_individuales.setStyleSheet("")
        self.opciones_ventas_individuales.setObjectName("opciones_ventas_individuales")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.opciones_ventas_individuales)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(80, -1, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem8)
        self.boton_ventas_individuales_diarias = QtWidgets.QPushButton(self.opciones_ventas_individuales)
        self.boton_ventas_individuales_diarias.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.boton_ventas_individuales_diarias.setAutoFillBackground(False)
        self.boton_ventas_individuales_diarias.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"}")
        self.boton_ventas_individuales_diarias.setObjectName("boton_ventas_individuales_diarias")
        self.verticalLayout_5.addWidget(self.boton_ventas_individuales_diarias, 0, QtCore.Qt.AlignRight)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        self.boton_ventas_individuales_mensuales = QtWidgets.QPushButton(self.opciones_ventas_individuales)
        self.boton_ventas_individuales_mensuales.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.boton_ventas_individuales_mensuales.setAutoFillBackground(False)
        self.boton_ventas_individuales_mensuales.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"}")
        self.boton_ventas_individuales_mensuales.setObjectName("boton_ventas_individuales_mensuales")
        self.verticalLayout_5.addWidget(self.boton_ventas_individuales_mensuales, 0, QtCore.Qt.AlignRight)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem10)
        self.boton_ventas_individuales_anuales = QtWidgets.QPushButton(self.opciones_ventas_individuales)
        self.boton_ventas_individuales_anuales.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.boton_ventas_individuales_anuales.setAutoFillBackground(False)
        self.boton_ventas_individuales_anuales.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"}")
        self.boton_ventas_individuales_anuales.setObjectName("boton_ventas_individuales_anuales")
        self.verticalLayout_5.addWidget(self.boton_ventas_individuales_anuales, 0, QtCore.Qt.AlignRight)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem11)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addWidget(self.opciones_ventas_individuales)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem12)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(0, -1, 4, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.boton_empleados = QtWidgets.QPushButton(self.menu_lateral)
        self.boton_empleados.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.boton_empleados.setAutoFillBackground(False)
        self.boton_empleados.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"    padding: 10px;\n"
"}")
        self.boton_empleados.setObjectName("boton_empleados")
        self.horizontalLayout_5.addWidget(self.boton_empleados)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem14)
        self.horizontalLayout_106 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_106.setContentsMargins(0, -1, 4, -1)
        self.horizontalLayout_106.setObjectName("horizontalLayout_106")
        self.boton_agregar_usuario = QtWidgets.QPushButton(self.menu_lateral)
        self.boton_agregar_usuario.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.boton_agregar_usuario.setAutoFillBackground(False)
        self.boton_agregar_usuario.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"    padding: 10px;\n"
"}")
        self.boton_agregar_usuario.setObjectName("boton_agregar_usuario")
        self.horizontalLayout_106.addWidget(self.boton_agregar_usuario)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_106.addItem(spacerItem15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_106)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem16)
        self.horizontalLayout_109 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_109.setContentsMargins(0, -1, 4, -1)
        self.horizontalLayout_109.setObjectName("horizontalLayout_109")
        self.boton_editar_usuario = QtWidgets.QPushButton(self.menu_lateral)
        self.boton_editar_usuario.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.boton_editar_usuario.setAutoFillBackground(False)
        self.boton_editar_usuario.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"    padding: 10px;\n"
"}")
        self.boton_editar_usuario.setObjectName("boton_editar_usuario")
        self.horizontalLayout_109.addWidget(self.boton_editar_usuario)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_109.addItem(spacerItem17)
        self.verticalLayout_2.addLayout(self.horizontalLayout_109)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem18)
        self.horizontalLayout_111 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_111.setContentsMargins(0, -1, 4, -1)
        self.horizontalLayout_111.setObjectName("horizontalLayout_111")
        self.boton_meta_ventas = QtWidgets.QPushButton(self.menu_lateral)
        self.boton_meta_ventas.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.boton_meta_ventas.setAutoFillBackground(False)
        self.boton_meta_ventas.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"    padding: 10px;\n"
"}")
        self.boton_meta_ventas.setObjectName("boton_meta_ventas")
        self.horizontalLayout_111.addWidget(self.boton_meta_ventas)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_111.addItem(spacerItem19)
        self.verticalLayout_2.addLayout(self.horizontalLayout_111)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem20)
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setContentsMargins(0, -1, 4, -1)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.boton_importar_datos = QtWidgets.QPushButton(self.menu_lateral)
        self.boton_importar_datos.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.boton_importar_datos.setAutoFillBackground(False)
        self.boton_importar_datos.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"    padding: 10px;\n"
"}")
        self.boton_importar_datos.setObjectName("boton_importar_datos")
        self.horizontalLayout_40.addWidget(self.boton_importar_datos)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_40.addItem(spacerItem21)
        self.verticalLayout_2.addLayout(self.horizontalLayout_40)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem22)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem23)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(0, -1, 4, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.boton_cerrar_sesion = QtWidgets.QPushButton(self.menu_lateral)
        self.boton_cerrar_sesion.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.boton_cerrar_sesion.setAutoFillBackground(False)
        self.boton_cerrar_sesion.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"    padding: 10px;\n"
"}")
        self.boton_cerrar_sesion.setObjectName("boton_cerrar_sesion")
        self.horizontalLayout_6.addWidget(self.boton_cerrar_sesion)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem24)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout.addWidget(self.menu_lateral)
        self.frame_informacion = QtWidgets.QFrame(self.centralwidget)
        self.frame_informacion.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_informacion.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_informacion.setStyleSheet("background-color: rgb(167, 199, 243);")
        self.frame_informacion.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_informacion.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_informacion.setObjectName("frame_informacion")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_informacion)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stacked_widget_paginas = QtWidgets.QStackedWidget(self.frame_informacion)
        self.stacked_widget_paginas.setObjectName("stacked_widget_paginas")
        self.pagina_por_defecto = QtWidgets.QWidget()
        self.pagina_por_defecto.setStyleSheet("")
        self.pagina_por_defecto.setObjectName("pagina_por_defecto")
        self.horizontalLayout_66 = QtWidgets.QHBoxLayout(self.pagina_por_defecto)
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName("horizontalLayout_66")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout()
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.frame_51 = QtWidgets.QFrame(self.pagina_por_defecto)
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout(self.frame_51)
        self.verticalLayout_47.setContentsMargins(9, 15, 9, 15)
        self.verticalLayout_47.setSpacing(12)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.frame_53 = QtWidgets.QFrame(self.frame_51)
        self.frame_53.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.frame_53)
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout()
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.label = QtWidgets.QLabel(self.frame_53)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"}")
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout_48.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.label_45 = QtWidgets.QLabel(self.frame_53)
        self.label_45.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"}")
        self.label_45.setObjectName("label_45")
        self.verticalLayout_48.addWidget(self.label_45, 0, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.frame_53)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    fo    nt-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 26px;\n"
"}\n"
"")
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setLineWidth(1)
        self.label_3.setMidLineWidth(1)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setIndent(-1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_48.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.frame_52 = QtWidgets.QFrame(self.frame_53)
        self.frame_52.setMinimumSize(QtCore.QSize(0, 4))
        self.frame_52.setMaximumSize(QtCore.QSize(16777215, 5))
        self.frame_52.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;")
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.verticalLayout_48.addWidget(self.frame_52)
        self.verticalLayout_49.addLayout(self.verticalLayout_48)
        self.verticalLayout_47.addWidget(self.frame_53)
        self.label_2 = QtWidgets.QLabel(self.frame_51)
        self.label_2.setMaximumSize(QtCore.QSize(664, 380))
        self.label_2.setAcceptDrops(False)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("resources/img/imagen_inicio.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_47.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_45.addWidget(self.frame_51)
        self.horizontalLayout_66.addLayout(self.verticalLayout_45)
        self.stacked_widget_paginas.addWidget(self.pagina_por_defecto)
        self.pagina_ventas_totales_diarias = QtWidgets.QWidget()
        self.pagina_ventas_totales_diarias.setObjectName("pagina_ventas_totales_diarias")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.pagina_ventas_totales_diarias)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.pagina_ventas_totales_diarias)
        self.frame_2.setStyleSheet("")
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setMinimumSize(QtCore.QSize(0, 70))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget.setObjectName("widget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_11.setContentsMargins(-1, -1, 9, 9)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_tipo_usuario_ventas_totales_diarias = QtWidgets.QLabel(self.widget)
        self.label_tipo_usuario_ventas_totales_diarias.setMinimumSize(QtCore.QSize(0, 40))
        self.label_tipo_usuario_ventas_totales_diarias.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_tipo_usuario_ventas_totales_diarias.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"}")
        self.label_tipo_usuario_ventas_totales_diarias.setObjectName("label_tipo_usuario_ventas_totales_diarias")
        self.verticalLayout_11.addWidget(self.label_tipo_usuario_ventas_totales_diarias, 0, QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 4))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_11.addWidget(self.frame_3, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_3.addWidget(self.widget)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("QFrame {\n"
"    background-color: rgb(153, 188, 244);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.frame_10 = QtWidgets.QFrame(self.frame_4)
        self.frame_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.fecha_seleccionada_ventas_totales_diarias = QtWidgets.QDateEdit(self.frame_10)
        self.fecha_seleccionada_ventas_totales_diarias.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 12px;\n"
"color: rgb(52, 64, 85);\n"
"border: none;")
        self.fecha_seleccionada_ventas_totales_diarias.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.fecha_seleccionada_ventas_totales_diarias.setCalendarPopup(True)
        self.fecha_seleccionada_ventas_totales_diarias.setObjectName("fecha_seleccionada_ventas_totales_diarias")
        self.verticalLayout_12.addWidget(self.fecha_seleccionada_ventas_totales_diarias)
        self.horizontalLayout_19.addWidget(self.frame_10)
        self.boton_generar_ventas_totales_diarias = QtWidgets.QPushButton(self.frame_4)
        self.boton_generar_ventas_totales_diarias.setMinimumSize(QtCore.QSize(30, 40))
        self.boton_generar_ventas_totales_diarias.setMaximumSize(QtCore.QSize(140, 16777215))
        self.boton_generar_ventas_totales_diarias.setStyleSheet("QPushButton {\n"
"    background-color: rgb(65, 107, 191);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"    border-radius : 15px;\n"
"}")
        self.boton_generar_ventas_totales_diarias.setObjectName("boton_generar_ventas_totales_diarias")
        self.horizontalLayout_19.addWidget(self.boton_generar_ventas_totales_diarias)
        self.verticalLayout_6.addLayout(self.horizontalLayout_19)
        self.grafica_ventas_totales_diarias = PlotWidget(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grafica_ventas_totales_diarias.sizePolicy().hasHeightForWidth())
        self.grafica_ventas_totales_diarias.setSizePolicy(sizePolicy)
        self.grafica_ventas_totales_diarias.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.grafica_ventas_totales_diarias.setObjectName("grafica_ventas_totales_diarias")
        self.verticalLayout_6.addWidget(self.grafica_ventas_totales_diarias)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 18px;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.label_porcentaje_ventas_totales_diarias = QtWidgets.QLabel(self.frame_5)
        self.label_porcentaje_ventas_totales_diarias.setStyleSheet("QLabel {\n"
"    color: #000000;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}")
        self.label_porcentaje_ventas_totales_diarias.setObjectName("label_porcentaje_ventas_totales_diarias")
        self.verticalLayout_7.addWidget(self.label_porcentaje_ventas_totales_diarias)
        self.horizontalLayout_10.addLayout(self.verticalLayout_7)
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("resources/img/icono_estadistica.png"))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        self.label_10.setMaximumSize(QtCore.QSize(64, 16777215))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("resources/img/icono_hora_mas_ventas.png"))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_13.addWidget(self.label_10)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        self.label_8.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.label_hora_mas_ventas_totales_diarias = QtWidgets.QLabel(self.frame_6)
        self.label_hora_mas_ventas_totales_diarias.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"}")
        self.label_hora_mas_ventas_totales_diarias.setObjectName("label_hora_mas_ventas_totales_diarias")
        self.verticalLayout_8.addWidget(self.label_hora_mas_ventas_totales_diarias)
        self.horizontalLayout_13.addLayout(self.verticalLayout_8)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_11 = QtWidgets.QLabel(self.frame_7)
        self.label_11.setMaximumSize(QtCore.QSize(64, 16777215))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("resources/img/icono_hora_menos_ventas.png"))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_15.addWidget(self.label_11)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.frame_7)
        self.label_12.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"}")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_9.addWidget(self.label_12)
        self.label_hora_menos_ventas_totales_diarias = QtWidgets.QLabel(self.frame_7)
        self.label_hora_menos_ventas_totales_diarias.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"}")
        self.label_hora_menos_ventas_totales_diarias.setObjectName("label_hora_menos_ventas_totales_diarias")
        self.verticalLayout_9.addWidget(self.label_hora_menos_ventas_totales_diarias)
        self.horizontalLayout_15.addLayout(self.verticalLayout_9)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.pagina_ventas_totales_diarias)
        self.frame.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: #99bcf4;\n"
"    border-radius: 15px;\n"
"}")
        self.frame.setObjectName("frame")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_14.setWordWrap(False)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_10.addWidget(self.label_14, 0, QtCore.Qt.AlignHCenter)
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_10.addWidget(self.label_17, 0, QtCore.Qt.AlignHCenter)
        self.label_dia_ventas_totales_diarias = QtWidgets.QLabel(self.frame)
        self.label_dia_ventas_totales_diarias.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_dia_ventas_totales_diarias.setWordWrap(True)
        self.label_dia_ventas_totales_diarias.setObjectName("label_dia_ventas_totales_diarias")
        self.verticalLayout_10.addWidget(self.label_dia_ventas_totales_diarias, 0, QtCore.Qt.AlignHCenter)
        self.frame_87 = QtWidgets.QFrame(self.frame)
        self.frame_87.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_87.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_87.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_87.setObjectName("frame_87")
        self.verticalLayout_84 = QtWidgets.QVBoxLayout(self.frame_87)
        self.verticalLayout_84.setObjectName("verticalLayout_84")
        self.tabla_ventas_totales_diarias = QtWidgets.QTableWidget(self.frame_87)
        self.tabla_ventas_totales_diarias.setMinimumSize(QtCore.QSize(0, 500))
        self.tabla_ventas_totales_diarias.setMaximumSize(QtCore.QSize(600, 16777215))
        self.tabla_ventas_totales_diarias.setAutoFillBackground(True)
        self.tabla_ventas_totales_diarias.setStyleSheet("QTableWidget::item {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-bottom: 1px solid #C8D0DB;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.tabla_ventas_totales_diarias.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_ventas_totales_diarias.setProperty("showDropIndicator", False)
        self.tabla_ventas_totales_diarias.setDragDropOverwriteMode(False)
        self.tabla_ventas_totales_diarias.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tabla_ventas_totales_diarias.setShowGrid(False)
        self.tabla_ventas_totales_diarias.setGridStyle(QtCore.Qt.SolidLine)
        self.tabla_ventas_totales_diarias.setCornerButtonEnabled(False)
        self.tabla_ventas_totales_diarias.setObjectName("tabla_ventas_totales_diarias")
        self.tabla_ventas_totales_diarias.setColumnCount(2)
        self.tabla_ventas_totales_diarias.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_totales_diarias.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_totales_diarias.setHorizontalHeaderItem(1, item)
        self.tabla_ventas_totales_diarias.horizontalHeader().setCascadingSectionResizes(True)
        self.tabla_ventas_totales_diarias.horizontalHeader().setDefaultSectionSize(200)
        self.tabla_ventas_totales_diarias.horizontalHeader().setStretchLastSection(True)
        self.tabla_ventas_totales_diarias.verticalHeader().setVisible(False)
        self.tabla_ventas_totales_diarias.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_84.addWidget(self.tabla_ventas_totales_diarias)
        self.verticalLayout_10.addWidget(self.frame_87)
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_15 = QtWidgets.QLabel(self.frame_9)
        self.label_15.setStyleSheet("QLabel {\n"
"    color: #344050;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"}")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_17.addWidget(self.label_15)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem25)
        self.label_total_ventas_totales_diarias = QtWidgets.QLabel(self.frame_9)
        self.label_total_ventas_totales_diarias.setStyleSheet("QLabel {\n"
"    color: #344050;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"}")
        self.label_total_ventas_totales_diarias.setObjectName("label_total_ventas_totales_diarias")
        self.horizontalLayout_17.addWidget(self.label_total_ventas_totales_diarias)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_17)
        self.verticalLayout_10.addWidget(self.frame_9)
        self.horizontalLayout_2.addWidget(self.frame)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_2)
        self.stacked_widget_paginas.addWidget(self.pagina_ventas_totales_diarias)
        self.pagina_ventas_totales_mensuales = QtWidgets.QWidget()
        self.pagina_ventas_totales_mensuales.setObjectName("pagina_ventas_totales_mensuales")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.pagina_ventas_totales_mensuales)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setSpacing(12)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.frame_11 = QtWidgets.QFrame(self.pagina_ventas_totales_mensuales)
        self.frame_11.setStyleSheet("")
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.widget_2 = QtWidgets.QWidget(self.frame_11)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 70))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_14.setContentsMargins(-1, -1, 9, 9)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_tipo_usuario_ventas_totales_mensuales = QtWidgets.QLabel(self.widget_2)
        self.label_tipo_usuario_ventas_totales_mensuales.setMinimumSize(QtCore.QSize(0, 40))
        self.label_tipo_usuario_ventas_totales_mensuales.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_tipo_usuario_ventas_totales_mensuales.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"}")
        self.label_tipo_usuario_ventas_totales_mensuales.setObjectName("label_tipo_usuario_ventas_totales_mensuales")
        self.verticalLayout_14.addWidget(self.label_tipo_usuario_ventas_totales_mensuales, 0, QtCore.Qt.AlignTop)
        self.frame_12 = QtWidgets.QFrame(self.widget_2)
        self.frame_12.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 4))
        self.frame_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_14.addWidget(self.frame_12, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_13.addWidget(self.widget_2)
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        self.frame_13.setStyleSheet("QFrame {\n"
"    background-color: rgb(153, 188, 244);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.frame_14 = QtWidgets.QFrame(self.frame_13)
        self.frame_14.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.combobox_ventas_totales_mensuales = QtWidgets.QComboBox(self.frame_14)
        self.combobox_ventas_totales_mensuales.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 12px;\n"
"color: rgb(52, 64, 85);\n"
"border: none;")
        self.combobox_ventas_totales_mensuales.setObjectName("combobox_ventas_totales_mensuales")
        self.verticalLayout_16.addWidget(self.combobox_ventas_totales_mensuales)
        self.horizontalLayout_21.addWidget(self.frame_14)
        self.boton_generar_ventas_totales_mensuales = QtWidgets.QPushButton(self.frame_13)
        self.boton_generar_ventas_totales_mensuales.setMinimumSize(QtCore.QSize(30, 40))
        self.boton_generar_ventas_totales_mensuales.setMaximumSize(QtCore.QSize(140, 16777215))
        self.boton_generar_ventas_totales_mensuales.setStyleSheet("QPushButton {\n"
"    background-color: rgb(65, 107, 191);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"    border-radius : 15px;\n"
"}")
        self.boton_generar_ventas_totales_mensuales.setObjectName("boton_generar_ventas_totales_mensuales")
        self.horizontalLayout_21.addWidget(self.boton_generar_ventas_totales_mensuales)
        self.verticalLayout_15.addLayout(self.horizontalLayout_21)
        self.grafica_ventas_totales_mensuales = PlotWidget(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grafica_ventas_totales_mensuales.sizePolicy().hasHeightForWidth())
        self.grafica_ventas_totales_mensuales.setSizePolicy(sizePolicy)
        self.grafica_ventas_totales_mensuales.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.grafica_ventas_totales_mensuales.setObjectName("grafica_ventas_totales_mensuales")
        self.verticalLayout_15.addWidget(self.grafica_ventas_totales_mensuales)
        self.frame_16 = QtWidgets.QFrame(self.frame_13)
        self.frame_16.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_20 = QtWidgets.QLabel(self.frame_16)
        self.label_20.setMaximumSize(QtCore.QSize(64, 16777215))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("resources/img/icono_mes_mas_ventas.png"))
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_25.addWidget(self.label_20)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_21 = QtWidgets.QLabel(self.frame_16)
        self.label_21.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"}")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_18.addWidget(self.label_21)
        self.label_mes_mas_ventas_totales_mensuales = QtWidgets.QLabel(self.frame_16)
        self.label_mes_mas_ventas_totales_mensuales.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"}")
        self.label_mes_mas_ventas_totales_mensuales.setObjectName("label_mes_mas_ventas_totales_mensuales")
        self.verticalLayout_18.addWidget(self.label_mes_mas_ventas_totales_mensuales)
        self.horizontalLayout_25.addLayout(self.verticalLayout_18)
        self.horizontalLayout_24.addLayout(self.horizontalLayout_25)
        self.verticalLayout_15.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_13)
        self.frame_17.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_22 = QtWidgets.QLabel(self.frame_17)
        self.label_22.setMaximumSize(QtCore.QSize(64, 16777215))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("resources/img/icono_mes_menos_ventas.png"))
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_27.addWidget(self.label_22)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_23 = QtWidgets.QLabel(self.frame_17)
        self.label_23.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"}")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_19.addWidget(self.label_23)
        self.label_mes_menos_ventas_totales_mensuales = QtWidgets.QLabel(self.frame_17)
        self.label_mes_menos_ventas_totales_mensuales.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"}")
        self.label_mes_menos_ventas_totales_mensuales.setObjectName("label_mes_menos_ventas_totales_mensuales")
        self.verticalLayout_19.addWidget(self.label_mes_menos_ventas_totales_mensuales)
        self.horizontalLayout_27.addLayout(self.verticalLayout_19)
        self.horizontalLayout_26.addLayout(self.horizontalLayout_27)
        self.verticalLayout_15.addWidget(self.frame_17)
        self.verticalLayout_13.addWidget(self.frame_13)
        self.horizontalLayout_20.addWidget(self.frame_11)
        self.frame_18 = QtWidgets.QFrame(self.pagina_ventas_totales_mensuales)
        self.frame_18.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_18.setStyleSheet("QFrame {\n"
"    background-color: #99bcf4;\n"
"    border-radius: 15px;\n"
"}")
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_24 = QtWidgets.QLabel(self.frame_18)
        self.label_24.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_24.setWordWrap(False)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_20.addWidget(self.label_24, 0, QtCore.Qt.AlignHCenter)
        self.label_25 = QtWidgets.QLabel(self.frame_18)
        self.label_25.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_25.setWordWrap(True)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_20.addWidget(self.label_25, 0, QtCore.Qt.AlignHCenter)
        self.label_mes_ventas_totales_mensuales = QtWidgets.QLabel(self.frame_18)
        self.label_mes_ventas_totales_mensuales.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_mes_ventas_totales_mensuales.setWordWrap(True)
        self.label_mes_ventas_totales_mensuales.setObjectName("label_mes_ventas_totales_mensuales")
        self.verticalLayout_20.addWidget(self.label_mes_ventas_totales_mensuales, 0, QtCore.Qt.AlignHCenter)
        self.frame_88 = QtWidgets.QFrame(self.frame_18)
        self.frame_88.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_88.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_88.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_88.setObjectName("frame_88")
        self.verticalLayout_85 = QtWidgets.QVBoxLayout(self.frame_88)
        self.verticalLayout_85.setObjectName("verticalLayout_85")
        self.tabla_ventas_totales_mensuales = QtWidgets.QTableWidget(self.frame_88)
        self.tabla_ventas_totales_mensuales.setMinimumSize(QtCore.QSize(0, 500))
        self.tabla_ventas_totales_mensuales.setMaximumSize(QtCore.QSize(600, 16777215))
        self.tabla_ventas_totales_mensuales.setAutoFillBackground(True)
        self.tabla_ventas_totales_mensuales.setStyleSheet("QTableWidget::item {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-bottom: 1px solid #C8D0DB;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.tabla_ventas_totales_mensuales.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_ventas_totales_mensuales.setProperty("showDropIndicator", False)
        self.tabla_ventas_totales_mensuales.setDragDropOverwriteMode(False)
        self.tabla_ventas_totales_mensuales.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tabla_ventas_totales_mensuales.setShowGrid(False)
        self.tabla_ventas_totales_mensuales.setGridStyle(QtCore.Qt.SolidLine)
        self.tabla_ventas_totales_mensuales.setCornerButtonEnabled(False)
        self.tabla_ventas_totales_mensuales.setObjectName("tabla_ventas_totales_mensuales")
        self.tabla_ventas_totales_mensuales.setColumnCount(3)
        self.tabla_ventas_totales_mensuales.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_totales_mensuales.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_totales_mensuales.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(8)
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_totales_mensuales.setHorizontalHeaderItem(2, item)
        self.tabla_ventas_totales_mensuales.horizontalHeader().setCascadingSectionResizes(True)
        self.tabla_ventas_totales_mensuales.horizontalHeader().setDefaultSectionSize(150)
        self.tabla_ventas_totales_mensuales.horizontalHeader().setStretchLastSection(True)
        self.tabla_ventas_totales_mensuales.verticalHeader().setVisible(False)
        self.tabla_ventas_totales_mensuales.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_85.addWidget(self.tabla_ventas_totales_mensuales)
        self.verticalLayout_20.addWidget(self.frame_88)
        self.frame_20 = QtWidgets.QFrame(self.frame_18)
        self.frame_20.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_26 = QtWidgets.QLabel(self.frame_20)
        self.label_26.setStyleSheet("QLabel {\n"
"    color: #344050;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"}")
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_30.addWidget(self.label_26)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem26)
        self.label_total_ventas_totales_mensuales = QtWidgets.QLabel(self.frame_20)
        self.label_total_ventas_totales_mensuales.setStyleSheet("QLabel {\n"
"    color: #344050;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"}")
        self.label_total_ventas_totales_mensuales.setObjectName("label_total_ventas_totales_mensuales")
        self.horizontalLayout_30.addWidget(self.label_total_ventas_totales_mensuales)
        self.horizontalLayout_29.addLayout(self.horizontalLayout_30)
        self.verticalLayout_20.addWidget(self.frame_20)
        self.horizontalLayout_20.addWidget(self.frame_18)
        self.horizontalLayout_31.addLayout(self.horizontalLayout_20)
        self.stacked_widget_paginas.addWidget(self.pagina_ventas_totales_mensuales)
        self.pagina_ventas_totales_anuales = QtWidgets.QWidget()
        self.pagina_ventas_totales_anuales.setObjectName("pagina_ventas_totales_anuales")
        self.horizontalLayout_60 = QtWidgets.QHBoxLayout(self.pagina_ventas_totales_anuales)
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_42.setSpacing(12)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.frame_24 = QtWidgets.QFrame(self.pagina_ventas_totales_anuales)
        self.frame_24.setStyleSheet("")
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.widget_4 = QtWidgets.QWidget(self.frame_24)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 70))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_33.setContentsMargins(-1, -1, 9, 9)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.label_tipo_usuario_ventas_totales_anuales = QtWidgets.QLabel(self.widget_4)
        self.label_tipo_usuario_ventas_totales_anuales.setMinimumSize(QtCore.QSize(0, 40))
        self.label_tipo_usuario_ventas_totales_anuales.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_tipo_usuario_ventas_totales_anuales.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"}")
        self.label_tipo_usuario_ventas_totales_anuales.setObjectName("label_tipo_usuario_ventas_totales_anuales")
        self.verticalLayout_33.addWidget(self.label_tipo_usuario_ventas_totales_anuales, 0, QtCore.Qt.AlignTop)
        self.frame_36 = QtWidgets.QFrame(self.widget_4)
        self.frame_36.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_36.setMaximumSize(QtCore.QSize(16777215, 4))
        self.frame_36.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;")
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.verticalLayout_33.addWidget(self.frame_36, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_21.addWidget(self.widget_4)
        self.frame_37 = QtWidgets.QFrame(self.frame_24)
        self.frame_37.setStyleSheet("QFrame {\n"
"    background-color: rgb(153, 188, 244);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.frame_37)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.grafica_ventas_totales_anuales = PlotWidget(self.frame_37)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grafica_ventas_totales_anuales.sizePolicy().hasHeightForWidth())
        self.grafica_ventas_totales_anuales.setSizePolicy(sizePolicy)
        self.grafica_ventas_totales_anuales.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.grafica_ventas_totales_anuales.setObjectName("grafica_ventas_totales_anuales")
        self.verticalLayout_34.addWidget(self.grafica_ventas_totales_anuales)
        self.frame_40 = QtWidgets.QFrame(self.frame_37)
        self.frame_40.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout(self.frame_40)
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.label_30 = QtWidgets.QLabel(self.frame_40)
        self.label_30.setMaximumSize(QtCore.QSize(64, 16777215))
        self.label_30.setText("")
        self.label_30.setPixmap(QtGui.QPixmap("resources/img/icono_mes_mas_ventas.png"))
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_54.addWidget(self.label_30)
        self.verticalLayout_37 = QtWidgets.QVBoxLayout()
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.label_34 = QtWidgets.QLabel(self.frame_40)
        self.label_34.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"}")
        self.label_34.setObjectName("label_34")
        self.verticalLayout_37.addWidget(self.label_34)
        self.label_anio_mas_ventas_totales_anuales = QtWidgets.QLabel(self.frame_40)
        self.label_anio_mas_ventas_totales_anuales.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"}")
        self.label_anio_mas_ventas_totales_anuales.setObjectName("label_anio_mas_ventas_totales_anuales")
        self.verticalLayout_37.addWidget(self.label_anio_mas_ventas_totales_anuales)
        self.horizontalLayout_54.addLayout(self.verticalLayout_37)
        self.horizontalLayout_53.addLayout(self.horizontalLayout_54)
        self.verticalLayout_34.addWidget(self.frame_40)
        self.frame_41 = QtWidgets.QFrame(self.frame_37)
        self.frame_41.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout(self.frame_41)
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.label_40 = QtWidgets.QLabel(self.frame_41)
        self.label_40.setMaximumSize(QtCore.QSize(64, 16777215))
        self.label_40.setText("")
        self.label_40.setPixmap(QtGui.QPixmap("resources/img/icono_mes_menos_ventas.png"))
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_56.addWidget(self.label_40)
        self.verticalLayout_38 = QtWidgets.QVBoxLayout()
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.label_41 = QtWidgets.QLabel(self.frame_41)
        self.label_41.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"}")
        self.label_41.setObjectName("label_41")
        self.verticalLayout_38.addWidget(self.label_41)
        self.label_anio_menos_ventas_totales_anuales = QtWidgets.QLabel(self.frame_41)
        self.label_anio_menos_ventas_totales_anuales.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"}")
        self.label_anio_menos_ventas_totales_anuales.setObjectName("label_anio_menos_ventas_totales_anuales")
        self.verticalLayout_38.addWidget(self.label_anio_menos_ventas_totales_anuales)
        self.horizontalLayout_56.addLayout(self.verticalLayout_38)
        self.horizontalLayout_55.addLayout(self.horizontalLayout_56)
        self.verticalLayout_34.addWidget(self.frame_41)
        self.verticalLayout_21.addWidget(self.frame_37)
        self.horizontalLayout_42.addWidget(self.frame_24)
        self.frame_42 = QtWidgets.QFrame(self.pagina_ventas_totales_anuales)
        self.frame_42.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_42.setStyleSheet("QFrame {\n"
"    background-color: #99bcf4;\n"
"    border-radius: 15px;\n"
"}")
        self.frame_42.setObjectName("frame_42")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.frame_42)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.label_42 = QtWidgets.QLabel(self.frame_42)
        self.label_42.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_42.setWordWrap(False)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_39.addWidget(self.label_42, 0, QtCore.Qt.AlignHCenter)
        self.label_43 = QtWidgets.QLabel(self.frame_42)
        self.label_43.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_43.setWordWrap(True)
        self.label_43.setObjectName("label_43")
        self.verticalLayout_39.addWidget(self.label_43, 0, QtCore.Qt.AlignHCenter)
        self.frame_89 = QtWidgets.QFrame(self.frame_42)
        self.frame_89.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_89.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_89.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_89.setObjectName("frame_89")
        self.verticalLayout_86 = QtWidgets.QVBoxLayout(self.frame_89)
        self.verticalLayout_86.setObjectName("verticalLayout_86")
        self.tabla_ventas_totales_anuales = QtWidgets.QTableWidget(self.frame_89)
        self.tabla_ventas_totales_anuales.setMinimumSize(QtCore.QSize(0, 500))
        self.tabla_ventas_totales_anuales.setMaximumSize(QtCore.QSize(600, 16777215))
        self.tabla_ventas_totales_anuales.setAutoFillBackground(True)
        self.tabla_ventas_totales_anuales.setStyleSheet("QTableWidget::item {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-bottom: 1px solid #C8D0DB;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.tabla_ventas_totales_anuales.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_ventas_totales_anuales.setProperty("showDropIndicator", False)
        self.tabla_ventas_totales_anuales.setDragDropOverwriteMode(False)
        self.tabla_ventas_totales_anuales.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tabla_ventas_totales_anuales.setShowGrid(False)
        self.tabla_ventas_totales_anuales.setGridStyle(QtCore.Qt.SolidLine)
        self.tabla_ventas_totales_anuales.setCornerButtonEnabled(False)
        self.tabla_ventas_totales_anuales.setObjectName("tabla_ventas_totales_anuales")
        self.tabla_ventas_totales_anuales.setColumnCount(3)
        self.tabla_ventas_totales_anuales.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_totales_anuales.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_totales_anuales.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(8)
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_totales_anuales.setHorizontalHeaderItem(2, item)
        self.tabla_ventas_totales_anuales.horizontalHeader().setCascadingSectionResizes(True)
        self.tabla_ventas_totales_anuales.horizontalHeader().setDefaultSectionSize(150)
        self.tabla_ventas_totales_anuales.horizontalHeader().setStretchLastSection(True)
        self.tabla_ventas_totales_anuales.verticalHeader().setVisible(False)
        self.tabla_ventas_totales_anuales.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_86.addWidget(self.tabla_ventas_totales_anuales)
        self.verticalLayout_39.addWidget(self.frame_89)
        self.frame_44 = QtWidgets.QFrame(self.frame_42)
        self.frame_44.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout(self.frame_44)
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        self.label_44 = QtWidgets.QLabel(self.frame_44)
        self.label_44.setStyleSheet("QLabel {\n"
"    color: #344050;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"}")
        self.label_44.setObjectName("label_44")
        self.horizontalLayout_59.addWidget(self.label_44)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_59.addItem(spacerItem27)
        self.label_total_ventas_totales_anuales = QtWidgets.QLabel(self.frame_44)
        self.label_total_ventas_totales_anuales.setStyleSheet("QLabel {\n"
"    color: #344050;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"}")
        self.label_total_ventas_totales_anuales.setObjectName("label_total_ventas_totales_anuales")
        self.horizontalLayout_59.addWidget(self.label_total_ventas_totales_anuales)
        self.horizontalLayout_58.addLayout(self.horizontalLayout_59)
        self.verticalLayout_39.addWidget(self.frame_44)
        self.horizontalLayout_61 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        self.frame_45 = QtWidgets.QFrame(self.frame_42)
        self.frame_45.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.frame_45)
        self.verticalLayout_43.setContentsMargins(6, -1, 6, -1)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout()
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.label_6 = QtWidgets.QLabel(self.frame_45)
        self.label_6.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 13px;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_41.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.label_fecha_en_curso_ventas_totales_anuales = QtWidgets.QLabel(self.frame_45)
        self.label_fecha_en_curso_ventas_totales_anuales.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"}")
        self.label_fecha_en_curso_ventas_totales_anuales.setObjectName("label_fecha_en_curso_ventas_totales_anuales")
        self.verticalLayout_41.addWidget(self.label_fecha_en_curso_ventas_totales_anuales, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_43.addLayout(self.verticalLayout_41)
        self.horizontalLayout_61.addWidget(self.frame_45)
        self.frame_38 = QtWidgets.QFrame(self.frame_42)
        self.frame_38.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_38.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.frame_38)
        self.verticalLayout_44.setContentsMargins(6, 9, 6, -1)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout()
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.label_47 = QtWidgets.QLabel(self.frame_38)
        self.label_47.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 13px;\n"
"}")
        self.label_47.setObjectName("label_47")
        self.verticalLayout_42.addWidget(self.label_47, 0, QtCore.Qt.AlignHCenter)
        self.label_ventas_anio_en_curso_ventas_totales_anuales = QtWidgets.QLabel(self.frame_38)
        self.label_ventas_anio_en_curso_ventas_totales_anuales.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 18px;\n"
"}")
        self.label_ventas_anio_en_curso_ventas_totales_anuales.setObjectName("label_ventas_anio_en_curso_ventas_totales_anuales")
        self.verticalLayout_42.addWidget(self.label_ventas_anio_en_curso_ventas_totales_anuales, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_44.addLayout(self.verticalLayout_42)
        self.horizontalLayout_61.addWidget(self.frame_38)
        self.verticalLayout_39.addLayout(self.horizontalLayout_61)
        self.frame_46 = QtWidgets.QFrame(self.frame_42)
        self.frame_46.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.horizontalLayout_62 = QtWidgets.QHBoxLayout(self.frame_46)
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.label_49 = QtWidgets.QLabel(self.frame_46)
        self.label_49.setStyleSheet("QLabel {\n"
"    color: #344050;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 12px;\n"
"}")
        self.label_49.setWordWrap(True)
        self.label_49.setObjectName("label_49")
        self.horizontalLayout_50.addWidget(self.label_49, 0, QtCore.Qt.AlignLeft)
        self.label_ventas_totales_anio_actual_incluido_ventas_totales_anuales = QtWidgets.QLabel(self.frame_46)
        self.label_ventas_totales_anio_actual_incluido_ventas_totales_anuales.setStyleSheet("QLabel {\n"
"    color: #344050;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 12px;\n"
"}")
        self.label_ventas_totales_anio_actual_incluido_ventas_totales_anuales.setObjectName("label_ventas_totales_anio_actual_incluido_ventas_totales_anuales")
        self.horizontalLayout_50.addWidget(self.label_ventas_totales_anio_actual_incluido_ventas_totales_anuales, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_62.addLayout(self.horizontalLayout_50)
        self.verticalLayout_39.addWidget(self.frame_46)
        self.horizontalLayout_42.addWidget(self.frame_42)
        self.horizontalLayout_60.addLayout(self.horizontalLayout_42)
        self.stacked_widget_paginas.addWidget(self.pagina_ventas_totales_anuales)
        self.pagina_ventas_individuales_diarias = QtWidgets.QWidget()
        self.pagina_ventas_individuales_diarias.setObjectName("pagina_ventas_individuales_diarias")
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout(self.pagina_ventas_individuales_diarias)
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setSpacing(12)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.frame_21 = QtWidgets.QFrame(self.pagina_ventas_individuales_diarias)
        self.frame_21.setStyleSheet("")
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.frame_21)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.widget_3 = QtWidgets.QWidget(self.frame_21)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 70))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_22.setContentsMargins(-1, -1, 9, 9)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_tipo_usuario_ventas_individuales_diarias = QtWidgets.QLabel(self.widget_3)
        self.label_tipo_usuario_ventas_individuales_diarias.setMinimumSize(QtCore.QSize(0, 40))
        self.label_tipo_usuario_ventas_individuales_diarias.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_tipo_usuario_ventas_individuales_diarias.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"}")
        self.label_tipo_usuario_ventas_individuales_diarias.setObjectName("label_tipo_usuario_ventas_individuales_diarias")
        self.verticalLayout_22.addWidget(self.label_tipo_usuario_ventas_individuales_diarias, 0, QtCore.Qt.AlignTop)
        self.frame_22 = QtWidgets.QFrame(self.widget_3)
        self.frame_22.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_22.setMaximumSize(QtCore.QSize(16777215, 4))
        self.frame_22.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_22.addWidget(self.frame_22, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_27.addWidget(self.widget_3)
        self.frame_31 = QtWidgets.QFrame(self.frame_21)
        self.frame_31.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_31)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.label_36 = QtWidgets.QLabel(self.frame_31)
        self.label_36.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    fo    nt-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 16px;\n"
"    text-align: center;\n"
"}")
        self.label_36.setWordWrap(False)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_29.addWidget(self.label_36)
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_44.setContentsMargins(0, 9, 0, 9)
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.frame_32 = QtWidgets.QFrame(self.frame_31)
        self.frame_32.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_32.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout(self.frame_32)
        self.horizontalLayout_45.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.campo_num_empleado_ventas_individuales_diarias = QtWidgets.QLineEdit(self.frame_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_num_empleado_ventas_individuales_diarias.sizePolicy().hasHeightForWidth())
        self.campo_num_empleado_ventas_individuales_diarias.setSizePolicy(sizePolicy)
        self.campo_num_empleado_ventas_individuales_diarias.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 12px;\n"
"color: rgb(52, 64, 85);\n"
"border: none;")
        self.campo_num_empleado_ventas_individuales_diarias.setClearButtonEnabled(False)
        self.campo_num_empleado_ventas_individuales_diarias.setObjectName("campo_num_empleado_ventas_individuales_diarias")
        self.horizontalLayout_45.addWidget(self.campo_num_empleado_ventas_individuales_diarias)
        self.horizontalLayout_44.addWidget(self.frame_32)
        self.boton_buscar_ventas_individuales_diarias = QtWidgets.QPushButton(self.frame_31)
        self.boton_buscar_ventas_individuales_diarias.setMinimumSize(QtCore.QSize(30, 40))
        self.boton_buscar_ventas_individuales_diarias.setMaximumSize(QtCore.QSize(90, 16777215))
        self.boton_buscar_ventas_individuales_diarias.setStyleSheet("QPushButton {\n"
"    background-color: rgb(65, 107, 191);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"    border-radius : 15px;\n"
"}")
        self.boton_buscar_ventas_individuales_diarias.setObjectName("boton_buscar_ventas_individuales_diarias")
        self.horizontalLayout_44.addWidget(self.boton_buscar_ventas_individuales_diarias)
        self.verticalLayout_29.addLayout(self.horizontalLayout_44)
        self.label_37 = QtWidgets.QLabel(self.frame_31)
        self.label_37.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    fo    nt-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 16px;\n"
"    text-align: center;\n"
"}")
        self.label_37.setWordWrap(False)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_29.addWidget(self.label_37)
        self.frame_25 = QtWidgets.QFrame(self.frame_31)
        self.frame_25.setStyleSheet("background-color: rgb(151, 189, 244);\n"
"border-radius: 15px;")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_4 = QtWidgets.QLabel(self.frame_25)
        self.label_4.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_34.addWidget(self.label_4)
        self.label_num_empleado_ventas_individuales_diarias = QtWidgets.QLabel(self.frame_25)
        self.label_num_empleado_ventas_individuales_diarias.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"}")
        self.label_num_empleado_ventas_individuales_diarias.setObjectName("label_num_empleado_ventas_individuales_diarias")
        self.horizontalLayout_34.addWidget(self.label_num_empleado_ventas_individuales_diarias)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem28)
        self.verticalLayout_25.addLayout(self.horizontalLayout_34)
        self.verticalLayout_26.addLayout(self.verticalLayout_25)
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label_27 = QtWidgets.QLabel(self.frame_25)
        self.label_27.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"}")
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_36.addWidget(self.label_27)
        self.label_nombre_ventas_individuales_diarias = QtWidgets.QLabel(self.frame_25)
        self.label_nombre_ventas_individuales_diarias.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"}")
        self.label_nombre_ventas_individuales_diarias.setObjectName("label_nombre_ventas_individuales_diarias")
        self.horizontalLayout_36.addWidget(self.label_nombre_ventas_individuales_diarias)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem29)
        self.verticalLayout_26.addLayout(self.horizontalLayout_36)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_9 = QtWidgets.QLabel(self.frame_25)
        self.label_9.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_35.addWidget(self.label_9)
        self.label_estatus_ventas_individuales_diarias = QtWidgets.QLabel(self.frame_25)
        self.label_estatus_ventas_individuales_diarias.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"}")
        self.label_estatus_ventas_individuales_diarias.setObjectName("label_estatus_ventas_individuales_diarias")
        self.horizontalLayout_35.addWidget(self.label_estatus_ventas_individuales_diarias)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem30)
        self.verticalLayout_26.addLayout(self.horizontalLayout_35)
        self.verticalLayout_29.addWidget(self.frame_25)
        self.frame_26 = QtWidgets.QFrame(self.frame_31)
        self.frame_26.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_26.setMaximumSize(QtCore.QSize(16777215, 4))
        self.frame_26.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_29.addWidget(self.frame_26)
        self.verticalLayout_27.addWidget(self.frame_31)
        self.frame_23 = QtWidgets.QFrame(self.frame_21)
        self.frame_23.setStyleSheet("QFrame {\n"
"    background-color: rgb(153, 188, 244);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.frame_33 = QtWidgets.QFrame(self.frame_23)
        self.frame_33.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_23.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.fecha_seleccionada_ventas_individuales_diarias = QtWidgets.QDateEdit(self.frame_33)
        self.fecha_seleccionada_ventas_individuales_diarias.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 12px;\n"
"color: rgb(52, 64, 85);\n"
"border: none;")
        self.fecha_seleccionada_ventas_individuales_diarias.setWrapping(False)
        self.fecha_seleccionada_ventas_individuales_diarias.setFrame(True)
        self.fecha_seleccionada_ventas_individuales_diarias.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.fecha_seleccionada_ventas_individuales_diarias.setAccelerated(False)
        self.fecha_seleccionada_ventas_individuales_diarias.setProperty("showGroupSeparator", False)
        self.fecha_seleccionada_ventas_individuales_diarias.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.fecha_seleccionada_ventas_individuales_diarias.setCalendarPopup(True)
        self.fecha_seleccionada_ventas_individuales_diarias.setCurrentSectionIndex(0)
        self.fecha_seleccionada_ventas_individuales_diarias.setObjectName("fecha_seleccionada_ventas_individuales_diarias")
        self.verticalLayout_23.addWidget(self.fecha_seleccionada_ventas_individuales_diarias)
        self.horizontalLayout_33.addWidget(self.frame_33)
        self.boton_generar_ventas_individuales_diarias = QtWidgets.QPushButton(self.frame_23)
        self.boton_generar_ventas_individuales_diarias.setMinimumSize(QtCore.QSize(30, 40))
        self.boton_generar_ventas_individuales_diarias.setMaximumSize(QtCore.QSize(140, 16777215))
        self.boton_generar_ventas_individuales_diarias.setStyleSheet("QPushButton {\n"
"    background-color: rgb(65, 107, 191);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"    border-radius : 15px;\n"
"}")
        self.boton_generar_ventas_individuales_diarias.setObjectName("boton_generar_ventas_individuales_diarias")
        self.horizontalLayout_33.addWidget(self.boton_generar_ventas_individuales_diarias)
        self.verticalLayout_30.addLayout(self.horizontalLayout_33)
        self.grafica_ventas_individuales_diarias = PlotWidget(self.frame_23)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grafica_ventas_individuales_diarias.sizePolicy().hasHeightForWidth())
        self.grafica_ventas_individuales_diarias.setSizePolicy(sizePolicy)
        self.grafica_ventas_individuales_diarias.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.grafica_ventas_individuales_diarias.setObjectName("grafica_ventas_individuales_diarias")
        self.verticalLayout_30.addWidget(self.grafica_ventas_individuales_diarias)
        self.verticalLayout_27.addWidget(self.frame_23)
        self.frame_27 = QtWidgets.QFrame(self.frame_21)
        self.frame_27.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_27.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.frame_27)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.label_31 = QtWidgets.QLabel(self.frame_27)
        self.label_31.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"}")
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_39.addWidget(self.label_31)
        self.label_porcentaje_ventas_individuales_diarias = QtWidgets.QLabel(self.frame_27)
        self.label_porcentaje_ventas_individuales_diarias.setStyleSheet("QLabel {\n"
"    color: #000000;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"}")
        self.label_porcentaje_ventas_individuales_diarias.setObjectName("label_porcentaje_ventas_individuales_diarias")
        self.horizontalLayout_39.addWidget(self.label_porcentaje_ventas_individuales_diarias)
        self.horizontalLayout_38.addLayout(self.horizontalLayout_39)
        self.label_32 = QtWidgets.QLabel(self.frame_27)
        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap("resources/img/icono_estadistica.png"))
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_38.addWidget(self.label_32, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_37.addLayout(self.horizontalLayout_38)
        self.verticalLayout_27.addWidget(self.frame_27)
        self.horizontalLayout_32.addWidget(self.frame_21)
        self.frame_28 = QtWidgets.QFrame(self.pagina_ventas_individuales_diarias)
        self.frame_28.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_28.setStyleSheet("QFrame {\n"
"    background-color: #99bcf4;\n"
"    border-radius: 15px;\n"
"}")
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_28)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.label_33 = QtWidgets.QLabel(self.frame_28)
        self.label_33.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_33.setWordWrap(False)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_46.addWidget(self.label_33, 0, QtCore.Qt.AlignHCenter)
        self.label_dia_ventas_individuales_diarias = QtWidgets.QLabel(self.frame_28)
        self.label_dia_ventas_individuales_diarias.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_dia_ventas_individuales_diarias.setObjectName("label_dia_ventas_individuales_diarias")
        self.horizontalLayout_46.addWidget(self.label_dia_ventas_individuales_diarias, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_24.addLayout(self.horizontalLayout_46)
        self.frame_90 = QtWidgets.QFrame(self.frame_28)
        self.frame_90.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_90.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_90.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_90.setObjectName("frame_90")
        self.verticalLayout_87 = QtWidgets.QVBoxLayout(self.frame_90)
        self.verticalLayout_87.setObjectName("verticalLayout_87")
        self.tabla_ventas_individuales_diarias = QtWidgets.QTableWidget(self.frame_90)
        self.tabla_ventas_individuales_diarias.setMinimumSize(QtCore.QSize(0, 500))
        self.tabla_ventas_individuales_diarias.setMaximumSize(QtCore.QSize(600, 16777215))
        self.tabla_ventas_individuales_diarias.setAutoFillBackground(True)
        self.tabla_ventas_individuales_diarias.setStyleSheet("QTableWidget::item {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-bottom: 1px solid #C8D0DB;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.tabla_ventas_individuales_diarias.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_ventas_individuales_diarias.setProperty("showDropIndicator", False)
        self.tabla_ventas_individuales_diarias.setDragDropOverwriteMode(False)
        self.tabla_ventas_individuales_diarias.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tabla_ventas_individuales_diarias.setShowGrid(False)
        self.tabla_ventas_individuales_diarias.setGridStyle(QtCore.Qt.SolidLine)
        self.tabla_ventas_individuales_diarias.setCornerButtonEnabled(False)
        self.tabla_ventas_individuales_diarias.setObjectName("tabla_ventas_individuales_diarias")
        self.tabla_ventas_individuales_diarias.setColumnCount(2)
        self.tabla_ventas_individuales_diarias.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_individuales_diarias.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_individuales_diarias.setHorizontalHeaderItem(1, item)
        self.tabla_ventas_individuales_diarias.horizontalHeader().setCascadingSectionResizes(True)
        self.tabla_ventas_individuales_diarias.horizontalHeader().setDefaultSectionSize(200)
        self.tabla_ventas_individuales_diarias.horizontalHeader().setMinimumSectionSize(200)
        self.tabla_ventas_individuales_diarias.horizontalHeader().setStretchLastSection(True)
        self.tabla_ventas_individuales_diarias.verticalHeader().setVisible(False)
        self.tabla_ventas_individuales_diarias.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_87.addWidget(self.tabla_ventas_individuales_diarias)
        self.verticalLayout_24.addWidget(self.frame_90)
        self.frame_34 = QtWidgets.QFrame(self.frame_28)
        self.frame_34.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout(self.frame_34)
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.label_38 = QtWidgets.QLabel(self.frame_34)
        self.label_38.setStyleSheet("QLabel {\n"
"    color: #344050;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"}")
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_49.addWidget(self.label_38)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_49.addItem(spacerItem31)
        self.label_total_ventas_individuales_diarias = QtWidgets.QLabel(self.frame_34)
        self.label_total_ventas_individuales_diarias.setStyleSheet("QLabel {\n"
"    color: #344050;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"}")
        self.label_total_ventas_individuales_diarias.setObjectName("label_total_ventas_individuales_diarias")
        self.horizontalLayout_49.addWidget(self.label_total_ventas_individuales_diarias)
        self.horizontalLayout_48.addLayout(self.horizontalLayout_49)
        self.verticalLayout_24.addWidget(self.frame_34)
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.frame_30 = QtWidgets.QFrame(self.frame_28)
        self.frame_30.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.frame_30)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label_35 = QtWidgets.QLabel(self.frame_30)
        self.label_35.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"}")
        self.label_35.setObjectName("label_35")
        self.verticalLayout_28.addWidget(self.label_35, 0, QtCore.Qt.AlignHCenter)
        self.label_hora_mas_ventas_individuales_diarias = QtWidgets.QLabel(self.frame_30)
        self.label_hora_mas_ventas_individuales_diarias.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"}")
        self.label_hora_mas_ventas_individuales_diarias.setObjectName("label_hora_mas_ventas_individuales_diarias")
        self.verticalLayout_28.addWidget(self.label_hora_mas_ventas_individuales_diarias, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_41.addLayout(self.verticalLayout_28)
        self.horizontalLayout_47.addWidget(self.frame_30)
        self.frame_35 = QtWidgets.QFrame(self.frame_28)
        self.frame_35.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_35)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.label_39 = QtWidgets.QLabel(self.frame_35)
        self.label_39.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"}")
        self.label_39.setObjectName("label_39")
        self.verticalLayout_31.addWidget(self.label_39, 0, QtCore.Qt.AlignHCenter)
        self.label_hora_menos_ventas_individuales_diarias = QtWidgets.QLabel(self.frame_35)
        self.label_hora_menos_ventas_individuales_diarias.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"}")
        self.label_hora_menos_ventas_individuales_diarias.setObjectName("label_hora_menos_ventas_individuales_diarias")
        self.verticalLayout_31.addWidget(self.label_hora_menos_ventas_individuales_diarias, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_32.addLayout(self.verticalLayout_31)
        self.horizontalLayout_47.addWidget(self.frame_35)
        self.verticalLayout_24.addLayout(self.horizontalLayout_47)
        self.horizontalLayout_32.addWidget(self.frame_28)
        self.horizontalLayout_43.addLayout(self.horizontalLayout_32)
        self.stacked_widget_paginas.addWidget(self.pagina_ventas_individuales_diarias)
        self.pagina_ventas_individuales_mensuales = QtWidgets.QWidget()
        self.pagina_ventas_individuales_mensuales.setObjectName("pagina_ventas_individuales_mensuales")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.pagina_ventas_individuales_mensuales)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.horizontalLayout_68 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_68.setSpacing(12)
        self.horizontalLayout_68.setObjectName("horizontalLayout_68")
        self.frame_54 = QtWidgets.QFrame(self.pagina_ventas_individuales_mensuales)
        self.frame_54.setStyleSheet("")
        self.frame_54.setObjectName("frame_54")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.frame_54)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.widget_8 = QtWidgets.QWidget(self.frame_54)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 70))
        self.widget_8.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_51.setContentsMargins(-1, -1, 9, 9)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.label_tipo_usuario_ventas_individuales_mensuales = QtWidgets.QLabel(self.widget_8)
        self.label_tipo_usuario_ventas_individuales_mensuales.setMinimumSize(QtCore.QSize(0, 40))
        self.label_tipo_usuario_ventas_individuales_mensuales.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_tipo_usuario_ventas_individuales_mensuales.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"}")
        self.label_tipo_usuario_ventas_individuales_mensuales.setObjectName("label_tipo_usuario_ventas_individuales_mensuales")
        self.verticalLayout_51.addWidget(self.label_tipo_usuario_ventas_individuales_mensuales, 0, QtCore.Qt.AlignTop)
        self.frame_55 = QtWidgets.QFrame(self.widget_8)
        self.frame_55.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_55.setMaximumSize(QtCore.QSize(16777215, 4))
        self.frame_55.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;")
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.verticalLayout_51.addWidget(self.frame_55, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_50.addWidget(self.widget_8)
        self.frame_56 = QtWidgets.QFrame(self.frame_54)
        self.frame_56.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}")
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.verticalLayout_52 = QtWidgets.QVBoxLayout(self.frame_56)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.label_46 = QtWidgets.QLabel(self.frame_56)
        self.label_46.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    fo    nt-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 16px;\n"
"    text-align: center;\n"
"}")
        self.label_46.setWordWrap(False)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_52.addWidget(self.label_46)
        self.horizontalLayout_69 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_69.setContentsMargins(0, 9, 0, 9)
        self.horizontalLayout_69.setObjectName("horizontalLayout_69")
        self.frame_57 = QtWidgets.QFrame(self.frame_56)
        self.frame_57.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_57.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.horizontalLayout_70 = QtWidgets.QHBoxLayout(self.frame_57)
        self.horizontalLayout_70.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_70.setObjectName("horizontalLayout_70")
        self.campo_num_empleado_ventas_individuales_diarias_2 = QtWidgets.QLineEdit(self.frame_57)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_num_empleado_ventas_individuales_diarias_2.sizePolicy().hasHeightForWidth())
        self.campo_num_empleado_ventas_individuales_diarias_2.setSizePolicy(sizePolicy)
        self.campo_num_empleado_ventas_individuales_diarias_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 12px;\n"
"color: rgb(52, 64, 85);\n"
"border: none;")
        self.campo_num_empleado_ventas_individuales_diarias_2.setClearButtonEnabled(False)
        self.campo_num_empleado_ventas_individuales_diarias_2.setObjectName("campo_num_empleado_ventas_individuales_diarias_2")
        self.horizontalLayout_70.addWidget(self.campo_num_empleado_ventas_individuales_diarias_2)
        self.horizontalLayout_69.addWidget(self.frame_57)
        self.boton_buscar_ventas_individuales_mensuales = QtWidgets.QPushButton(self.frame_56)
        self.boton_buscar_ventas_individuales_mensuales.setMinimumSize(QtCore.QSize(30, 40))
        self.boton_buscar_ventas_individuales_mensuales.setMaximumSize(QtCore.QSize(90, 16777215))
        self.boton_buscar_ventas_individuales_mensuales.setStyleSheet("QPushButton {\n"
"    background-color: rgb(65, 107, 191);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"    border-radius : 15px;\n"
"}")
        self.boton_buscar_ventas_individuales_mensuales.setObjectName("boton_buscar_ventas_individuales_mensuales")
        self.horizontalLayout_69.addWidget(self.boton_buscar_ventas_individuales_mensuales)
        self.verticalLayout_52.addLayout(self.horizontalLayout_69)
        self.label_48 = QtWidgets.QLabel(self.frame_56)
        self.label_48.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    fo    nt-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 16px;\n"
"    text-align: center;\n"
"}")
        self.label_48.setWordWrap(False)
        self.label_48.setObjectName("label_48")
        self.verticalLayout_52.addWidget(self.label_48)
        self.frame_58 = QtWidgets.QFrame(self.frame_56)
        self.frame_58.setStyleSheet("background-color: rgb(151, 189, 244);\n"
"border-radius: 15px;")
        self.frame_58.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_58.setObjectName("frame_58")
        self.verticalLayout_53 = QtWidgets.QVBoxLayout(self.frame_58)
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        self.verticalLayout_54 = QtWidgets.QVBoxLayout()
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.horizontalLayout_71 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_71.setObjectName("horizontalLayout_71")
        self.label_50 = QtWidgets.QLabel(self.frame_58)
        self.label_50.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"}")
        self.label_50.setObjectName("label_50")
        self.horizontalLayout_71.addWidget(self.label_50)
        self.label_num_empleado_ventas_individuales_diarias_2 = QtWidgets.QLabel(self.frame_58)
        self.label_num_empleado_ventas_individuales_diarias_2.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"}")
        self.label_num_empleado_ventas_individuales_diarias_2.setObjectName("label_num_empleado_ventas_individuales_diarias_2")
        self.horizontalLayout_71.addWidget(self.label_num_empleado_ventas_individuales_diarias_2)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_71.addItem(spacerItem32)
        self.verticalLayout_54.addLayout(self.horizontalLayout_71)
        self.verticalLayout_53.addLayout(self.verticalLayout_54)
        self.horizontalLayout_72 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_72.setObjectName("horizontalLayout_72")
        self.label_51 = QtWidgets.QLabel(self.frame_58)
        self.label_51.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"}")
        self.label_51.setObjectName("label_51")
        self.horizontalLayout_72.addWidget(self.label_51)
        self.label_nombre_ventas_individuales_diarias_2 = QtWidgets.QLabel(self.frame_58)
        self.label_nombre_ventas_individuales_diarias_2.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"}")
        self.label_nombre_ventas_individuales_diarias_2.setObjectName("label_nombre_ventas_individuales_diarias_2")
        self.horizontalLayout_72.addWidget(self.label_nombre_ventas_individuales_diarias_2)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_72.addItem(spacerItem33)
        self.verticalLayout_53.addLayout(self.horizontalLayout_72)
        self.horizontalLayout_73 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_73.setObjectName("horizontalLayout_73")
        self.label_52 = QtWidgets.QLabel(self.frame_58)
        self.label_52.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"}")
        self.label_52.setObjectName("label_52")
        self.horizontalLayout_73.addWidget(self.label_52)
        self.label_estatus_ventas_individuales_diarias_2 = QtWidgets.QLabel(self.frame_58)
        self.label_estatus_ventas_individuales_diarias_2.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"}")
        self.label_estatus_ventas_individuales_diarias_2.setObjectName("label_estatus_ventas_individuales_diarias_2")
        self.horizontalLayout_73.addWidget(self.label_estatus_ventas_individuales_diarias_2)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_73.addItem(spacerItem34)
        self.verticalLayout_53.addLayout(self.horizontalLayout_73)
        self.verticalLayout_52.addWidget(self.frame_58)
        self.frame_59 = QtWidgets.QFrame(self.frame_56)
        self.frame_59.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_59.setMaximumSize(QtCore.QSize(16777215, 4))
        self.frame_59.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;")
        self.frame_59.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_59.setObjectName("frame_59")
        self.verticalLayout_52.addWidget(self.frame_59)
        self.verticalLayout_50.addWidget(self.frame_56)
        self.frame_60 = QtWidgets.QFrame(self.frame_54)
        self.frame_60.setStyleSheet("QFrame {\n"
"    background-color: rgb(153, 188, 244);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_60.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_60.setObjectName("frame_60")
        self.verticalLayout_78 = QtWidgets.QVBoxLayout(self.frame_60)
        self.verticalLayout_78.setObjectName("verticalLayout_78")
        self.horizontalLayout_74 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_74.setObjectName("horizontalLayout_74")
        self.frame_19 = QtWidgets.QFrame(self.frame_60)
        self.frame_19.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_55 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_55.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.combobox_ventas_totales_mensuales_2 = QtWidgets.QComboBox(self.frame_19)
        self.combobox_ventas_totales_mensuales_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 12px;\n"
"color: rgb(52, 64, 85);\n"
"border: none;")
        self.combobox_ventas_totales_mensuales_2.setObjectName("combobox_ventas_totales_mensuales_2")
        self.verticalLayout_55.addWidget(self.combobox_ventas_totales_mensuales_2)
        self.horizontalLayout_74.addWidget(self.frame_19)
        self.boton_generar_ventas_individuales_mensuales = QtWidgets.QPushButton(self.frame_60)
        self.boton_generar_ventas_individuales_mensuales.setMinimumSize(QtCore.QSize(30, 40))
        self.boton_generar_ventas_individuales_mensuales.setMaximumSize(QtCore.QSize(140, 16777215))
        self.boton_generar_ventas_individuales_mensuales.setStyleSheet("QPushButton {\n"
"    background-color: rgb(65, 107, 191);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"    border-radius : 15px;\n"
"}")
        self.boton_generar_ventas_individuales_mensuales.setObjectName("boton_generar_ventas_individuales_mensuales")
        self.horizontalLayout_74.addWidget(self.boton_generar_ventas_individuales_mensuales)
        self.verticalLayout_78.addLayout(self.horizontalLayout_74)
        self.grafica_ventas_individuales_mensuales = PlotWidget(self.frame_60)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grafica_ventas_individuales_mensuales.sizePolicy().hasHeightForWidth())
        self.grafica_ventas_individuales_mensuales.setSizePolicy(sizePolicy)
        self.grafica_ventas_individuales_mensuales.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.grafica_ventas_individuales_mensuales.setObjectName("grafica_ventas_individuales_mensuales")
        self.verticalLayout_78.addWidget(self.grafica_ventas_individuales_mensuales)
        self.verticalLayout_50.addWidget(self.frame_60)
        self.horizontalLayout_68.addWidget(self.frame_54)
        self.frame_63 = QtWidgets.QFrame(self.pagina_ventas_individuales_mensuales)
        self.frame_63.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_63.setStyleSheet("QFrame {\n"
"    background-color: #99bcf4;\n"
"    border-radius: 15px;\n"
"}")
        self.frame_63.setObjectName("frame_63")
        self.verticalLayout_57 = QtWidgets.QVBoxLayout(self.frame_63)
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.horizontalLayout_78 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_78.setObjectName("horizontalLayout_78")
        self.label_55 = QtWidgets.QLabel(self.frame_63)
        self.label_55.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_55.setWordWrap(False)
        self.label_55.setObjectName("label_55")
        self.horizontalLayout_78.addWidget(self.label_55, 0, QtCore.Qt.AlignHCenter)
        self.label_mes_ventas_individuales_mensuales = QtWidgets.QLabel(self.frame_63)
        self.label_mes_ventas_individuales_mensuales.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_mes_ventas_individuales_mensuales.setObjectName("label_mes_ventas_individuales_mensuales")
        self.horizontalLayout_78.addWidget(self.label_mes_ventas_individuales_mensuales, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_57.addLayout(self.horizontalLayout_78)
        self.frame_91 = QtWidgets.QFrame(self.frame_63)
        self.frame_91.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_91.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_91.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_91.setObjectName("frame_91")
        self.verticalLayout_88 = QtWidgets.QVBoxLayout(self.frame_91)
        self.verticalLayout_88.setObjectName("verticalLayout_88")
        self.tabla_ventas_individuales_mensuales = QtWidgets.QTableWidget(self.frame_91)
        self.tabla_ventas_individuales_mensuales.setMinimumSize(QtCore.QSize(0, 500))
        self.tabla_ventas_individuales_mensuales.setMaximumSize(QtCore.QSize(600, 16777215))
        self.tabla_ventas_individuales_mensuales.setAutoFillBackground(True)
        self.tabla_ventas_individuales_mensuales.setStyleSheet("QTableWidget::item {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-bottom: 1px solid #C8D0DB;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.tabla_ventas_individuales_mensuales.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_ventas_individuales_mensuales.setProperty("showDropIndicator", False)
        self.tabla_ventas_individuales_mensuales.setDragDropOverwriteMode(False)
        self.tabla_ventas_individuales_mensuales.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tabla_ventas_individuales_mensuales.setShowGrid(False)
        self.tabla_ventas_individuales_mensuales.setGridStyle(QtCore.Qt.SolidLine)
        self.tabla_ventas_individuales_mensuales.setCornerButtonEnabled(False)
        self.tabla_ventas_individuales_mensuales.setObjectName("tabla_ventas_individuales_mensuales")
        self.tabla_ventas_individuales_mensuales.setColumnCount(3)
        self.tabla_ventas_individuales_mensuales.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_individuales_mensuales.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_individuales_mensuales.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(8)
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_individuales_mensuales.setHorizontalHeaderItem(2, item)
        self.tabla_ventas_individuales_mensuales.horizontalHeader().setCascadingSectionResizes(True)
        self.tabla_ventas_individuales_mensuales.horizontalHeader().setDefaultSectionSize(150)
        self.tabla_ventas_individuales_mensuales.horizontalHeader().setStretchLastSection(True)
        self.tabla_ventas_individuales_mensuales.verticalHeader().setVisible(False)
        self.tabla_ventas_individuales_mensuales.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_88.addWidget(self.tabla_ventas_individuales_mensuales)
        self.verticalLayout_57.addWidget(self.frame_91)
        self.frame_65 = QtWidgets.QFrame(self.frame_63)
        self.frame_65.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_65.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_65.setObjectName("frame_65")
        self.horizontalLayout_80 = QtWidgets.QHBoxLayout(self.frame_65)
        self.horizontalLayout_80.setObjectName("horizontalLayout_80")
        self.horizontalLayout_81 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_81.setObjectName("horizontalLayout_81")
        self.label_56 = QtWidgets.QLabel(self.frame_65)
        self.label_56.setStyleSheet("QLabel {\n"
"    color: #344050;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"}")
        self.label_56.setObjectName("label_56")
        self.horizontalLayout_81.addWidget(self.label_56)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_81.addItem(spacerItem35)
        self.label_total_ventas_individuales_diarias_2 = QtWidgets.QLabel(self.frame_65)
        self.label_total_ventas_individuales_diarias_2.setStyleSheet("QLabel {\n"
"    color: #344050;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"}")
        self.label_total_ventas_individuales_diarias_2.setObjectName("label_total_ventas_individuales_diarias_2")
        self.horizontalLayout_81.addWidget(self.label_total_ventas_individuales_diarias_2)
        self.horizontalLayout_80.addLayout(self.horizontalLayout_81)
        self.verticalLayout_57.addWidget(self.frame_65)
        self.horizontalLayout_82 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_82.setObjectName("horizontalLayout_82")
        self.verticalLayout_57.addLayout(self.horizontalLayout_82)
        self.frame_67 = QtWidgets.QFrame(self.frame_63)
        self.frame_67.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_67.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_67.setObjectName("frame_67")
        self.horizontalLayout_100 = QtWidgets.QHBoxLayout(self.frame_67)
        self.horizontalLayout_100.setObjectName("horizontalLayout_100")
        self.label_71 = QtWidgets.QLabel(self.frame_67)
        self.label_71.setMaximumSize(QtCore.QSize(64, 16777215))
        self.label_71.setText("")
        self.label_71.setPixmap(QtGui.QPixmap("resources/img/icono_mes_mas_ventas.png"))
        self.label_71.setObjectName("label_71")
        self.horizontalLayout_100.addWidget(self.label_71)
        self.frame_66 = QtWidgets.QFrame(self.frame_67)
        self.frame_66.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_66.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_66.setObjectName("frame_66")
        self.horizontalLayout_83 = QtWidgets.QHBoxLayout(self.frame_66)
        self.horizontalLayout_83.setObjectName("horizontalLayout_83")
        self.verticalLayout_59 = QtWidgets.QVBoxLayout()
        self.verticalLayout_59.setObjectName("verticalLayout_59")
        self.label_58 = QtWidgets.QLabel(self.frame_66)
        self.label_58.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"}")
        self.label_58.setObjectName("label_58")
        self.verticalLayout_59.addWidget(self.label_58)
        self.label_hora_mas_ventas_individuales_diarias_4 = QtWidgets.QLabel(self.frame_66)
        self.label_hora_mas_ventas_individuales_diarias_4.setMinimumSize(QtCore.QSize(0, 37))
        self.label_hora_mas_ventas_individuales_diarias_4.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"}")
        self.label_hora_mas_ventas_individuales_diarias_4.setObjectName("label_hora_mas_ventas_individuales_diarias_4")
        self.verticalLayout_59.addWidget(self.label_hora_mas_ventas_individuales_diarias_4)
        self.horizontalLayout_83.addLayout(self.verticalLayout_59)
        self.label_72 = QtWidgets.QLabel(self.frame_66)
        self.label_72.setMaximumSize(QtCore.QSize(64, 16777215))
        self.label_72.setText("")
        self.label_72.setPixmap(QtGui.QPixmap("resources/img/icono_mes_menos_ventas.png"))
        self.label_72.setObjectName("label_72")
        self.horizontalLayout_83.addWidget(self.label_72)
        self.verticalLayout_58 = QtWidgets.QVBoxLayout()
        self.verticalLayout_58.setObjectName("verticalLayout_58")
        self.label_57 = QtWidgets.QLabel(self.frame_66)
        self.label_57.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"}")
        self.label_57.setObjectName("label_57")
        self.verticalLayout_58.addWidget(self.label_57)
        self.label_hora_mas_ventas_individuales_diarias_2 = QtWidgets.QLabel(self.frame_66)
        self.label_hora_mas_ventas_individuales_diarias_2.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"}")
        self.label_hora_mas_ventas_individuales_diarias_2.setObjectName("label_hora_mas_ventas_individuales_diarias_2")
        self.verticalLayout_58.addWidget(self.label_hora_mas_ventas_individuales_diarias_2)
        self.horizontalLayout_83.addLayout(self.verticalLayout_58)
        self.horizontalLayout_100.addWidget(self.frame_66)
        self.verticalLayout_57.addWidget(self.frame_67)
        self.horizontalLayout_68.addWidget(self.frame_63)
        self.horizontalLayout_28.addLayout(self.horizontalLayout_68)
        self.stacked_widget_paginas.addWidget(self.pagina_ventas_individuales_mensuales)
        self.pagina_ventas_individuales_anuales = QtWidgets.QWidget()
        self.pagina_ventas_individuales_anuales.setObjectName("pagina_ventas_individuales_anuales")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.pagina_ventas_individuales_anuales)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_84 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_84.setSpacing(12)
        self.horizontalLayout_84.setObjectName("horizontalLayout_84")
        self.frame_68 = QtWidgets.QFrame(self.pagina_ventas_individuales_anuales)
        self.frame_68.setStyleSheet("")
        self.frame_68.setObjectName("frame_68")
        self.verticalLayout_60 = QtWidgets.QVBoxLayout(self.frame_68)
        self.verticalLayout_60.setObjectName("verticalLayout_60")
        self.widget_9 = QtWidgets.QWidget(self.frame_68)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 70))
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_61 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_61.setContentsMargins(-1, -1, 9, 9)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName("verticalLayout_61")
        self.label_tipo_usuario_ventas_individuales_anuales = QtWidgets.QLabel(self.widget_9)
        self.label_tipo_usuario_ventas_individuales_anuales.setMinimumSize(QtCore.QSize(0, 40))
        self.label_tipo_usuario_ventas_individuales_anuales.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_tipo_usuario_ventas_individuales_anuales.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"}")
        self.label_tipo_usuario_ventas_individuales_anuales.setObjectName("label_tipo_usuario_ventas_individuales_anuales")
        self.verticalLayout_61.addWidget(self.label_tipo_usuario_ventas_individuales_anuales, 0, QtCore.Qt.AlignTop)
        self.frame_69 = QtWidgets.QFrame(self.widget_9)
        self.frame_69.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_69.setMaximumSize(QtCore.QSize(16777215, 4))
        self.frame_69.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;")
        self.frame_69.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_69.setObjectName("frame_69")
        self.verticalLayout_61.addWidget(self.frame_69, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_60.addWidget(self.widget_9)
        self.frame_70 = QtWidgets.QFrame(self.frame_68)
        self.frame_70.setStyleSheet("QFrame {\n"
"    border: none;\n"
"}")
        self.frame_70.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_70.setObjectName("frame_70")
        self.verticalLayout_62 = QtWidgets.QVBoxLayout(self.frame_70)
        self.verticalLayout_62.setObjectName("verticalLayout_62")
        self.label_59 = QtWidgets.QLabel(self.frame_70)
        self.label_59.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    fo    nt-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 16px;\n"
"    text-align: center;\n"
"}")
        self.label_59.setWordWrap(False)
        self.label_59.setObjectName("label_59")
        self.verticalLayout_62.addWidget(self.label_59)
        self.horizontalLayout_85 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_85.setContentsMargins(0, 9, 0, 9)
        self.horizontalLayout_85.setObjectName("horizontalLayout_85")
        self.frame_71 = QtWidgets.QFrame(self.frame_70)
        self.frame_71.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_71.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_71.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_71.setObjectName("frame_71")
        self.horizontalLayout_86 = QtWidgets.QHBoxLayout(self.frame_71)
        self.horizontalLayout_86.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_86.setObjectName("horizontalLayout_86")
        self.campo_num_empleado_ventas_individuales_anuales = QtWidgets.QLineEdit(self.frame_71)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_num_empleado_ventas_individuales_anuales.sizePolicy().hasHeightForWidth())
        self.campo_num_empleado_ventas_individuales_anuales.setSizePolicy(sizePolicy)
        self.campo_num_empleado_ventas_individuales_anuales.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 12px;\n"
"color: rgb(52, 64, 85);\n"
"border: none;")
        self.campo_num_empleado_ventas_individuales_anuales.setClearButtonEnabled(False)
        self.campo_num_empleado_ventas_individuales_anuales.setObjectName("campo_num_empleado_ventas_individuales_anuales")
        self.horizontalLayout_86.addWidget(self.campo_num_empleado_ventas_individuales_anuales)
        self.horizontalLayout_85.addWidget(self.frame_71)
        self.boton_buscar_ventas_individuales_anuales = QtWidgets.QPushButton(self.frame_70)
        self.boton_buscar_ventas_individuales_anuales.setMinimumSize(QtCore.QSize(30, 40))
        self.boton_buscar_ventas_individuales_anuales.setMaximumSize(QtCore.QSize(90, 16777215))
        self.boton_buscar_ventas_individuales_anuales.setStyleSheet("QPushButton {\n"
"    background-color: rgb(65, 107, 191);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"    border-radius : 15px;\n"
"}")
        self.boton_buscar_ventas_individuales_anuales.setObjectName("boton_buscar_ventas_individuales_anuales")
        self.horizontalLayout_85.addWidget(self.boton_buscar_ventas_individuales_anuales)
        self.verticalLayout_62.addLayout(self.horizontalLayout_85)
        self.label_60 = QtWidgets.QLabel(self.frame_70)
        self.label_60.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    fo    nt-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 16px;\n"
"    text-align: center;\n"
"}")
        self.label_60.setWordWrap(False)
        self.label_60.setObjectName("label_60")
        self.verticalLayout_62.addWidget(self.label_60)
        self.frame_72 = QtWidgets.QFrame(self.frame_70)
        self.frame_72.setStyleSheet("background-color: rgb(151, 189, 244);\n"
"border-radius: 15px;")
        self.frame_72.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_72.setObjectName("frame_72")
        self.verticalLayout_63 = QtWidgets.QVBoxLayout(self.frame_72)
        self.verticalLayout_63.setObjectName("verticalLayout_63")
        self.verticalLayout_64 = QtWidgets.QVBoxLayout()
        self.verticalLayout_64.setObjectName("verticalLayout_64")
        self.horizontalLayout_87 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_87.setObjectName("horizontalLayout_87")
        self.label_61 = QtWidgets.QLabel(self.frame_72)
        self.label_61.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"}")
        self.label_61.setObjectName("label_61")
        self.horizontalLayout_87.addWidget(self.label_61)
        self.label_num_empleado_ventas_individuales_anuales = QtWidgets.QLabel(self.frame_72)
        self.label_num_empleado_ventas_individuales_anuales.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"}")
        self.label_num_empleado_ventas_individuales_anuales.setObjectName("label_num_empleado_ventas_individuales_anuales")
        self.horizontalLayout_87.addWidget(self.label_num_empleado_ventas_individuales_anuales)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_87.addItem(spacerItem36)
        self.verticalLayout_64.addLayout(self.horizontalLayout_87)
        self.verticalLayout_63.addLayout(self.verticalLayout_64)
        self.horizontalLayout_88 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_88.setObjectName("horizontalLayout_88")
        self.label_62 = QtWidgets.QLabel(self.frame_72)
        self.label_62.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"}")
        self.label_62.setObjectName("label_62")
        self.horizontalLayout_88.addWidget(self.label_62)
        self.label_nombre_ventas_individuales_anuales = QtWidgets.QLabel(self.frame_72)
        self.label_nombre_ventas_individuales_anuales.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"}")
        self.label_nombre_ventas_individuales_anuales.setObjectName("label_nombre_ventas_individuales_anuales")
        self.horizontalLayout_88.addWidget(self.label_nombre_ventas_individuales_anuales)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_88.addItem(spacerItem37)
        self.verticalLayout_63.addLayout(self.horizontalLayout_88)
        self.horizontalLayout_89 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_89.setObjectName("horizontalLayout_89")
        self.label_63 = QtWidgets.QLabel(self.frame_72)
        self.label_63.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"}")
        self.label_63.setObjectName("label_63")
        self.horizontalLayout_89.addWidget(self.label_63)
        self.label_estatus_ventas_individuales_anuales = QtWidgets.QLabel(self.frame_72)
        self.label_estatus_ventas_individuales_anuales.setStyleSheet("QLabel {\n"
"    color: rgb(65, 107, 191);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"}")
        self.label_estatus_ventas_individuales_anuales.setObjectName("label_estatus_ventas_individuales_anuales")
        self.horizontalLayout_89.addWidget(self.label_estatus_ventas_individuales_anuales)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_89.addItem(spacerItem38)
        self.verticalLayout_63.addLayout(self.horizontalLayout_89)
        self.verticalLayout_62.addWidget(self.frame_72)
        self.frame_73 = QtWidgets.QFrame(self.frame_70)
        self.frame_73.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_73.setMaximumSize(QtCore.QSize(16777215, 4))
        self.frame_73.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;")
        self.frame_73.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_73.setObjectName("frame_73")
        self.verticalLayout_62.addWidget(self.frame_73)
        self.verticalLayout_60.addWidget(self.frame_70)
        self.frame_74 = QtWidgets.QFrame(self.frame_68)
        self.frame_74.setStyleSheet("QFrame {\n"
"    background-color: rgb(153, 188, 244);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_74.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_74.setObjectName("frame_74")
        self.verticalLayout_65 = QtWidgets.QVBoxLayout(self.frame_74)
        self.verticalLayout_65.setObjectName("verticalLayout_65")
        self.grafica_ventas_individuales_anuales = PlotWidget(self.frame_74)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grafica_ventas_individuales_anuales.sizePolicy().hasHeightForWidth())
        self.grafica_ventas_individuales_anuales.setSizePolicy(sizePolicy)
        self.grafica_ventas_individuales_anuales.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.grafica_ventas_individuales_anuales.setObjectName("grafica_ventas_individuales_anuales")
        self.verticalLayout_65.addWidget(self.grafica_ventas_individuales_anuales)
        self.verticalLayout_60.addWidget(self.frame_74)
        self.horizontalLayout_84.addWidget(self.frame_68)
        self.frame_77 = QtWidgets.QFrame(self.pagina_ventas_individuales_anuales)
        self.frame_77.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_77.setStyleSheet("QFrame {\n"
"    background-color: #99bcf4;\n"
"    border-radius: 15px;\n"
"}")
        self.frame_77.setObjectName("frame_77")
        self.verticalLayout_56 = QtWidgets.QVBoxLayout(self.frame_77)
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.horizontalLayout_94 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_94.setObjectName("horizontalLayout_94")
        self.label_66 = QtWidgets.QLabel(self.frame_77)
        self.label_66.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_66.setWordWrap(False)
        self.label_66.setObjectName("label_66")
        self.horizontalLayout_94.addWidget(self.label_66, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_56.addLayout(self.horizontalLayout_94)
        self.frame_92 = QtWidgets.QFrame(self.frame_77)
        self.frame_92.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_92.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_92.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_92.setObjectName("frame_92")
        self.verticalLayout_89 = QtWidgets.QVBoxLayout(self.frame_92)
        self.verticalLayout_89.setObjectName("verticalLayout_89")
        self.tabla_ventas_individuales_anuales = QtWidgets.QTableWidget(self.frame_92)
        self.tabla_ventas_individuales_anuales.setMinimumSize(QtCore.QSize(0, 500))
        self.tabla_ventas_individuales_anuales.setMaximumSize(QtCore.QSize(600, 16777215))
        self.tabla_ventas_individuales_anuales.setAutoFillBackground(True)
        self.tabla_ventas_individuales_anuales.setStyleSheet("QTableWidget::item {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-bottom: 1px solid #C8D0DB;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.tabla_ventas_individuales_anuales.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_ventas_individuales_anuales.setProperty("showDropIndicator", False)
        self.tabla_ventas_individuales_anuales.setDragDropOverwriteMode(False)
        self.tabla_ventas_individuales_anuales.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tabla_ventas_individuales_anuales.setShowGrid(False)
        self.tabla_ventas_individuales_anuales.setGridStyle(QtCore.Qt.SolidLine)
        self.tabla_ventas_individuales_anuales.setCornerButtonEnabled(False)
        self.tabla_ventas_individuales_anuales.setObjectName("tabla_ventas_individuales_anuales")
        self.tabla_ventas_individuales_anuales.setColumnCount(3)
        self.tabla_ventas_individuales_anuales.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_individuales_anuales.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_individuales_anuales.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_individuales_anuales.setHorizontalHeaderItem(2, item)
        self.tabla_ventas_individuales_anuales.horizontalHeader().setCascadingSectionResizes(True)
        self.tabla_ventas_individuales_anuales.horizontalHeader().setDefaultSectionSize(150)
        self.tabla_ventas_individuales_anuales.horizontalHeader().setStretchLastSection(True)
        self.tabla_ventas_individuales_anuales.verticalHeader().setVisible(False)
        self.tabla_ventas_individuales_anuales.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_89.addWidget(self.tabla_ventas_individuales_anuales)
        self.verticalLayout_56.addWidget(self.frame_92)
        self.frame_79 = QtWidgets.QFrame(self.frame_77)
        self.frame_79.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_79.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_79.setObjectName("frame_79")
        self.horizontalLayout_96 = QtWidgets.QHBoxLayout(self.frame_79)
        self.horizontalLayout_96.setObjectName("horizontalLayout_96")
        self.horizontalLayout_97 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_97.setObjectName("horizontalLayout_97")
        self.label_67 = QtWidgets.QLabel(self.frame_79)
        self.label_67.setStyleSheet("QLabel {\n"
"    color: #344050;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"}")
        self.label_67.setObjectName("label_67")
        self.horizontalLayout_97.addWidget(self.label_67)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_97.addItem(spacerItem39)
        self.label_total_ventas_individuales_anuales = QtWidgets.QLabel(self.frame_79)
        self.label_total_ventas_individuales_anuales.setStyleSheet("QLabel {\n"
"    color: #344050;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"}")
        self.label_total_ventas_individuales_anuales.setObjectName("label_total_ventas_individuales_anuales")
        self.horizontalLayout_97.addWidget(self.label_total_ventas_individuales_anuales)
        self.horizontalLayout_96.addLayout(self.horizontalLayout_97)
        self.verticalLayout_56.addWidget(self.frame_79)
        self.horizontalLayout_98 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_98.setObjectName("horizontalLayout_98")
        self.verticalLayout_56.addLayout(self.horizontalLayout_98)
        self.frame_80 = QtWidgets.QFrame(self.frame_77)
        self.frame_80.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_80.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_80.setObjectName("frame_80")
        self.horizontalLayout_101 = QtWidgets.QHBoxLayout(self.frame_80)
        self.horizontalLayout_101.setObjectName("horizontalLayout_101")
        self.label_73 = QtWidgets.QLabel(self.frame_80)
        self.label_73.setMaximumSize(QtCore.QSize(64, 16777215))
        self.label_73.setText("")
        self.label_73.setPixmap(QtGui.QPixmap("resources/img/icono_mes_mas_ventas.png"))
        self.label_73.setObjectName("label_73")
        self.horizontalLayout_101.addWidget(self.label_73)
        self.frame_81 = QtWidgets.QFrame(self.frame_80)
        self.frame_81.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_81.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_81.setObjectName("frame_81")
        self.horizontalLayout_99 = QtWidgets.QHBoxLayout(self.frame_81)
        self.horizontalLayout_99.setObjectName("horizontalLayout_99")
        self.verticalLayout_68 = QtWidgets.QVBoxLayout()
        self.verticalLayout_68.setObjectName("verticalLayout_68")
        self.label_68 = QtWidgets.QLabel(self.frame_81)
        self.label_68.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"}")
        self.label_68.setWordWrap(True)
        self.label_68.setObjectName("label_68")
        self.verticalLayout_68.addWidget(self.label_68, 0, QtCore.Qt.AlignHCenter)
        self.label_anio_mas_ventas_individuales_anuales = QtWidgets.QLabel(self.frame_81)
        self.label_anio_mas_ventas_individuales_anuales.setMinimumSize(QtCore.QSize(0, 37))
        self.label_anio_mas_ventas_individuales_anuales.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 18px;\n"
"}")
        self.label_anio_mas_ventas_individuales_anuales.setObjectName("label_anio_mas_ventas_individuales_anuales")
        self.verticalLayout_68.addWidget(self.label_anio_mas_ventas_individuales_anuales, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_99.addLayout(self.verticalLayout_68)
        self.label_74 = QtWidgets.QLabel(self.frame_81)
        self.label_74.setMaximumSize(QtCore.QSize(64, 16777215))
        self.label_74.setText("")
        self.label_74.setPixmap(QtGui.QPixmap("resources/img/icono_mes_menos_ventas.png"))
        self.label_74.setObjectName("label_74")
        self.horizontalLayout_99.addWidget(self.label_74)
        self.verticalLayout_69 = QtWidgets.QVBoxLayout()
        self.verticalLayout_69.setObjectName("verticalLayout_69")
        self.label_69 = QtWidgets.QLabel(self.frame_81)
        self.label_69.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"}")
        self.label_69.setWordWrap(True)
        self.label_69.setObjectName("label_69")
        self.verticalLayout_69.addWidget(self.label_69, 0, QtCore.Qt.AlignHCenter)
        self.label_anio_menos_ventas_individuales_anuales = QtWidgets.QLabel(self.frame_81)
        self.label_anio_menos_ventas_individuales_anuales.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 18px;\n"
"}")
        self.label_anio_menos_ventas_individuales_anuales.setObjectName("label_anio_menos_ventas_individuales_anuales")
        self.verticalLayout_69.addWidget(self.label_anio_menos_ventas_individuales_anuales, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_99.addLayout(self.verticalLayout_69)
        self.horizontalLayout_101.addWidget(self.frame_81)
        self.verticalLayout_56.addWidget(self.frame_80)
        self.horizontalLayout_104 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_104.setObjectName("horizontalLayout_104")
        self.frame_84 = QtWidgets.QFrame(self.frame_77)
        self.frame_84.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_84.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_84.setObjectName("frame_84")
        self.horizontalLayout_105 = QtWidgets.QHBoxLayout(self.frame_84)
        self.horizontalLayout_105.setObjectName("horizontalLayout_105")
        self.verticalLayout_73 = QtWidgets.QVBoxLayout()
        self.verticalLayout_73.setObjectName("verticalLayout_73")
        self.label_76 = QtWidgets.QLabel(self.frame_84)
        self.label_76.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"}")
        self.label_76.setObjectName("label_76")
        self.verticalLayout_73.addWidget(self.label_76, 0, QtCore.Qt.AlignHCenter)
        self.label_fecha_en_curso_ventas_individuales_anuales = QtWidgets.QLabel(self.frame_84)
        self.label_fecha_en_curso_ventas_individuales_anuales.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"}")
        self.label_fecha_en_curso_ventas_individuales_anuales.setObjectName("label_fecha_en_curso_ventas_individuales_anuales")
        self.verticalLayout_73.addWidget(self.label_fecha_en_curso_ventas_individuales_anuales, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_105.addLayout(self.verticalLayout_73)
        self.horizontalLayout_104.addWidget(self.frame_84)
        self.frame_85 = QtWidgets.QFrame(self.frame_77)
        self.frame_85.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_85.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_85.setObjectName("frame_85")
        self.verticalLayout_74 = QtWidgets.QVBoxLayout(self.frame_85)
        self.verticalLayout_74.setObjectName("verticalLayout_74")
        self.verticalLayout_75 = QtWidgets.QVBoxLayout()
        self.verticalLayout_75.setObjectName("verticalLayout_75")
        self.label_77 = QtWidgets.QLabel(self.frame_85)
        self.label_77.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"}")
        self.label_77.setObjectName("label_77")
        self.verticalLayout_75.addWidget(self.label_77, 0, QtCore.Qt.AlignHCenter)
        self.label_ventas_anio_en_curso_ventas_individuales_anuales = QtWidgets.QLabel(self.frame_85)
        self.label_ventas_anio_en_curso_ventas_individuales_anuales.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 18px;\n"
"}")
        self.label_ventas_anio_en_curso_ventas_individuales_anuales.setObjectName("label_ventas_anio_en_curso_ventas_individuales_anuales")
        self.verticalLayout_75.addWidget(self.label_ventas_anio_en_curso_ventas_individuales_anuales, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_74.addLayout(self.verticalLayout_75)
        self.horizontalLayout_104.addWidget(self.frame_85)
        self.verticalLayout_56.addLayout(self.horizontalLayout_104)
        self.frame_86 = QtWidgets.QFrame(self.frame_77)
        self.frame_86.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_86.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_86.setObjectName("frame_86")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_86)
        self.gridLayout.setObjectName("gridLayout")
        self.label_78 = QtWidgets.QLabel(self.frame_86)
        self.label_78.setStyleSheet("QLabel {\n"
"    color: #344050;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 12px;\n"
"}")
        self.label_78.setObjectName("label_78")
        self.gridLayout.addWidget(self.label_78, 0, 0, 1, 1)
        self.label_ventas_totales_anio_actual_incluido_ventas_individuales_anuales = QtWidgets.QLabel(self.frame_86)
        self.label_ventas_totales_anio_actual_incluido_ventas_individuales_anuales.setStyleSheet("QLabel {\n"
"    color: #344050;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 14px;\n"
"}")
        self.label_ventas_totales_anio_actual_incluido_ventas_individuales_anuales.setObjectName("label_ventas_totales_anio_actual_incluido_ventas_individuales_anuales")
        self.gridLayout.addWidget(self.label_ventas_totales_anio_actual_incluido_ventas_individuales_anuales, 0, 1, 1, 1, QtCore.Qt.AlignRight)
        self.verticalLayout_56.addWidget(self.frame_86)
        self.horizontalLayout_84.addWidget(self.frame_77)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_84)
        self.stacked_widget_paginas.addWidget(self.pagina_ventas_individuales_anuales)
        self.pagina_empleados = QtWidgets.QWidget()
        self.pagina_empleados.setObjectName("pagina_empleados")
        self.horizontalLayout_102 = QtWidgets.QHBoxLayout(self.pagina_empleados)
        self.horizontalLayout_102.setObjectName("horizontalLayout_102")
        self.horizontalLayout_63 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        self.frame_47 = QtWidgets.QFrame(self.pagina_empleados)
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.verticalLayout_71 = QtWidgets.QVBoxLayout(self.frame_47)
        self.verticalLayout_71.setObjectName("verticalLayout_71")
        self.widget_5 = QtWidgets.QWidget(self.frame_47)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 90))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.horizontalLayout_103 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_103.setObjectName("horizontalLayout_103")
        self.frame_82 = QtWidgets.QFrame(self.widget_5)
        self.frame_82.setStyleSheet("border: none;")
        self.frame_82.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_82.setObjectName("frame_82")
        self.verticalLayout_72 = QtWidgets.QVBoxLayout(self.frame_82)
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_72.setObjectName("verticalLayout_72")
        self.verticalLayout_70 = QtWidgets.QVBoxLayout()
        self.verticalLayout_70.setObjectName("verticalLayout_70")
        self.label_tipo_usuario_empleados = QtWidgets.QLabel(self.frame_82)
        self.label_tipo_usuario_empleados.setMinimumSize(QtCore.QSize(0, 40))
        self.label_tipo_usuario_empleados.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_tipo_usuario_empleados.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"}")
        self.label_tipo_usuario_empleados.setObjectName("label_tipo_usuario_empleados")
        self.verticalLayout_70.addWidget(self.label_tipo_usuario_empleados)
        self.frame_48 = QtWidgets.QFrame(self.frame_82)
        self.frame_48.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_48.setMaximumSize(QtCore.QSize(300, 4))
        self.frame_48.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;")
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.verticalLayout_70.addWidget(self.frame_48)
        self.verticalLayout_72.addLayout(self.verticalLayout_70)
        self.horizontalLayout_103.addWidget(self.frame_82)
        self.horizontalLayout_64 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_64.setContentsMargins(0, 9, 12, 9)
        self.horizontalLayout_64.setSpacing(15)
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")
        self.frame_49 = QtWidgets.QFrame(self.widget_5)
        self.frame_49.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_49.setMaximumSize(QtCore.QSize(250, 20))
        self.frame_49.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_49.setObjectName("frame_49")
        self.horizontalLayout_65 = QtWidgets.QHBoxLayout(self.frame_49)
        self.horizontalLayout_65.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        self.campo_nombre_empleado_empleados = QtWidgets.QLineEdit(self.frame_49)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_nombre_empleado_empleados.sizePolicy().hasHeightForWidth())
        self.campo_nombre_empleado_empleados.setSizePolicy(sizePolicy)
        self.campo_nombre_empleado_empleados.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 12px;\n"
"color: rgb(52, 64, 85);\n"
"border: none;")
        self.campo_nombre_empleado_empleados.setClearButtonEnabled(False)
        self.campo_nombre_empleado_empleados.setObjectName("campo_nombre_empleado_empleados")
        self.horizontalLayout_65.addWidget(self.campo_nombre_empleado_empleados)
        self.horizontalLayout_64.addWidget(self.frame_49, 0, QtCore.Qt.AlignVCenter)
        self.boton_buscar_empleados = QtWidgets.QPushButton(self.widget_5)
        self.boton_buscar_empleados.setMinimumSize(QtCore.QSize(30, 40))
        self.boton_buscar_empleados.setMaximumSize(QtCore.QSize(90, 16777215))
        self.boton_buscar_empleados.setStyleSheet("QPushButton {\n"
"    background-color: rgb(65, 107, 191);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"    border-radius : 15px;\n"
"}")
        self.boton_buscar_empleados.setObjectName("boton_buscar_empleados")
        self.horizontalLayout_64.addWidget(self.boton_buscar_empleados)
        self.horizontalLayout_103.addLayout(self.horizontalLayout_64)
        self.verticalLayout_35.addLayout(self.horizontalLayout_103)
        self.verticalLayout_71.addWidget(self.widget_5)
        self.frame_61 = QtWidgets.QFrame(self.frame_47)
        self.frame_61.setStyleSheet("QFrame {\n"
"    background-color: rgb(153, 188, 244);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_61.setObjectName("frame_61")
        self.verticalLayout_76 = QtWidgets.QVBoxLayout(self.frame_61)
        self.verticalLayout_76.setObjectName("verticalLayout_76")
        self.widget_7 = QtWidgets.QWidget(self.frame_61)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 70))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_7.setStyleSheet("background-color: rgb(153, 188, 244);")
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_40.setContentsMargins(25, -1, 15, 9)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.label_13 = QtWidgets.QLabel(self.widget_7)
        self.label_13.setMinimumSize(QtCore.QSize(0, 40))
        self.label_13.setMaximumSize(QtCore.QSize(400, 40))
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setStyleSheet("QLabel {\n"
"    color: rgb(0, 85, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"}")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_40.addWidget(self.label_13, 0, QtCore.Qt.AlignHCenter)
        self.frame_50 = QtWidgets.QFrame(self.widget_7)
        self.frame_50.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_50.setMaximumSize(QtCore.QSize(16777215, 4))
        self.frame_50.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"border-radius: 2px;")
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.verticalLayout_40.addWidget(self.frame_50, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_76.addWidget(self.widget_7)
        self.verticalLayout_46 = QtWidgets.QVBoxLayout()
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.horizontalLayout_67 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_67.setObjectName("horizontalLayout_67")
        self.frame_83 = QtWidgets.QFrame(self.frame_61)
        self.frame_83.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_83.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_83.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_83.setObjectName("frame_83")
        self.verticalLayout_77 = QtWidgets.QVBoxLayout(self.frame_83)
        self.verticalLayout_77.setObjectName("verticalLayout_77")
        self.tabla_empleados = QtWidgets.QTableWidget(self.frame_83)
        self.tabla_empleados.setMinimumSize(QtCore.QSize(0, 500))
        self.tabla_empleados.setMaximumSize(QtCore.QSize(600, 16777215))
        self.tabla_empleados.setAutoFillBackground(True)
        self.tabla_empleados.setStyleSheet("QTableWidget::item {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-bottom: 1px solid #C8D0DB;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.tabla_empleados.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_empleados.setProperty("showDropIndicator", False)
        self.tabla_empleados.setDragDropOverwriteMode(False)
        self.tabla_empleados.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tabla_empleados.setShowGrid(False)
        self.tabla_empleados.setGridStyle(QtCore.Qt.SolidLine)
        self.tabla_empleados.setCornerButtonEnabled(False)
        self.tabla_empleados.setObjectName("tabla_empleados")
        self.tabla_empleados.setColumnCount(4)
        self.tabla_empleados.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_empleados.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_empleados.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_empleados.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_empleados.setHorizontalHeaderItem(3, item)
        self.tabla_empleados.horizontalHeader().setCascadingSectionResizes(True)
        self.tabla_empleados.horizontalHeader().setDefaultSectionSize(150)
        self.tabla_empleados.verticalHeader().setVisible(False)
        self.tabla_empleados.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_77.addWidget(self.tabla_empleados)
        self.horizontalLayout_67.addWidget(self.frame_83)
        self.verticalLayout_46.addLayout(self.horizontalLayout_67)
        self.verticalLayout_76.addLayout(self.verticalLayout_46)
        self.verticalLayout_71.addWidget(self.frame_61)
        self.horizontalLayout_63.addWidget(self.frame_47)
        self.horizontalLayout_102.addLayout(self.horizontalLayout_63)
        self.stacked_widget_paginas.addWidget(self.pagina_empleados)
        self.pagina_importar_datos = QtWidgets.QWidget()
        self.pagina_importar_datos.setObjectName("pagina_importar_datos")
        self.verticalLayout_66 = QtWidgets.QVBoxLayout(self.pagina_importar_datos)
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_66.setObjectName("verticalLayout_66")
        self.frame_8 = QtWidgets.QFrame(self.pagina_importar_datos)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_67 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_67.setObjectName("verticalLayout_67")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_8)
        self.scrollArea.setStyleSheet("border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 1048, 910))
        self.scrollAreaWidgetContents_4.setStyleSheet("")
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_82 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_82.setSpacing(6)
        self.verticalLayout_82.setObjectName("verticalLayout_82")
        self.frame_75 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_75.setMinimumSize(QtCore.QSize(1000, 0))
        self.frame_75.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_75.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_75.setObjectName("frame_75")
        self.verticalLayout_83 = QtWidgets.QVBoxLayout(self.frame_75)
        self.verticalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_83.setObjectName("verticalLayout_83")
        self.widget_6 = QtWidgets.QWidget(self.frame_75)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 70))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_79 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_79.setObjectName("verticalLayout_79")
        self.label_tipo_usuario_importar_datos = QtWidgets.QLabel(self.widget_6)
        self.label_tipo_usuario_importar_datos.setMinimumSize(QtCore.QSize(0, 40))
        self.label_tipo_usuario_importar_datos.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_tipo_usuario_importar_datos.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"}")
        self.label_tipo_usuario_importar_datos.setObjectName("label_tipo_usuario_importar_datos")
        self.verticalLayout_79.addWidget(self.label_tipo_usuario_importar_datos)
        self.frame_29 = QtWidgets.QFrame(self.widget_6)
        self.frame_29.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_29.setMaximumSize(QtCore.QSize(300, 4))
        self.frame_29.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_79.addWidget(self.frame_29)
        self.verticalLayout_83.addWidget(self.widget_6)
        self.frame_43 = QtWidgets.QFrame(self.frame_75)
        self.frame_43.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_43.setStyleSheet("QFrame {\n"
"    background-color: rgb(153, 188, 244);\n"
"    border-radius: 15px;\n"
"    margin-left: 16px;\n"
"    margin-right: 16px;\n"
"}")
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout(self.frame_43)
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.label_70 = QtWidgets.QLabel(self.frame_43)
        self.label_70.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 28px;\n"
"}")
        self.label_70.setObjectName("label_70")
        self.horizontalLayout_57.addWidget(self.label_70, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_83.addWidget(self.frame_43)
        self.frame_61 = QtWidgets.QFrame(self.frame_75)
        self.frame_61.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_61.setObjectName("frame_61")
        self.verticalLayout_80 = QtWidgets.QVBoxLayout(self.frame_61)
        self.verticalLayout_80.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_80.setSpacing(6)
        self.verticalLayout_80.setObjectName("verticalLayout_80")
        self.horizontalLayout_79 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_79.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_79.setSpacing(25)
        self.horizontalLayout_79.setObjectName("horizontalLayout_79")
        self.frame_64 = QtWidgets.QFrame(self.frame_61)
        self.frame_64.setStyleSheet("QFrame {\n"
"    background-color: rgb(153, 188, 244);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_64.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_64.setObjectName("frame_64")
        self.verticalLayout_81 = QtWidgets.QVBoxLayout(self.frame_64)
        self.verticalLayout_81.setObjectName("verticalLayout_81")
        self.label_79 = QtWidgets.QLabel(self.frame_64)
        self.label_79.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_79.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 18px;\n"
"}")
        self.label_79.setWordWrap(False)
        self.label_79.setObjectName("label_79")
        self.verticalLayout_81.addWidget(self.label_79, 0, QtCore.Qt.AlignHCenter)
        self.frame_93 = QtWidgets.QFrame(self.frame_64)
        self.frame_93.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_93.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_93.setObjectName("frame_93")
        self.horizontalLayout_107 = QtWidgets.QHBoxLayout(self.frame_93)
        self.horizontalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_107.setObjectName("horizontalLayout_107")
        self.boton_seleccionar_archivo_ventas = QtWidgets.QPushButton(self.frame_93)
        self.boton_seleccionar_archivo_ventas.setMinimumSize(QtCore.QSize(250, 45))
        self.boton_seleccionar_archivo_ventas.setMaximumSize(QtCore.QSize(250, 45))
        self.boton_seleccionar_archivo_ventas.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.boton_seleccionar_archivo_ventas.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color:#416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"    border-radius : 15px;\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"}")
        self.boton_seleccionar_archivo_ventas.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/img/icono_subir_archivo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_seleccionar_archivo_ventas.setIcon(icon2)
        self.boton_seleccionar_archivo_ventas.setIconSize(QtCore.QSize(32, 32))
        self.boton_seleccionar_archivo_ventas.setObjectName("boton_seleccionar_archivo_ventas")
        self.horizontalLayout_107.addWidget(self.boton_seleccionar_archivo_ventas)
        self.boton_ayuda_archivo_ventas = QtWidgets.QPushButton(self.frame_93)
        self.boton_ayuda_archivo_ventas.setMaximumSize(QtCore.QSize(30, 30))
        self.boton_ayuda_archivo_ventas.setStyleSheet("QPushButton {\n"
"    background-color:#416BBF;\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 14px;\n"
"    border-radius : 15px;\n"
"    text-align: center;\n"
"}")
        self.boton_ayuda_archivo_ventas.setObjectName("boton_ayuda_archivo_ventas")
        self.horizontalLayout_107.addWidget(self.boton_ayuda_archivo_ventas)
        self.verticalLayout_81.addWidget(self.frame_93)
        self.boton_subir_archivo = QtWidgets.QPushButton(self.frame_64)
        self.boton_subir_archivo.setMinimumSize(QtCore.QSize(120, 40))
        self.boton_subir_archivo.setStyleSheet("QPushButton {\n"
"    background-color: rgb(65, 107, 191);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"    border-radius : 15px;\n"
"}")
        self.boton_subir_archivo.setObjectName("boton_subir_archivo")
        self.verticalLayout_81.addWidget(self.boton_subir_archivo, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_79.addWidget(self.frame_64)
        self.frame_78 = QtWidgets.QFrame(self.frame_61)
        self.frame_78.setMaximumSize(QtCore.QSize(550, 16777215))
        self.frame_78.setStyleSheet("QFrame {\n"
"    background-color: rgb(153, 188, 244);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_78.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_78.setObjectName("frame_78")
        self.horizontalLayout_90 = QtWidgets.QHBoxLayout(self.frame_78)
        self.horizontalLayout_90.setObjectName("horizontalLayout_90")
        self.frame_94 = QtWidgets.QFrame(self.frame_78)
        self.frame_94.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_94.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_94.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_94.setObjectName("frame_94")
        self.verticalLayout_90 = QtWidgets.QVBoxLayout(self.frame_94)
        self.verticalLayout_90.setObjectName("verticalLayout_90")
        self.tabla_eliminar_registros_de_archivos = QtWidgets.QTableWidget(self.frame_94)
        self.tabla_eliminar_registros_de_archivos.setMinimumSize(QtCore.QSize(0, 0))
        self.tabla_eliminar_registros_de_archivos.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabla_eliminar_registros_de_archivos.setAutoFillBackground(True)
        self.tabla_eliminar_registros_de_archivos.setStyleSheet("QTableWidget::item {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-bottom: 1px solid #C8D0DB;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.tabla_eliminar_registros_de_archivos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_eliminar_registros_de_archivos.setProperty("showDropIndicator", False)
        self.tabla_eliminar_registros_de_archivos.setDragDropOverwriteMode(False)
        self.tabla_eliminar_registros_de_archivos.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tabla_eliminar_registros_de_archivos.setShowGrid(False)
        self.tabla_eliminar_registros_de_archivos.setGridStyle(QtCore.Qt.SolidLine)
        self.tabla_eliminar_registros_de_archivos.setCornerButtonEnabled(False)
        self.tabla_eliminar_registros_de_archivos.setObjectName("tabla_eliminar_registros_de_archivos")
        self.tabla_eliminar_registros_de_archivos.setColumnCount(3)
        self.tabla_eliminar_registros_de_archivos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_eliminar_registros_de_archivos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_eliminar_registros_de_archivos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_eliminar_registros_de_archivos.setHorizontalHeaderItem(2, item)
        self.tabla_eliminar_registros_de_archivos.horizontalHeader().setCascadingSectionResizes(True)
        self.tabla_eliminar_registros_de_archivos.horizontalHeader().setDefaultSectionSize(150)
        self.tabla_eliminar_registros_de_archivos.horizontalHeader().setMinimumSectionSize(30)
        self.tabla_eliminar_registros_de_archivos.horizontalHeader().setStretchLastSection(True)
        self.tabla_eliminar_registros_de_archivos.verticalHeader().setVisible(False)
        self.tabla_eliminar_registros_de_archivos.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_90.addWidget(self.tabla_eliminar_registros_de_archivos)
        self.horizontalLayout_90.addWidget(self.frame_94)
        self.horizontalLayout_79.addWidget(self.frame_78)
        self.verticalLayout_80.addLayout(self.horizontalLayout_79)
        self.verticalLayout_83.addWidget(self.frame_61)
        self.verticalLayout_82.addWidget(self.frame_75)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_67.addWidget(self.scrollArea)
        self.verticalLayout_66.addWidget(self.frame_8)
        self.stacked_widget_paginas.addWidget(self.pagina_importar_datos)
        self.pagina_agregar_usuario = QtWidgets.QWidget()
        self.pagina_agregar_usuario.setObjectName("pagina_agregar_usuario")
        self.verticalLayout_91 = QtWidgets.QVBoxLayout(self.pagina_agregar_usuario)
        self.verticalLayout_91.setObjectName("verticalLayout_91")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.pagina_agregar_usuario)
        self.scrollArea_2.setStyleSheet("border: none;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1036, 670))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_111 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_111.setObjectName("verticalLayout_111")
        self.frame_100 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_100.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_100.setObjectName("frame_100")
        self.verticalLayout_98 = QtWidgets.QVBoxLayout(self.frame_100)
        self.verticalLayout_98.setSpacing(20)
        self.verticalLayout_98.setObjectName("verticalLayout_98")
        self.widget_12 = QtWidgets.QWidget(self.frame_100)
        self.widget_12.setMinimumSize(QtCore.QSize(0, 70))
        self.widget_12.setMaximumSize(QtCore.QSize(16777215, 90))
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_99 = QtWidgets.QVBoxLayout(self.widget_12)
        self.verticalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_99.setSpacing(0)
        self.verticalLayout_99.setObjectName("verticalLayout_99")
        self.horizontalLayout_116 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_116.setObjectName("horizontalLayout_116")
        self.frame_101 = QtWidgets.QFrame(self.widget_12)
        self.frame_101.setStyleSheet("border: none;")
        self.frame_101.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_101.setObjectName("frame_101")
        self.verticalLayout_100 = QtWidgets.QVBoxLayout(self.frame_101)
        self.verticalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_100.setObjectName("verticalLayout_100")
        self.verticalLayout_101 = QtWidgets.QVBoxLayout()
        self.verticalLayout_101.setObjectName("verticalLayout_101")
        self.label_tipo_usuario_agregar_usuario = QtWidgets.QLabel(self.frame_101)
        self.label_tipo_usuario_agregar_usuario.setMinimumSize(QtCore.QSize(0, 40))
        self.label_tipo_usuario_agregar_usuario.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_tipo_usuario_agregar_usuario.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"}")
        self.label_tipo_usuario_agregar_usuario.setObjectName("label_tipo_usuario_agregar_usuario")
        self.verticalLayout_101.addWidget(self.label_tipo_usuario_agregar_usuario)
        self.frame_102 = QtWidgets.QFrame(self.frame_101)
        self.frame_102.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_102.setMaximumSize(QtCore.QSize(300, 4))
        self.frame_102.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;")
        self.frame_102.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_102.setObjectName("frame_102")
        self.verticalLayout_101.addWidget(self.frame_102)
        self.verticalLayout_100.addLayout(self.verticalLayout_101)
        self.horizontalLayout_116.addWidget(self.frame_101)
        self.horizontalLayout_117 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_117.setContentsMargins(0, 9, 12, 9)
        self.horizontalLayout_117.setSpacing(15)
        self.horizontalLayout_117.setObjectName("horizontalLayout_117")
        self.horizontalLayout_116.addLayout(self.horizontalLayout_117)
        self.verticalLayout_99.addLayout(self.horizontalLayout_116)
        self.verticalLayout_98.addWidget(self.widget_12)
        self.frame_98 = QtWidgets.QFrame(self.frame_100)
        self.frame_98.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_98.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_98.setStyleSheet("background-color: #97bcf5;\n"
"border-radius: 15px;")
        self.frame_98.setObjectName("frame_98")
        self.verticalLayout_103 = QtWidgets.QVBoxLayout(self.frame_98)
        self.verticalLayout_103.setContentsMargins(25, -1, 15, 9)
        self.verticalLayout_103.setSpacing(0)
        self.verticalLayout_103.setObjectName("verticalLayout_103")
        self.label_80 = QtWidgets.QLabel(self.frame_98)
        self.label_80.setMinimumSize(QtCore.QSize(0, 40))
        self.label_80.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_80.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_80.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 24px;\n"
"}")
        self.label_80.setObjectName("label_80")
        self.verticalLayout_103.addWidget(self.label_80, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_98.addWidget(self.frame_98)
        self.frame_104 = QtWidgets.QFrame(self.frame_100)
        self.frame_104.setMinimumSize(QtCore.QSize(1000, 0))
        self.frame_104.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_104.setStyleSheet("QFrame {\n"
"    background-color: #97bcf5;\n"
"    border-radius: 15px;\n"
"}")
        self.frame_104.setObjectName("frame_104")
        self.verticalLayout_93 = QtWidgets.QVBoxLayout(self.frame_104)
        self.verticalLayout_93.setObjectName("verticalLayout_93")
        self.horizontalLayout_95 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_95.setSpacing(20)
        self.horizontalLayout_95.setObjectName("horizontalLayout_95")
        self.verticalLayout_97 = QtWidgets.QVBoxLayout()
        self.verticalLayout_97.setObjectName("verticalLayout_97")
        self.label_mensaje_agregar = QtWidgets.QLabel(self.frame_104)
        self.label_mensaje_agregar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_mensaje_agregar.setStyleSheet("QLabel {\n"
"    color: rgb(255, 0, 0);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"}")
        self.label_mensaje_agregar.setText("")
        self.label_mensaje_agregar.setWordWrap(True)
        self.label_mensaje_agregar.setObjectName("label_mensaje_agregar")
        self.verticalLayout_97.addWidget(self.label_mensaje_agregar, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_114 = QtWidgets.QFrame(self.frame_104)
        self.frame_114.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_114.setMaximumSize(QtCore.QSize(250, 50))
        self.frame_114.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_114.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_114.setObjectName("frame_114")
        self.horizontalLayout_132 = QtWidgets.QHBoxLayout(self.frame_114)
        self.horizontalLayout_132.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_132.setObjectName("horizontalLayout_132")
        self.campo_apellido_paterno_agregar = QtWidgets.QLineEdit(self.frame_114)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_apellido_paterno_agregar.sizePolicy().hasHeightForWidth())
        self.campo_apellido_paterno_agregar.setSizePolicy(sizePolicy)
        self.campo_apellido_paterno_agregar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"color: #416BBF;\n"
"border: none;")
        self.campo_apellido_paterno_agregar.setClearButtonEnabled(False)
        self.campo_apellido_paterno_agregar.setObjectName("campo_apellido_paterno_agregar")
        self.horizontalLayout_132.addWidget(self.campo_apellido_paterno_agregar)
        self.gridLayout_2.addWidget(self.frame_114, 0, 1, 1, 1)
        self.frame_106 = QtWidgets.QFrame(self.frame_104)
        self.frame_106.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_106.setMaximumSize(QtCore.QSize(250, 50))
        self.frame_106.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_106.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_106.setObjectName("frame_106")
        self.horizontalLayout_124 = QtWidgets.QHBoxLayout(self.frame_106)
        self.horizontalLayout_124.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_124.setObjectName("horizontalLayout_124")
        self.campo_nombre_empleado_agregar = QtWidgets.QLineEdit(self.frame_106)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_nombre_empleado_agregar.sizePolicy().hasHeightForWidth())
        self.campo_nombre_empleado_agregar.setSizePolicy(sizePolicy)
        self.campo_nombre_empleado_agregar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"color: #416BBF;\n"
"border: none;")
        self.campo_nombre_empleado_agregar.setClearButtonEnabled(False)
        self.campo_nombre_empleado_agregar.setObjectName("campo_nombre_empleado_agregar")
        self.horizontalLayout_124.addWidget(self.campo_nombre_empleado_agregar)
        self.gridLayout_2.addWidget(self.frame_106, 0, 0, 1, 1)
        self.frame_108 = QtWidgets.QFrame(self.frame_104)
        self.frame_108.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_108.setMaximumSize(QtCore.QSize(250, 50))
        self.frame_108.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_108.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_108.setObjectName("frame_108")
        self.horizontalLayout_126 = QtWidgets.QHBoxLayout(self.frame_108)
        self.horizontalLayout_126.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_126.setObjectName("horizontalLayout_126")
        self.campo_apellido_materno_agregar = QtWidgets.QLineEdit(self.frame_108)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_apellido_materno_agregar.sizePolicy().hasHeightForWidth())
        self.campo_apellido_materno_agregar.setSizePolicy(sizePolicy)
        self.campo_apellido_materno_agregar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"color: #416BBF;\n"
"border: none;")
        self.campo_apellido_materno_agregar.setClearButtonEnabled(False)
        self.campo_apellido_materno_agregar.setObjectName("campo_apellido_materno_agregar")
        self.horizontalLayout_126.addWidget(self.campo_apellido_materno_agregar)
        self.gridLayout_2.addWidget(self.frame_108, 1, 0, 1, 1)
        self.frame_107 = QtWidgets.QFrame(self.frame_104)
        self.frame_107.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_107.setMaximumSize(QtCore.QSize(250, 50))
        self.frame_107.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_107.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_107.setObjectName("frame_107")
        self.horizontalLayout_125 = QtWidgets.QHBoxLayout(self.frame_107)
        self.horizontalLayout_125.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_125.setObjectName("horizontalLayout_125")
        self.campo_numero_telefono_agregar = QtWidgets.QLineEdit(self.frame_107)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_numero_telefono_agregar.sizePolicy().hasHeightForWidth())
        self.campo_numero_telefono_agregar.setSizePolicy(sizePolicy)
        self.campo_numero_telefono_agregar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"color: #416BBF;\n"
"border: none;")
        self.campo_numero_telefono_agregar.setClearButtonEnabled(False)
        self.campo_numero_telefono_agregar.setObjectName("campo_numero_telefono_agregar")
        self.horizontalLayout_125.addWidget(self.campo_numero_telefono_agregar)
        self.gridLayout_2.addWidget(self.frame_107, 1, 1, 1, 1)
        self.frame_109 = QtWidgets.QFrame(self.frame_104)
        self.frame_109.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_109.setMaximumSize(QtCore.QSize(250, 50))
        self.frame_109.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_109.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_109.setObjectName("frame_109")
        self.horizontalLayout_127 = QtWidgets.QHBoxLayout(self.frame_109)
        self.horizontalLayout_127.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_127.setObjectName("horizontalLayout_127")
        self.campo_contrasena_empleado_agregar = QtWidgets.QLineEdit(self.frame_109)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_contrasena_empleado_agregar.sizePolicy().hasHeightForWidth())
        self.campo_contrasena_empleado_agregar.setSizePolicy(sizePolicy)
        self.campo_contrasena_empleado_agregar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"color: #416BBF;\n"
"border: none;")
        self.campo_contrasena_empleado_agregar.setEchoMode(QtWidgets.QLineEdit.Password)
        self.campo_contrasena_empleado_agregar.setClearButtonEnabled(False)
        self.campo_contrasena_empleado_agregar.setObjectName("campo_contrasena_empleado_agregar")
        self.horizontalLayout_127.addWidget(self.campo_contrasena_empleado_agregar)
        self.gridLayout_2.addWidget(self.frame_109, 2, 1, 1, 1)
        self.frame_110 = QtWidgets.QFrame(self.frame_104)
        self.frame_110.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_110.setMaximumSize(QtCore.QSize(250, 50))
        self.frame_110.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_110.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_110.setObjectName("frame_110")
        self.horizontalLayout_128 = QtWidgets.QHBoxLayout(self.frame_110)
        self.horizontalLayout_128.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_128.setObjectName("horizontalLayout_128")
        self.campo_correo_empleado_agregar = QtWidgets.QLineEdit(self.frame_110)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_correo_empleado_agregar.sizePolicy().hasHeightForWidth())
        self.campo_correo_empleado_agregar.setSizePolicy(sizePolicy)
        self.campo_correo_empleado_agregar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"color: #416BBF;\n"
"border: none;")
        self.campo_correo_empleado_agregar.setClearButtonEnabled(False)
        self.campo_correo_empleado_agregar.setObjectName("campo_correo_empleado_agregar")
        self.horizontalLayout_128.addWidget(self.campo_correo_empleado_agregar)
        self.gridLayout_2.addWidget(self.frame_110, 2, 0, 1, 1)
        self.frame_112 = QtWidgets.QFrame(self.frame_104)
        self.frame_112.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_112.setMaximumSize(QtCore.QSize(250, 50))
        self.frame_112.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_112.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_112.setObjectName("frame_112")
        self.horizontalLayout_130 = QtWidgets.QHBoxLayout(self.frame_112)
        self.horizontalLayout_130.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_130.setObjectName("horizontalLayout_130")
        self.comboBox_tipo_empleado_agregar = QtWidgets.QComboBox(self.frame_112)
        self.comboBox_tipo_empleado_agregar.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_tipo_empleado_agregar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"color: #416BBF;\n"
"border: none;")
        self.comboBox_tipo_empleado_agregar.setIconSize(QtCore.QSize(16, 16))
        self.comboBox_tipo_empleado_agregar.setObjectName("comboBox_tipo_empleado_agregar")
        self.comboBox_tipo_empleado_agregar.addItem("")
        self.comboBox_tipo_empleado_agregar.addItem("")
        self.comboBox_tipo_empleado_agregar.addItem("")
        self.horizontalLayout_130.addWidget(self.comboBox_tipo_empleado_agregar)
        self.gridLayout_2.addWidget(self.frame_112, 3, 0, 1, 1)
        self.frame_113 = QtWidgets.QFrame(self.frame_104)
        self.frame_113.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_113.setMaximumSize(QtCore.QSize(250, 50))
        self.frame_113.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_113.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_113.setObjectName("frame_113")
        self.horizontalLayout_131 = QtWidgets.QHBoxLayout(self.frame_113)
        self.horizontalLayout_131.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_131.setObjectName("horizontalLayout_131")
        self.comboBox_estatus_empleado_agregar = QtWidgets.QComboBox(self.frame_113)
        self.comboBox_estatus_empleado_agregar.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_estatus_empleado_agregar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"color: #416BBF;\n"
"border: none;")
        self.comboBox_estatus_empleado_agregar.setEditable(False)
        self.comboBox_estatus_empleado_agregar.setFrame(True)
        self.comboBox_estatus_empleado_agregar.setModelColumn(0)
        self.comboBox_estatus_empleado_agregar.setObjectName("comboBox_estatus_empleado_agregar")
        self.comboBox_estatus_empleado_agregar.addItem("")
        self.comboBox_estatus_empleado_agregar.addItem("")
        self.horizontalLayout_131.addWidget(self.comboBox_estatus_empleado_agregar)
        self.gridLayout_2.addWidget(self.frame_113, 3, 1, 1, 1)
        self.verticalLayout_97.addLayout(self.gridLayout_2)
        self.boton_agregar_empleado_agregar = QtWidgets.QPushButton(self.frame_104)
        self.boton_agregar_empleado_agregar.setMinimumSize(QtCore.QSize(30, 40))
        self.boton_agregar_empleado_agregar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.boton_agregar_empleado_agregar.setStyleSheet("QPushButton {\n"
"    background-color: rgb(65, 107, 191);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"    border-radius : 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4caf50;\n"
"}")
        self.boton_agregar_empleado_agregar.setObjectName("boton_agregar_empleado_agregar")
        self.verticalLayout_97.addWidget(self.boton_agregar_empleado_agregar)
        self.horizontalLayout_95.addLayout(self.verticalLayout_97)
        self.frame_99 = QtWidgets.QFrame(self.frame_104)
        self.frame_99.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_99.setStyleSheet("QFrame {\n"
"    background-color: #a5cbfe;\n"
"    border-radius: 15px;\n"
"}")
        self.frame_99.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_99.setObjectName("frame_99")
        self.verticalLayout_94 = QtWidgets.QVBoxLayout(self.frame_99)
        self.verticalLayout_94.setObjectName("verticalLayout_94")
        self.label_83 = QtWidgets.QLabel(self.frame_99)
        self.label_83.setMinimumSize(QtCore.QSize(0, 40))
        self.label_83.setMaximumSize(QtCore.QSize(400, 40))
        self.label_83.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_83.setStyleSheet("QLabel {\n"
"    color: #4670c1;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 26px;\n"
"}")
        self.label_83.setObjectName("label_83")
        self.verticalLayout_94.addWidget(self.label_83, 0, QtCore.Qt.AlignHCenter)
        self.label_numero_empleado_agregar = QtWidgets.QLabel(self.frame_99)
        self.label_numero_empleado_agregar.setMinimumSize(QtCore.QSize(0, 40))
        self.label_numero_empleado_agregar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_numero_empleado_agregar.setStyleSheet("QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"}")
        self.label_numero_empleado_agregar.setText("")
        self.label_numero_empleado_agregar.setObjectName("label_numero_empleado_agregar")
        self.verticalLayout_94.addWidget(self.label_numero_empleado_agregar, 0, QtCore.Qt.AlignHCenter)
        self.label_16 = QtWidgets.QLabel(self.frame_99)
        self.label_16.setMaximumSize(QtCore.QSize(372, 324))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("resources/img/agregar_usuario.svg"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_94.addWidget(self.label_16, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_95.addWidget(self.frame_99)
        self.verticalLayout_93.addLayout(self.horizontalLayout_95)
        self.verticalLayout_98.addWidget(self.frame_104)
        self.verticalLayout_111.addWidget(self.frame_100)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_91.addWidget(self.scrollArea_2)
        self.stacked_widget_paginas.addWidget(self.pagina_agregar_usuario)
        self.pagina_editar_usuario = QtWidgets.QWidget()
        self.pagina_editar_usuario.setObjectName("pagina_editar_usuario")
        self.verticalLayout_92 = QtWidgets.QVBoxLayout(self.pagina_editar_usuario)
        self.verticalLayout_92.setObjectName("verticalLayout_92")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.pagina_editar_usuario)
        self.scrollArea_3.setStyleSheet("border: none;")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1036, 720))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_112 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_112.setObjectName("verticalLayout_112")
        self.frame_103 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_103.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_103.setObjectName("frame_103")
        self.verticalLayout_102 = QtWidgets.QVBoxLayout(self.frame_103)
        self.verticalLayout_102.setSpacing(20)
        self.verticalLayout_102.setObjectName("verticalLayout_102")
        self.widget_14 = QtWidgets.QWidget(self.frame_103)
        self.widget_14.setMinimumSize(QtCore.QSize(0, 70))
        self.widget_14.setMaximumSize(QtCore.QSize(16777215, 90))
        self.widget_14.setObjectName("widget_14")
        self.verticalLayout_104 = QtWidgets.QVBoxLayout(self.widget_14)
        self.verticalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_104.setSpacing(0)
        self.verticalLayout_104.setObjectName("verticalLayout_104")
        self.horizontalLayout_129 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_129.setObjectName("horizontalLayout_129")
        self.frame_111 = QtWidgets.QFrame(self.widget_14)
        self.frame_111.setStyleSheet("border: none;")
        self.frame_111.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_111.setObjectName("frame_111")
        self.verticalLayout_105 = QtWidgets.QVBoxLayout(self.frame_111)
        self.verticalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_105.setObjectName("verticalLayout_105")
        self.verticalLayout_106 = QtWidgets.QVBoxLayout()
        self.verticalLayout_106.setObjectName("verticalLayout_106")
        self.label_tipo_usuario_editar_usuario = QtWidgets.QLabel(self.frame_111)
        self.label_tipo_usuario_editar_usuario.setMinimumSize(QtCore.QSize(0, 40))
        self.label_tipo_usuario_editar_usuario.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_tipo_usuario_editar_usuario.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"}")
        self.label_tipo_usuario_editar_usuario.setObjectName("label_tipo_usuario_editar_usuario")
        self.verticalLayout_106.addWidget(self.label_tipo_usuario_editar_usuario)
        self.frame_115 = QtWidgets.QFrame(self.frame_111)
        self.frame_115.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_115.setMaximumSize(QtCore.QSize(300, 4))
        self.frame_115.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;")
        self.frame_115.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_115.setObjectName("frame_115")
        self.verticalLayout_106.addWidget(self.frame_115)
        self.verticalLayout_105.addLayout(self.verticalLayout_106)
        self.horizontalLayout_129.addWidget(self.frame_111)
        self.verticalLayout_104.addLayout(self.horizontalLayout_129)
        self.verticalLayout_102.addWidget(self.widget_14)
        self.frame_97 = QtWidgets.QFrame(self.frame_103)
        self.frame_97.setMinimumSize(QtCore.QSize(0, 120))
        self.frame_97.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_97.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_97.setObjectName("frame_97")
        self.verticalLayout_96 = QtWidgets.QVBoxLayout(self.frame_97)
        self.verticalLayout_96.setObjectName("verticalLayout_96")
        self.horizontalLayout_110 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_110.setSpacing(24)
        self.horizontalLayout_110.setObjectName("horizontalLayout_110")
        self.frame_96 = QtWidgets.QFrame(self.frame_97)
        self.frame_96.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_96.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_96.setStyleSheet("background-color: #97bcf5;\n"
"border-radius: 15px;")
        self.frame_96.setObjectName("frame_96")
        self.verticalLayout_107 = QtWidgets.QVBoxLayout(self.frame_96)
        self.verticalLayout_107.setContentsMargins(25, -1, 15, 9)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName("verticalLayout_107")
        self.label_81 = QtWidgets.QLabel(self.frame_96)
        self.label_81.setMinimumSize(QtCore.QSize(0, 40))
        self.label_81.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_81.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_81.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 24px;\n"
"}")
        self.label_81.setObjectName("label_81")
        self.verticalLayout_107.addWidget(self.label_81, 0, QtCore.Qt.AlignHCenter)
        self.label_84 = QtWidgets.QLabel(self.frame_96)
        self.label_84.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 24px;\n"
"}")
        self.label_84.setObjectName("label_84")
        self.verticalLayout_107.addWidget(self.label_84, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_110.addWidget(self.frame_96)
        self.verticalLayout_110 = QtWidgets.QVBoxLayout()
        self.verticalLayout_110.setObjectName("verticalLayout_110")
        self.label_85 = QtWidgets.QLabel(self.frame_97)
        self.label_85.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 14px;\n"
"}")
        self.label_85.setObjectName("label_85")
        self.verticalLayout_110.addWidget(self.label_85, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_134 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_134.setContentsMargins(0, 9, 12, 9)
        self.horizontalLayout_134.setSpacing(15)
        self.horizontalLayout_134.setObjectName("horizontalLayout_134")
        self.frame_126 = QtWidgets.QFrame(self.frame_97)
        self.frame_126.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_126.setMaximumSize(QtCore.QSize(250, 20))
        self.frame_126.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_126.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_126.setObjectName("frame_126")
        self.horizontalLayout_143 = QtWidgets.QHBoxLayout(self.frame_126)
        self.horizontalLayout_143.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_143.setObjectName("horizontalLayout_143")
        self.campo_busca_numero_empleado_editar = QtWidgets.QLineEdit(self.frame_126)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_busca_numero_empleado_editar.sizePolicy().hasHeightForWidth())
        self.campo_busca_numero_empleado_editar.setSizePolicy(sizePolicy)
        self.campo_busca_numero_empleado_editar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 12px;\n"
"color: rgb(52, 64, 85);\n"
"border: none;")
        self.campo_busca_numero_empleado_editar.setClearButtonEnabled(False)
        self.campo_busca_numero_empleado_editar.setObjectName("campo_busca_numero_empleado_editar")
        self.horizontalLayout_143.addWidget(self.campo_busca_numero_empleado_editar)
        self.horizontalLayout_134.addWidget(self.frame_126, 0, QtCore.Qt.AlignVCenter)
        self.boton_buscar_empleados_editar = QtWidgets.QPushButton(self.frame_97)
        self.boton_buscar_empleados_editar.setMinimumSize(QtCore.QSize(30, 40))
        self.boton_buscar_empleados_editar.setMaximumSize(QtCore.QSize(90, 16777215))
        self.boton_buscar_empleados_editar.setStyleSheet("QPushButton {\n"
"    background-color: rgb(65, 107, 191);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"    border-radius : 15px;\n"
"}")
        self.boton_buscar_empleados_editar.setObjectName("boton_buscar_empleados_editar")
        self.horizontalLayout_134.addWidget(self.boton_buscar_empleados_editar)
        self.verticalLayout_110.addLayout(self.horizontalLayout_134)
        self.horizontalLayout_110.addLayout(self.verticalLayout_110)
        self.verticalLayout_96.addLayout(self.horizontalLayout_110)
        self.verticalLayout_102.addWidget(self.frame_97)
        self.frame_116 = QtWidgets.QFrame(self.frame_103)
        self.frame_116.setMinimumSize(QtCore.QSize(1000, 0))
        self.frame_116.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_116.setStyleSheet("QFrame {\n"
"    background-color: #97bcf5;\n"
"    border-radius: 15px;\n"
"}")
        self.frame_116.setObjectName("frame_116")
        self.verticalLayout_95 = QtWidgets.QVBoxLayout(self.frame_116)
        self.verticalLayout_95.setObjectName("verticalLayout_95")
        self.horizontalLayout_108 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_108.setSpacing(20)
        self.horizontalLayout_108.setObjectName("horizontalLayout_108")
        self.verticalLayout_108 = QtWidgets.QVBoxLayout()
        self.verticalLayout_108.setObjectName("verticalLayout_108")
        self.label_mensaje_editar = QtWidgets.QLabel(self.frame_116)
        self.label_mensaje_editar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_mensaje_editar.setStyleSheet("QLabel {\n"
"    color: rgb(255, 0, 0);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"}")
        self.label_mensaje_editar.setText("")
        self.label_mensaje_editar.setWordWrap(True)
        self.label_mensaje_editar.setObjectName("label_mensaje_editar")
        self.verticalLayout_108.addWidget(self.label_mensaje_editar, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_118 = QtWidgets.QFrame(self.frame_116)
        self.frame_118.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_118.setMaximumSize(QtCore.QSize(250, 50))
        self.frame_118.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_118.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_118.setObjectName("frame_118")
        self.horizontalLayout_135 = QtWidgets.QHBoxLayout(self.frame_118)
        self.horizontalLayout_135.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_135.setObjectName("horizontalLayout_135")
        self.campo_apellido_paterno_editar = QtWidgets.QLineEdit(self.frame_118)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_apellido_paterno_editar.sizePolicy().hasHeightForWidth())
        self.campo_apellido_paterno_editar.setSizePolicy(sizePolicy)
        self.campo_apellido_paterno_editar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"color: #416BBF;\n"
"border: none;")
        self.campo_apellido_paterno_editar.setClearButtonEnabled(False)
        self.campo_apellido_paterno_editar.setObjectName("campo_apellido_paterno_editar")
        self.horizontalLayout_135.addWidget(self.campo_apellido_paterno_editar)
        self.gridLayout_3.addWidget(self.frame_118, 0, 1, 1, 1)
        self.frame_119 = QtWidgets.QFrame(self.frame_116)
        self.frame_119.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_119.setMaximumSize(QtCore.QSize(250, 50))
        self.frame_119.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_119.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_119.setObjectName("frame_119")
        self.horizontalLayout_136 = QtWidgets.QHBoxLayout(self.frame_119)
        self.horizontalLayout_136.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_136.setObjectName("horizontalLayout_136")
        self.campo_nombre_empleado_editar = QtWidgets.QLineEdit(self.frame_119)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_nombre_empleado_editar.sizePolicy().hasHeightForWidth())
        self.campo_nombre_empleado_editar.setSizePolicy(sizePolicy)
        self.campo_nombre_empleado_editar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"color: #416BBF;\n"
"border: none;")
        self.campo_nombre_empleado_editar.setClearButtonEnabled(False)
        self.campo_nombre_empleado_editar.setObjectName("campo_nombre_empleado_editar")
        self.horizontalLayout_136.addWidget(self.campo_nombre_empleado_editar)
        self.gridLayout_3.addWidget(self.frame_119, 0, 0, 1, 1)
        self.frame_120 = QtWidgets.QFrame(self.frame_116)
        self.frame_120.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_120.setMaximumSize(QtCore.QSize(250, 50))
        self.frame_120.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_120.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_120.setObjectName("frame_120")
        self.horizontalLayout_137 = QtWidgets.QHBoxLayout(self.frame_120)
        self.horizontalLayout_137.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_137.setObjectName("horizontalLayout_137")
        self.campo_apellido_materno_editar = QtWidgets.QLineEdit(self.frame_120)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_apellido_materno_editar.sizePolicy().hasHeightForWidth())
        self.campo_apellido_materno_editar.setSizePolicy(sizePolicy)
        self.campo_apellido_materno_editar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"color: #416BBF;\n"
"border: none;")
        self.campo_apellido_materno_editar.setClearButtonEnabled(False)
        self.campo_apellido_materno_editar.setObjectName("campo_apellido_materno_editar")
        self.horizontalLayout_137.addWidget(self.campo_apellido_materno_editar)
        self.gridLayout_3.addWidget(self.frame_120, 1, 0, 1, 1)
        self.frame_121 = QtWidgets.QFrame(self.frame_116)
        self.frame_121.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_121.setMaximumSize(QtCore.QSize(250, 50))
        self.frame_121.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_121.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_121.setObjectName("frame_121")
        self.horizontalLayout_138 = QtWidgets.QHBoxLayout(self.frame_121)
        self.horizontalLayout_138.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_138.setObjectName("horizontalLayout_138")
        self.campo_numero_telefono_editar = QtWidgets.QLineEdit(self.frame_121)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_numero_telefono_editar.sizePolicy().hasHeightForWidth())
        self.campo_numero_telefono_editar.setSizePolicy(sizePolicy)
        self.campo_numero_telefono_editar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"color: #416BBF;\n"
"border: none;")
        self.campo_numero_telefono_editar.setClearButtonEnabled(False)
        self.campo_numero_telefono_editar.setObjectName("campo_numero_telefono_editar")
        self.horizontalLayout_138.addWidget(self.campo_numero_telefono_editar)
        self.gridLayout_3.addWidget(self.frame_121, 1, 1, 1, 1)
        self.frame_122 = QtWidgets.QFrame(self.frame_116)
        self.frame_122.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_122.setMaximumSize(QtCore.QSize(250, 50))
        self.frame_122.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_122.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_122.setObjectName("frame_122")
        self.horizontalLayout_139 = QtWidgets.QHBoxLayout(self.frame_122)
        self.horizontalLayout_139.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_139.setObjectName("horizontalLayout_139")
        self.campo_contrasena_empleado_editar = QtWidgets.QLineEdit(self.frame_122)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_contrasena_empleado_editar.sizePolicy().hasHeightForWidth())
        self.campo_contrasena_empleado_editar.setSizePolicy(sizePolicy)
        self.campo_contrasena_empleado_editar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"color: #416BBF;\n"
"border: none;")
        self.campo_contrasena_empleado_editar.setEchoMode(QtWidgets.QLineEdit.Password)
        self.campo_contrasena_empleado_editar.setClearButtonEnabled(False)
        self.campo_contrasena_empleado_editar.setObjectName("campo_contrasena_empleado_editar")
        self.horizontalLayout_139.addWidget(self.campo_contrasena_empleado_editar)
        self.gridLayout_3.addWidget(self.frame_122, 2, 1, 1, 1)
        self.frame_123 = QtWidgets.QFrame(self.frame_116)
        self.frame_123.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_123.setMaximumSize(QtCore.QSize(250, 50))
        self.frame_123.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_123.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_123.setObjectName("frame_123")
        self.horizontalLayout_140 = QtWidgets.QHBoxLayout(self.frame_123)
        self.horizontalLayout_140.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_140.setObjectName("horizontalLayout_140")
        self.campo_correo_empleado_editar = QtWidgets.QLineEdit(self.frame_123)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_correo_empleado_editar.sizePolicy().hasHeightForWidth())
        self.campo_correo_empleado_editar.setSizePolicy(sizePolicy)
        self.campo_correo_empleado_editar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"color: #416BBF;\n"
"border: none;")
        self.campo_correo_empleado_editar.setClearButtonEnabled(False)
        self.campo_correo_empleado_editar.setObjectName("campo_correo_empleado_editar")
        self.horizontalLayout_140.addWidget(self.campo_correo_empleado_editar)
        self.gridLayout_3.addWidget(self.frame_123, 2, 0, 1, 1)
        self.frame_124 = QtWidgets.QFrame(self.frame_116)
        self.frame_124.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_124.setMaximumSize(QtCore.QSize(250, 50))
        self.frame_124.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_124.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_124.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_124.setObjectName("frame_124")
        self.horizontalLayout_141 = QtWidgets.QHBoxLayout(self.frame_124)
        self.horizontalLayout_141.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_141.setObjectName("horizontalLayout_141")
        self.comboBox_tipo_empleado_editar = QtWidgets.QComboBox(self.frame_124)
        self.comboBox_tipo_empleado_editar.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_tipo_empleado_editar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"color: #416BBF;\n"
"border: none;")
        self.comboBox_tipo_empleado_editar.setObjectName("comboBox_tipo_empleado_editar")
        self.comboBox_tipo_empleado_editar.addItem("")
        self.comboBox_tipo_empleado_editar.addItem("")
        self.comboBox_tipo_empleado_editar.addItem("")
        self.horizontalLayout_141.addWidget(self.comboBox_tipo_empleado_editar)
        self.gridLayout_3.addWidget(self.frame_124, 3, 0, 1, 1)
        self.frame_125 = QtWidgets.QFrame(self.frame_116)
        self.frame_125.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_125.setMaximumSize(QtCore.QSize(250, 50))
        self.frame_125.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_125.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_125.setObjectName("frame_125")
        self.horizontalLayout_142 = QtWidgets.QHBoxLayout(self.frame_125)
        self.horizontalLayout_142.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_142.setObjectName("horizontalLayout_142")
        self.comboBox_estatus_empleado_editar = QtWidgets.QComboBox(self.frame_125)
        self.comboBox_estatus_empleado_editar.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_estatus_empleado_editar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 14px;\n"
"color: #416BBF;\n"
"border: none;")
        self.comboBox_estatus_empleado_editar.setObjectName("comboBox_estatus_empleado_editar")
        self.comboBox_estatus_empleado_editar.addItem("")
        self.comboBox_estatus_empleado_editar.addItem("")
        self.horizontalLayout_142.addWidget(self.comboBox_estatus_empleado_editar)
        self.gridLayout_3.addWidget(self.frame_125, 3, 1, 1, 1)
        self.verticalLayout_108.addLayout(self.gridLayout_3)
        self.boton_guardar_empleados_editar = QtWidgets.QPushButton(self.frame_116)
        self.boton_guardar_empleados_editar.setMinimumSize(QtCore.QSize(30, 40))
        self.boton_guardar_empleados_editar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.boton_guardar_empleados_editar.setStyleSheet("QPushButton {\n"
"    background-color: rgb(65, 107, 191);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"    border-radius : 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4caf50;\n"
"}")
        self.boton_guardar_empleados_editar.setObjectName("boton_guardar_empleados_editar")
        self.verticalLayout_108.addWidget(self.boton_guardar_empleados_editar)
        self.horizontalLayout_108.addLayout(self.verticalLayout_108)
        self.frame_105 = QtWidgets.QFrame(self.frame_116)
        self.frame_105.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_105.setStyleSheet("QFrame {\n"
"    background-color: #a5cbfe;\n"
"    border-radius: 15px;\n"
"}")
        self.frame_105.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_105.setObjectName("frame_105")
        self.verticalLayout_109 = QtWidgets.QVBoxLayout(self.frame_105)
        self.verticalLayout_109.setObjectName("verticalLayout_109")
        self.label_82 = QtWidgets.QLabel(self.frame_105)
        self.label_82.setMinimumSize(QtCore.QSize(0, 40))
        self.label_82.setMaximumSize(QtCore.QSize(400, 40))
        self.label_82.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_82.setStyleSheet("QLabel {\n"
"    color: #4670c1;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 26px;\n"
"}")
        self.label_82.setObjectName("label_82")
        self.verticalLayout_109.addWidget(self.label_82, 0, QtCore.Qt.AlignHCenter)
        self.label_numero_empleado_editar = QtWidgets.QLabel(self.frame_105)
        self.label_numero_empleado_editar.setMinimumSize(QtCore.QSize(0, 40))
        self.label_numero_empleado_editar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_numero_empleado_editar.setStyleSheet("QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 28px;\n"
"}")
        self.label_numero_empleado_editar.setText("")
        self.label_numero_empleado_editar.setObjectName("label_numero_empleado_editar")
        self.verticalLayout_109.addWidget(self.label_numero_empleado_editar, 0, QtCore.Qt.AlignHCenter)
        self.label_75 = QtWidgets.QLabel(self.frame_105)
        self.label_75.setMaximumSize(QtCore.QSize(372, 324))
        self.label_75.setText("")
        self.label_75.setPixmap(QtGui.QPixmap("resources/img/editar_usuario.svg"))
        self.label_75.setScaledContents(True)
        self.label_75.setObjectName("label_75")
        self.verticalLayout_109.addWidget(self.label_75, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_108.addWidget(self.frame_105)
        self.verticalLayout_95.addLayout(self.horizontalLayout_108)
        self.verticalLayout_102.addWidget(self.frame_116)
        self.verticalLayout_112.addWidget(self.frame_103)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_92.addWidget(self.scrollArea_3)
        self.stacked_widget_paginas.addWidget(self.pagina_editar_usuario)
        self.pagina_meta_ventas = QtWidgets.QWidget()
        self.pagina_meta_ventas.setObjectName("pagina_meta_ventas")
        self.verticalLayout_113 = QtWidgets.QVBoxLayout(self.pagina_meta_ventas)
        self.verticalLayout_113.setObjectName("verticalLayout_113")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.pagina_meta_ventas)
        self.scrollArea_4.setStyleSheet("border: none;")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1018, 514))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_114 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_114.setObjectName("verticalLayout_114")
        self.frame_95 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_95.setMinimumSize(QtCore.QSize(1000, 0))
        self.frame_95.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_95.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_95.setObjectName("frame_95")
        self.verticalLayout_116 = QtWidgets.QVBoxLayout(self.frame_95)
        self.verticalLayout_116.setObjectName("verticalLayout_116")
        self.widget_10 = QtWidgets.QWidget(self.frame_95)
        self.widget_10.setMinimumSize(QtCore.QSize(0, 70))
        self.widget_10.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_115 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_115.setContentsMargins(-1, -1, 9, 9)
        self.verticalLayout_115.setSpacing(0)
        self.verticalLayout_115.setObjectName("verticalLayout_115")
        self.label_tipo_usuario_meta_ventas = QtWidgets.QLabel(self.widget_10)
        self.label_tipo_usuario_meta_ventas.setMinimumSize(QtCore.QSize(0, 40))
        self.label_tipo_usuario_meta_ventas.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_tipo_usuario_meta_ventas.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"}")
        self.label_tipo_usuario_meta_ventas.setObjectName("label_tipo_usuario_meta_ventas")
        self.verticalLayout_115.addWidget(self.label_tipo_usuario_meta_ventas, 0, QtCore.Qt.AlignTop)
        self.frame_117 = QtWidgets.QFrame(self.widget_10)
        self.frame_117.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_117.setMaximumSize(QtCore.QSize(400, 4))
        self.frame_117.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;")
        self.frame_117.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_117.setObjectName("frame_117")
        self.verticalLayout_115.addWidget(self.frame_117, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_116.addWidget(self.widget_10)
        self.frame_127 = QtWidgets.QFrame(self.frame_95)
        self.frame_127.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_127.setStyleSheet("QFrame {\n"
"    background-color: rgb(153, 188, 244);\n"
"    border-radius: 15px;\n"
"    margin-left: 16px;\n"
"    margin-right: 16px;\n"
"}")
        self.frame_127.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_127.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_127.setObjectName("frame_127")
        self.horizontalLayout_112 = QtWidgets.QHBoxLayout(self.frame_127)
        self.horizontalLayout_112.setObjectName("horizontalLayout_112")
        self.label_86 = QtWidgets.QLabel(self.frame_127)
        self.label_86.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 28px;\n"
"}")
        self.label_86.setObjectName("label_86")
        self.horizontalLayout_112.addWidget(self.label_86, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_116.addWidget(self.frame_127)
        self.frame_128 = QtWidgets.QFrame(self.frame_95)
        self.frame_128.setStyleSheet("QFrame {\n"
"    background-color: rgb(153, 188, 244);\n"
"    border-radius: 15px;\n"
"    margin-left: 16px;\n"
"    margin-right: 16px;\n"
"}")
        self.frame_128.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_128.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_128.setObjectName("frame_128")
        self.verticalLayout_117 = QtWidgets.QVBoxLayout(self.frame_128)
        self.verticalLayout_117.setObjectName("verticalLayout_117")
        self.horizontalFrame = QtWidgets.QFrame(self.frame_128)
        self.horizontalFrame.setMaximumSize(QtCore.QSize(16777215, 150))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_113 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_113.setObjectName("horizontalLayout_113")
        self.label_87 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_87.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_87.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 18px;\n"
"}")
        self.label_87.setWordWrap(True)
        self.label_87.setObjectName("label_87")
        self.horizontalLayout_113.addWidget(self.label_87)
        self.frame_130 = QtWidgets.QFrame(self.horizontalFrame)
        self.frame_130.setMinimumSize(QtCore.QSize(250, 50))
        self.frame_130.setMaximumSize(QtCore.QSize(400, 50))
        self.frame_130.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_130.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_130.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_130.setObjectName("frame_130")
        self.horizontalLayout_144 = QtWidgets.QHBoxLayout(self.frame_130)
        self.horizontalLayout_144.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_144.setObjectName("horizontalLayout_144")
        self.campo_meta_diaria_por_empleado = QtWidgets.QLineEdit(self.frame_130)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.campo_meta_diaria_por_empleado.sizePolicy().hasHeightForWidth())
        self.campo_meta_diaria_por_empleado.setSizePolicy(sizePolicy)
        self.campo_meta_diaria_por_empleado.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font-family: \'Montserrat\';\n"
"font-style: normal;\n"
"font-weight: 600;\n"
"font-size: 14px;\n"
"color: #416BBF;\n"
"border: none;")
        self.campo_meta_diaria_por_empleado.setText("")
        self.campo_meta_diaria_por_empleado.setClearButtonEnabled(False)
        self.campo_meta_diaria_por_empleado.setObjectName("campo_meta_diaria_por_empleado")
        self.horizontalLayout_144.addWidget(self.campo_meta_diaria_por_empleado)
        self.horizontalLayout_113.addWidget(self.frame_130)
        self.boton_guardar_meta_ventas = QtWidgets.QPushButton(self.horizontalFrame)
        self.boton_guardar_meta_ventas.setMinimumSize(QtCore.QSize(30, 40))
        self.boton_guardar_meta_ventas.setMaximumSize(QtCore.QSize(140, 16777215))
        self.boton_guardar_meta_ventas.setStyleSheet("QPushButton {\n"
"    background-color: rgb(65, 107, 191);\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 14px;\n"
"    border-radius : 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4caf50;\n"
"}")
        self.boton_guardar_meta_ventas.setObjectName("boton_guardar_meta_ventas")
        self.horizontalLayout_113.addWidget(self.boton_guardar_meta_ventas)
        self.verticalLayout_117.addWidget(self.horizontalFrame)
        self.frame_129 = QtWidgets.QFrame(self.frame_128)
        self.frame_129.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_129.setObjectName("frame_129")
        self.verticalLayout_118 = QtWidgets.QVBoxLayout(self.frame_129)
        self.verticalLayout_118.setObjectName("verticalLayout_118")
        self.frame_131 = QtWidgets.QFrame(self.frame_129)
        self.frame_131.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_131.setMaximumSize(QtCore.QSize(16777215, 4))
        self.frame_131.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;")
        self.frame_131.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_131.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_131.setObjectName("frame_131")
        self.verticalLayout_118.addWidget(self.frame_131)
        self.horizontalLayout_114 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_114.setObjectName("horizontalLayout_114")
        self.verticalLayout_120 = QtWidgets.QVBoxLayout()
        self.verticalLayout_120.setObjectName("verticalLayout_120")
        self.label_88 = QtWidgets.QLabel(self.frame_129)
        self.label_88.setMaximumSize(QtCore.QSize(16777215, 120))
        self.label_88.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 18px;\n"
"}")
        self.label_88.setObjectName("label_88")
        self.verticalLayout_120.addWidget(self.label_88, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_115 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_115.setObjectName("horizontalLayout_115")
        self.label_89 = QtWidgets.QLabel(self.frame_129)
        self.label_89.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_89.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-size: 16px;\n"
"}")
        self.label_89.setObjectName("label_89")
        self.horizontalLayout_115.addWidget(self.label_89)
        self.frame_133 = QtWidgets.QFrame(self.frame_129)
        self.frame_133.setMinimumSize(QtCore.QSize(250, 50))
        self.frame_133.setMaximumSize(QtCore.QSize(400, 50))
        self.frame_133.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_133.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_133.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_133.setObjectName("frame_133")
        self.horizontalLayout_145 = QtWidgets.QHBoxLayout(self.frame_133)
        self.horizontalLayout_145.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_145.setObjectName("horizontalLayout_145")
        self.label_meta_diaria_empleado = QtWidgets.QLabel(self.frame_133)
        self.label_meta_diaria_empleado.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 18px;\n"
"}")
        self.label_meta_diaria_empleado.setObjectName("label_meta_diaria_empleado")
        self.horizontalLayout_145.addWidget(self.label_meta_diaria_empleado)
        self.horizontalLayout_115.addWidget(self.frame_133)
        self.verticalLayout_120.addLayout(self.horizontalLayout_115)
        self.horizontalLayout_119 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_119.setObjectName("horizontalLayout_119")
        self.label_91 = QtWidgets.QLabel(self.frame_129)
        self.label_91.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_91.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-size: 16px;\n"
"}")
        self.label_91.setObjectName("label_91")
        self.horizontalLayout_119.addWidget(self.label_91)
        self.frame_134 = QtWidgets.QFrame(self.frame_129)
        self.frame_134.setMinimumSize(QtCore.QSize(250, 50))
        self.frame_134.setMaximumSize(QtCore.QSize(400, 50))
        self.frame_134.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_134.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_134.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_134.setObjectName("frame_134")
        self.horizontalLayout_146 = QtWidgets.QHBoxLayout(self.frame_134)
        self.horizontalLayout_146.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_146.setObjectName("horizontalLayout_146")
        self.label_meta_mensual_empleado = QtWidgets.QLabel(self.frame_134)
        self.label_meta_mensual_empleado.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 18px;\n"
"}")
        self.label_meta_mensual_empleado.setObjectName("label_meta_mensual_empleado")
        self.horizontalLayout_146.addWidget(self.label_meta_mensual_empleado)
        self.horizontalLayout_119.addWidget(self.frame_134)
        self.verticalLayout_120.addLayout(self.horizontalLayout_119)
        self.horizontalLayout_121 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_121.setObjectName("horizontalLayout_121")
        self.label_92 = QtWidgets.QLabel(self.frame_129)
        self.label_92.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_92.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-size: 16px;\n"
"}")
        self.label_92.setObjectName("label_92")
        self.horizontalLayout_121.addWidget(self.label_92)
        self.frame_135 = QtWidgets.QFrame(self.frame_129)
        self.frame_135.setMinimumSize(QtCore.QSize(250, 50))
        self.frame_135.setMaximumSize(QtCore.QSize(400, 50))
        self.frame_135.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_135.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_135.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_135.setObjectName("frame_135")
        self.horizontalLayout_147 = QtWidgets.QHBoxLayout(self.frame_135)
        self.horizontalLayout_147.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_147.setObjectName("horizontalLayout_147")
        self.label_meta_anual_empleado = QtWidgets.QLabel(self.frame_135)
        self.label_meta_anual_empleado.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 18px;\n"
"}")
        self.label_meta_anual_empleado.setObjectName("label_meta_anual_empleado")
        self.horizontalLayout_147.addWidget(self.label_meta_anual_empleado)
        self.horizontalLayout_121.addWidget(self.frame_135)
        self.verticalLayout_120.addLayout(self.horizontalLayout_121)
        self.horizontalLayout_114.addLayout(self.verticalLayout_120)
        self.verticalLayout_119 = QtWidgets.QVBoxLayout()
        self.verticalLayout_119.setObjectName("verticalLayout_119")
        self.verticalLayout_121 = QtWidgets.QVBoxLayout()
        self.verticalLayout_121.setObjectName("verticalLayout_121")
        self.label_90 = QtWidgets.QLabel(self.frame_129)
        self.label_90.setMaximumSize(QtCore.QSize(16777215, 120))
        self.label_90.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 18px;\n"
"}")
        self.label_90.setObjectName("label_90")
        self.verticalLayout_121.addWidget(self.label_90, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_122 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_122.setObjectName("horizontalLayout_122")
        self.label_96 = QtWidgets.QLabel(self.frame_129)
        self.label_96.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_96.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-size: 16px;\n"
"}")
        self.label_96.setObjectName("label_96")
        self.horizontalLayout_122.addWidget(self.label_96)
        self.frame_136 = QtWidgets.QFrame(self.frame_129)
        self.frame_136.setMinimumSize(QtCore.QSize(250, 50))
        self.frame_136.setMaximumSize(QtCore.QSize(400, 50))
        self.frame_136.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_136.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_136.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_136.setObjectName("frame_136")
        self.horizontalLayout_148 = QtWidgets.QHBoxLayout(self.frame_136)
        self.horizontalLayout_148.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_148.setObjectName("horizontalLayout_148")
        self.label_meta_diaria_total = QtWidgets.QLabel(self.frame_136)
        self.label_meta_diaria_total.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 18px;\n"
"}")
        self.label_meta_diaria_total.setObjectName("label_meta_diaria_total")
        self.horizontalLayout_148.addWidget(self.label_meta_diaria_total)
        self.horizontalLayout_122.addWidget(self.frame_136)
        self.verticalLayout_121.addLayout(self.horizontalLayout_122)
        self.horizontalLayout_123 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_123.setObjectName("horizontalLayout_123")
        self.label_98 = QtWidgets.QLabel(self.frame_129)
        self.label_98.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_98.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-size: 16px;\n"
"}")
        self.label_98.setObjectName("label_98")
        self.horizontalLayout_123.addWidget(self.label_98)
        self.frame_137 = QtWidgets.QFrame(self.frame_129)
        self.frame_137.setMinimumSize(QtCore.QSize(250, 50))
        self.frame_137.setMaximumSize(QtCore.QSize(400, 50))
        self.frame_137.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_137.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_137.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_137.setObjectName("frame_137")
        self.horizontalLayout_149 = QtWidgets.QHBoxLayout(self.frame_137)
        self.horizontalLayout_149.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_149.setObjectName("horizontalLayout_149")
        self.label_meta_mensual_total = QtWidgets.QLabel(self.frame_137)
        self.label_meta_mensual_total.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 18px;\n"
"}")
        self.label_meta_mensual_total.setObjectName("label_meta_mensual_total")
        self.horizontalLayout_149.addWidget(self.label_meta_mensual_total)
        self.horizontalLayout_123.addWidget(self.frame_137)
        self.verticalLayout_121.addLayout(self.horizontalLayout_123)
        self.horizontalLayout_133 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_133.setObjectName("horizontalLayout_133")
        self.label_100 = QtWidgets.QLabel(self.frame_129)
        self.label_100.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_100.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-size: 16px;\n"
"}")
        self.label_100.setObjectName("label_100")
        self.horizontalLayout_133.addWidget(self.label_100)
        self.frame_138 = QtWidgets.QFrame(self.frame_129)
        self.frame_138.setMinimumSize(QtCore.QSize(250, 50))
        self.frame_138.setMaximumSize(QtCore.QSize(400, 50))
        self.frame_138.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_138.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_138.setObjectName("frame_138")
        self.horizontalLayout_150 = QtWidgets.QHBoxLayout(self.frame_138)
        self.horizontalLayout_150.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_150.setObjectName("horizontalLayout_150")
        self.label_meta_anual_total = QtWidgets.QLabel(self.frame_138)
        self.label_meta_anual_total.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 18px;\n"
"}")
        self.label_meta_anual_total.setObjectName("label_meta_anual_total")
        self.horizontalLayout_150.addWidget(self.label_meta_anual_total)
        self.horizontalLayout_133.addWidget(self.frame_138)
        self.verticalLayout_121.addLayout(self.horizontalLayout_133)
        self.verticalLayout_119.addLayout(self.verticalLayout_121)
        self.horizontalLayout_114.addLayout(self.verticalLayout_119)
        self.verticalLayout_118.addLayout(self.horizontalLayout_114)
        self.verticalLayout_117.addWidget(self.frame_129)
        self.verticalLayout_116.addWidget(self.frame_128)
        self.verticalLayout_114.addWidget(self.frame_95)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_113.addWidget(self.scrollArea_4)
        self.stacked_widget_paginas.addWidget(self.pagina_meta_ventas)
        self.verticalLayout.addWidget(self.stacked_widget_paginas)
        self.horizontalLayout.addWidget(self.frame_informacion)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stacked_widget_paginas.setCurrentIndex(6)
        self.comboBox_tipo_empleado_agregar.setCurrentIndex(0)
        self.comboBox_estatus_empleado_agregar.setCurrentIndex(0)
        self.comboBox_tipo_empleado_editar.setCurrentIndex(0)
        self.comboBox_estatus_empleado_editar.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Espressoft"))
        self.boton_ventas_totales.setText(_translate("MainWindow", "Ventas totales"))
        self.boton_ventas_totales_diarias.setText(_translate("MainWindow", "Ventas diarias"))
        self.boton_ventas_totales_mensuales.setText(_translate("MainWindow", "Ventas mensuales"))
        self.boton_ventas_totales_anuales.setText(_translate("MainWindow", "Ventas anuales"))
        self.boton_ventas_individuales.setText(_translate("MainWindow", "Ventas individuales"))
        self.boton_ventas_individuales_diarias.setText(_translate("MainWindow", "Ventas diarias"))
        self.boton_ventas_individuales_mensuales.setText(_translate("MainWindow", "Ventas mensuales"))
        self.boton_ventas_individuales_anuales.setText(_translate("MainWindow", "Ventas anuales"))
        self.boton_empleados.setText(_translate("MainWindow", "Empleados"))
        self.boton_agregar_usuario.setText(_translate("MainWindow", "Agregar Usuario"))
        self.boton_editar_usuario.setText(_translate("MainWindow", "Editar Usuario"))
        self.boton_meta_ventas.setText(_translate("MainWindow", "Meta de ventas"))
        self.boton_importar_datos.setText(_translate("MainWindow", "Importar datos"))
        self.boton_cerrar_sesion.setText(_translate("MainWindow", "Cerrar sesión"))
        self.label.setText(_translate("MainWindow", "BIENVENIDO A LA APLICACIÓN DE GESTIÓN"))
        self.label_45.setText(_translate("MainWindow", "DE ESTADÍSTICAS DE"))
        self.label_3.setText(_translate("MainWindow", "CAFÉ INDIGO"))
        self.label_tipo_usuario_ventas_totales_diarias.setText(_translate("MainWindow", "TIPO DE USUARIO"))
        self.fecha_seleccionada_ventas_totales_diarias.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.boton_generar_ventas_totales_diarias.setText(_translate("MainWindow", "Generar"))
        self.label_5.setText(_translate("MainWindow", "Porcentaje de ventas al dia:"))
        self.label_porcentaje_ventas_totales_diarias.setText(_translate("MainWindow", "--.--%"))
        self.label_8.setText(_translate("MainWindow", "Hora con más ventas:"))
        self.label_hora_mas_ventas_totales_diarias.setText(_translate("MainWindow", "--:-- pm/am - --:-- pm/am"))
        self.label_12.setText(_translate("MainWindow", "Hora con menos ventas:"))
        self.label_hora_menos_ventas_totales_diarias.setText(_translate("MainWindow", "--:-- pm/am - --:-- pm/am"))
        self.label_14.setText(_translate("MainWindow", "VENTAS TOTALES DE CAFÉ"))
        self.label_17.setText(_translate("MainWindow", "INDIGO POR DÍA:"))
        self.label_dia_ventas_totales_diarias.setText(_translate("MainWindow", "--/--/--"))
        item = self.tabla_ventas_totales_diarias.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hora"))
        item = self.tabla_ventas_totales_diarias.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ingresos totales"))
        self.label_15.setText(_translate("MainWindow", "Total:"))
        self.label_total_ventas_totales_diarias.setText(_translate("MainWindow", "$--.--"))
        self.label_tipo_usuario_ventas_totales_mensuales.setText(_translate("MainWindow", "TIPO DE USUARIO"))
        self.boton_generar_ventas_totales_mensuales.setText(_translate("MainWindow", "Generar"))
        self.label_21.setText(_translate("MainWindow", "Mes con más ventas:"))
        self.label_mes_mas_ventas_totales_mensuales.setText(_translate("MainWindow", "----"))
        self.label_23.setText(_translate("MainWindow", "Mes con menos ventas:"))
        self.label_mes_menos_ventas_totales_mensuales.setText(_translate("MainWindow", "----"))
        self.label_24.setText(_translate("MainWindow", "VENTAS TOTALES DE CAFÉ"))
        self.label_25.setText(_translate("MainWindow", "INDIGO POR MES:"))
        self.label_mes_ventas_totales_mensuales.setText(_translate("MainWindow", "----"))
        item = self.tabla_ventas_totales_mensuales.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mes"))
        item = self.tabla_ventas_totales_mensuales.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ingresos totales"))
        item = self.tabla_ventas_totales_mensuales.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Porcentaje de ventas \npor mes"))
        self.label_26.setText(_translate("MainWindow", "Total:"))
        self.label_total_ventas_totales_mensuales.setText(_translate("MainWindow", "$--.--"))
        self.label_tipo_usuario_ventas_totales_anuales.setText(_translate("MainWindow", "TIPO DE USUARIO"))
        self.label_34.setText(_translate("MainWindow", "Año con más ventas:"))
        self.label_anio_mas_ventas_totales_anuales.setText(_translate("MainWindow", "----"))
        self.label_41.setText(_translate("MainWindow", "Año con menos ventas:"))
        self.label_anio_menos_ventas_totales_anuales.setText(_translate("MainWindow", "----"))
        self.label_42.setText(_translate("MainWindow", "VENTAS TOTALES ANUALES"))
        self.label_43.setText(_translate("MainWindow", "DE CAFÉ INDIGO"))
        item = self.tabla_ventas_totales_anuales.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Año"))
        item = self.tabla_ventas_totales_anuales.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ingresos totales"))
        item = self.tabla_ventas_totales_anuales.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Porcentaje de ventas \npor año"))
        self.label_44.setText(_translate("MainWindow", "Total:"))
        self.label_total_ventas_totales_anuales.setText(_translate("MainWindow", "$--.--"))
        self.label_6.setText(_translate("MainWindow", "Fecha de año en curso:"))
        self.label_fecha_en_curso_ventas_totales_anuales.setText(_translate("MainWindow", "-- de -- del ----"))
        self.label_47.setText(_translate("MainWindow", "Ventas de año en curso:"))
        self.label_ventas_anio_en_curso_ventas_totales_anuales.setText(_translate("MainWindow", "$--.--"))
        self.label_49.setText(_translate("MainWindow", "Ventas totales incluyendo año en curso:"))
        self.label_ventas_totales_anio_actual_incluido_ventas_totales_anuales.setText(_translate("MainWindow", "$--.--"))
        self.label_tipo_usuario_ventas_individuales_diarias.setText(_translate("MainWindow", "TIPO DE USUARIO"))
        self.label_36.setText(_translate("MainWindow", "Ingresa número de empleado"))
        self.campo_num_empleado_ventas_individuales_diarias.setPlaceholderText(_translate("MainWindow", "Número empleado"))
        self.boton_buscar_ventas_individuales_diarias.setText(_translate("MainWindow", "Buscar"))
        self.label_37.setText(_translate("MainWindow", "Datos de empleado:"))
        self.label_4.setText(_translate("MainWindow", "Número de empleado ingresado:"))
        self.label_num_empleado_ventas_individuales_diarias.setText(_translate("MainWindow", "----"))
        self.label_27.setText(_translate("MainWindow", "Nombre:"))
        self.label_nombre_ventas_individuales_diarias.setText(_translate("MainWindow", "-------"))
        self.label_9.setText(_translate("MainWindow", "Estatus:"))
        self.label_estatus_ventas_individuales_diarias.setText(_translate("MainWindow", "------"))
        self.boton_generar_ventas_individuales_diarias.setText(_translate("MainWindow", "Generar"))
        self.label_31.setText(_translate("MainWindow", "Porcentaje de ventas al día:"))
        self.label_porcentaje_ventas_individuales_diarias.setText(_translate("MainWindow", "--.--%"))
        self.label_33.setText(_translate("MainWindow", "VENTAS DEL DÍA:"))
        self.label_dia_ventas_individuales_diarias.setText(_translate("MainWindow", "--/--/--"))
        item = self.tabla_ventas_individuales_diarias.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hora"))
        item = self.tabla_ventas_individuales_diarias.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ingresos"))
        self.label_38.setText(_translate("MainWindow", "Total:"))
        self.label_total_ventas_individuales_diarias.setText(_translate("MainWindow", "$--.--"))
        self.label_35.setText(_translate("MainWindow", "Hora con más ventas:"))
        self.label_hora_mas_ventas_individuales_diarias.setText(_translate("MainWindow", "--:-- pm - --:-- pm"))
        self.label_39.setText(_translate("MainWindow", "Hora con menos ventas:"))
        self.label_hora_menos_ventas_individuales_diarias.setText(_translate("MainWindow", "--:-- pm - --:-- pm"))
        self.label_tipo_usuario_ventas_individuales_mensuales.setText(_translate("MainWindow", "TIPO DE USUARIO"))
        self.label_46.setText(_translate("MainWindow", "Ingresa número de empleado"))
        self.campo_num_empleado_ventas_individuales_diarias_2.setPlaceholderText(_translate("MainWindow", "Número empleado"))
        self.boton_buscar_ventas_individuales_mensuales.setText(_translate("MainWindow", "Buscar"))
        self.label_48.setText(_translate("MainWindow", "Datos de empleado:"))
        self.label_50.setText(_translate("MainWindow", "Número de empleado ingresado:"))
        self.label_num_empleado_ventas_individuales_diarias_2.setText(_translate("MainWindow", "----"))
        self.label_51.setText(_translate("MainWindow", "Nombre:"))
        self.label_nombre_ventas_individuales_diarias_2.setText(_translate("MainWindow", "-------"))
        self.label_52.setText(_translate("MainWindow", "Estatus:"))
        self.label_estatus_ventas_individuales_diarias_2.setText(_translate("MainWindow", "------"))
        self.boton_generar_ventas_individuales_mensuales.setText(_translate("MainWindow", "Generar"))
        self.label_55.setText(_translate("MainWindow", "VENTAS MENSUALES:"))
        self.label_mes_ventas_individuales_mensuales.setText(_translate("MainWindow", "----"))
        item = self.tabla_ventas_individuales_mensuales.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mes"))
        item = self.tabla_ventas_individuales_mensuales.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ingresos"))
        item = self.tabla_ventas_individuales_mensuales.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Porcentaje de ventas \npor mes"))
        self.label_56.setText(_translate("MainWindow", "Total:"))
        self.label_total_ventas_individuales_diarias_2.setText(_translate("MainWindow", "$--.--"))
        self.label_58.setText(_translate("MainWindow", "Mes con mas ventas:"))
        self.label_hora_mas_ventas_individuales_diarias_4.setText(_translate("MainWindow", "            -----"))
        self.label_57.setText(_translate("MainWindow", "Mes con menos ventas:"))
        self.label_hora_mas_ventas_individuales_diarias_2.setText(_translate("MainWindow", "            -----"))
        self.label_tipo_usuario_ventas_individuales_anuales.setText(_translate("MainWindow", "TIPO DE USUARIO"))
        self.label_59.setText(_translate("MainWindow", "Ingresa número de empleado"))
        self.campo_num_empleado_ventas_individuales_anuales.setPlaceholderText(_translate("MainWindow", "Número empleado"))
        self.boton_buscar_ventas_individuales_anuales.setText(_translate("MainWindow", "Buscar"))
        self.label_60.setText(_translate("MainWindow", "Datos de empleado:"))
        self.label_61.setText(_translate("MainWindow", "Número de empleado ingresado:"))
        self.label_num_empleado_ventas_individuales_anuales.setText(_translate("MainWindow", "----"))
        self.label_62.setText(_translate("MainWindow", "Nombre:"))
        self.label_nombre_ventas_individuales_anuales.setText(_translate("MainWindow", "-------"))
        self.label_63.setText(_translate("MainWindow", "Estatus:"))
        self.label_estatus_ventas_individuales_anuales.setText(_translate("MainWindow", "------"))
        self.label_66.setText(_translate("MainWindow", "VENTAS ANUALES"))
        item = self.tabla_ventas_individuales_anuales.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Año"))
        item = self.tabla_ventas_individuales_anuales.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ingresos totales"))
        item = self.tabla_ventas_individuales_anuales.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Porcentaje de ventas \npor año"))
        self.label_67.setText(_translate("MainWindow", "Total:"))
        self.label_total_ventas_individuales_anuales.setText(_translate("MainWindow", "$--.--"))
        self.label_68.setText(_translate("MainWindow", "Año con mas ventas:"))
        self.label_anio_mas_ventas_individuales_anuales.setText(_translate("MainWindow", "----"))
        self.label_69.setText(_translate("MainWindow", "Año con menos ventas:"))
        self.label_anio_menos_ventas_individuales_anuales.setText(_translate("MainWindow", "----"))
        self.label_76.setText(_translate("MainWindow", "Fecha del año en curso"))
        self.label_fecha_en_curso_ventas_individuales_anuales.setText(_translate("MainWindow", "-- de ----- del ----"))
        self.label_77.setText(_translate("MainWindow", "Ventas de año en curso"))
        self.label_ventas_anio_en_curso_ventas_individuales_anuales.setText(_translate("MainWindow", "$--.--"))
        self.label_78.setText(_translate("MainWindow", "Ventas totales incluyendo año en curso:"))
        self.label_ventas_totales_anio_actual_incluido_ventas_individuales_anuales.setText(_translate("MainWindow", "$--.--"))
        self.label_tipo_usuario_empleados.setText(_translate("MainWindow", "TIPO DE USUARIO"))
        self.campo_nombre_empleado_empleados.setPlaceholderText(_translate("MainWindow", "Nombre de empleado"))
        self.boton_buscar_empleados.setText(_translate("MainWindow", "Buscar"))
        self.label_13.setText(_translate("MainWindow", "EMPLEADOS DE CAFÉ INDIGO"))
        item = self.tabla_empleados.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tabla_empleados.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Numero Empleado"))
        item = self.tabla_empleados.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tipo de empleado"))
        item = self.tabla_empleados.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Estatus"))
        self.label_tipo_usuario_importar_datos.setText(_translate("MainWindow", "TIPO DE USUARIO"))
        self.label_70.setText(_translate("MainWindow", "IMPORTAR DATOS"))
        self.label_79.setText(_translate("MainWindow", "Selecciona el archivo Excel de ventas"))
        self.boton_ayuda_archivo_ventas.setToolTip(_translate("MainWindow", "Formato del archivo de ventas"))
        self.boton_ayuda_archivo_ventas.setText(_translate("MainWindow", "?"))
        self.boton_subir_archivo.setText(_translate("MainWindow", "Subir"))
        item = self.tabla_eliminar_registros_de_archivos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre de archivo"))
        item = self.tabla_eliminar_registros_de_archivos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Fecha"))
        self.label_tipo_usuario_agregar_usuario.setText(_translate("MainWindow", "TIPO DE USUARIO"))
        self.label_80.setText(_translate("MainWindow", "AGREGAR USUARIO A CAFÉ INDIGO"))
        self.campo_apellido_paterno_agregar.setPlaceholderText(_translate("MainWindow", "Apellido Paterno"))
        self.campo_nombre_empleado_agregar.setPlaceholderText(_translate("MainWindow", "Nombre de empleado"))
        self.campo_apellido_materno_agregar.setPlaceholderText(_translate("MainWindow", "Apellido Materno"))
        self.campo_numero_telefono_agregar.setPlaceholderText(_translate("MainWindow", "Número de télefono"))
        self.campo_contrasena_empleado_agregar.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.campo_correo_empleado_agregar.setPlaceholderText(_translate("MainWindow", "Correo"))
        self.frame_112.setToolTip(_translate("MainWindow", "Tipo de empleado"))
        self.comboBox_tipo_empleado_agregar.setProperty("placeholderText", _translate("MainWindow", "Tipo de empleado"))
        self.comboBox_tipo_empleado_agregar.setItemText(0, _translate("MainWindow", "empleado"))
        self.comboBox_tipo_empleado_agregar.setItemText(1, _translate("MainWindow", "gerente"))
        self.comboBox_tipo_empleado_agregar.setItemText(2, _translate("MainWindow", "administrador"))
        self.frame_113.setToolTip(_translate("MainWindow", "Estatus"))
        self.comboBox_estatus_empleado_agregar.setCurrentText(_translate("MainWindow", "activo"))
        self.comboBox_estatus_empleado_agregar.setProperty("placeholderText", _translate("MainWindow", "Estatus"))
        self.comboBox_estatus_empleado_agregar.setItemText(0, _translate("MainWindow", "activo"))
        self.comboBox_estatus_empleado_agregar.setItemText(1, _translate("MainWindow", "inactivo"))
        self.boton_agregar_empleado_agregar.setText(_translate("MainWindow", "AGREGAR "))
        self.label_83.setText(_translate("MainWindow", "Numero de empleado:"))
        self.label_tipo_usuario_editar_usuario.setText(_translate("MainWindow", "TIPO DE USUARIO"))
        self.label_81.setText(_translate("MainWindow", "EDITAR USUARIO DE"))
        self.label_84.setText(_translate("MainWindow", "CAFÉ INDIGO"))
        self.label_85.setText(_translate("MainWindow", "Ingresa número de empleado por editar"))
        self.campo_busca_numero_empleado_editar.setPlaceholderText(_translate("MainWindow", "Número de empleado"))
        self.boton_buscar_empleados_editar.setText(_translate("MainWindow", "Buscar"))
        self.campo_apellido_paterno_editar.setPlaceholderText(_translate("MainWindow", "Apellido Paterno"))
        self.campo_nombre_empleado_editar.setPlaceholderText(_translate("MainWindow", "Nombre de empleado"))
        self.campo_apellido_materno_editar.setPlaceholderText(_translate("MainWindow", "Apellido Materno"))
        self.campo_numero_telefono_editar.setPlaceholderText(_translate("MainWindow", "Número de télefono"))
        self.campo_contrasena_empleado_editar.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.campo_correo_empleado_editar.setPlaceholderText(_translate("MainWindow", "Correo"))
        self.comboBox_tipo_empleado_editar.setProperty("placeholderText", _translate("MainWindow", "Tipo de empleado"))
        self.comboBox_tipo_empleado_editar.setItemText(0, _translate("MainWindow", "empleado"))
        self.comboBox_tipo_empleado_editar.setItemText(1, _translate("MainWindow", "gerente"))
        self.comboBox_tipo_empleado_editar.setItemText(2, _translate("MainWindow", "administrador"))
        self.comboBox_estatus_empleado_editar.setProperty("placeholderText", _translate("MainWindow", "Estatus"))
        self.comboBox_estatus_empleado_editar.setItemText(0, _translate("MainWindow", "activo"))
        self.comboBox_estatus_empleado_editar.setItemText(1, _translate("MainWindow", "inactivo"))
        self.boton_guardar_empleados_editar.setText(_translate("MainWindow", "GUARDAR"))
        self.label_82.setText(_translate("MainWindow", "Número de empleado:"))
        self.label_tipo_usuario_meta_ventas.setText(_translate("MainWindow", "TIPO DE USUARIO"))
        self.label_86.setText(_translate("MainWindow", "META DE VENTAS"))
        self.label_87.setText(_translate("MainWindow", "Ingresa el total de pesos ($MXN) esperados por ganar en un día por empleado"))
        self.campo_meta_diaria_por_empleado.setPlaceholderText(_translate("MainWindow", "$MXN"))
        self.boton_guardar_meta_ventas.setText(_translate("MainWindow", "GUARDAR"))
        self.label_88.setText(_translate("MainWindow", "Ganancias esperadas por empleado"))
        self.label_89.setText(_translate("MainWindow", "Al día:"))
        self.label_meta_diaria_empleado.setText(_translate("MainWindow", "$--.--"))
        self.label_91.setText(_translate("MainWindow", "Al mes:"))
        self.label_meta_mensual_empleado.setText(_translate("MainWindow", "$--.--"))
        self.label_92.setText(_translate("MainWindow", "Al año:"))
        self.label_meta_anual_empleado.setText(_translate("MainWindow", "$--.--"))
        self.label_90.setText(_translate("MainWindow", "Ganancias esperadas totales"))
        self.label_96.setText(_translate("MainWindow", "Al día:"))
        self.label_meta_diaria_total.setText(_translate("MainWindow", "$--.--"))
        self.label_98.setText(_translate("MainWindow", "Al mes:"))
        self.label_meta_mensual_total.setText(_translate("MainWindow", "$--.--"))
        self.label_100.setText(_translate("MainWindow", "Al año:"))
        self.label_meta_anual_total.setText(_translate("MainWindow", "$--.--"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

