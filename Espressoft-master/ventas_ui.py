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
        MainWindow.resize(973, 627)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/img/icono_desplegable.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_ventas_totales_desplegable.setIcon(icon)
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
        self.boton_ventas_individuales_desplegable.setIcon(icon)
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
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(0, -1, 4, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.boton_cerrar = QtWidgets.QPushButton(self.menu_lateral)
        self.boton_cerrar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.boton_cerrar.setAutoFillBackground(False)
        self.boton_cerrar.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 16px;\n"
"    border: none;\n"
"    padding: 10px;\n"
"}")
        self.boton_cerrar.setObjectName("boton_cerrar")
        self.horizontalLayout_6.addWidget(self.boton_cerrar)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem15)
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
        self.pagina_por_defecto.setObjectName("pagina_por_defecto")
        self.label = QtWidgets.QLabel(self.pagina_por_defecto)
        self.label.setGeometry(QtCore.QRect(140, 230, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.pagina_por_defecto)
        self.label_2.setGeometry(QtCore.QRect(180, 330, 47, 13))
        self.label_2.setObjectName("label_2")
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
"    fo    nt-style: normal;\n"
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
"    fo    nt-style: normal;\n"
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
"    fo    nt-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_dia_ventas_totales_diarias.setWordWrap(True)
        self.label_dia_ventas_totales_diarias.setObjectName("label_dia_ventas_totales_diarias")
        self.verticalLayout_10.addWidget(self.label_dia_ventas_totales_diarias, 0, QtCore.Qt.AlignHCenter)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_16.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.tabla_ventas_totales_diarias = QtWidgets.QTableWidget(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabla_ventas_totales_diarias.sizePolicy().hasHeightForWidth())
        self.tabla_ventas_totales_diarias.setSizePolicy(sizePolicy)
        self.tabla_ventas_totales_diarias.setStyleSheet("QTableWidget::item {\n"
"    border-bottom: 1px solid #C8D0DB;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"    color: #000000;\n"
"}\n"
"\n"
"\n"
"")
        self.tabla_ventas_totales_diarias.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tabla_ventas_totales_diarias.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_ventas_totales_diarias.setProperty("showDropIndicator", False)
        self.tabla_ventas_totales_diarias.setDragDropOverwriteMode(False)
        self.tabla_ventas_totales_diarias.setAlternatingRowColors(False)
        self.tabla_ventas_totales_diarias.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tabla_ventas_totales_diarias.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabla_ventas_totales_diarias.setTextElideMode(QtCore.Qt.ElideRight)
        self.tabla_ventas_totales_diarias.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tabla_ventas_totales_diarias.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tabla_ventas_totales_diarias.setShowGrid(False)
        self.tabla_ventas_totales_diarias.setGridStyle(QtCore.Qt.NoPen)
        self.tabla_ventas_totales_diarias.setWordWrap(False)
        self.tabla_ventas_totales_diarias.setCornerButtonEnabled(False)
        self.tabla_ventas_totales_diarias.setObjectName("tabla_ventas_totales_diarias")
        self.tabla_ventas_totales_diarias.setColumnCount(2)
        self.tabla_ventas_totales_diarias.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_ventas_totales_diarias.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_ventas_totales_diarias.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_totales_diarias.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_totales_diarias.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tabla_ventas_totales_diarias.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_ventas_totales_diarias.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_ventas_totales_diarias.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_ventas_totales_diarias.setItem(1, 1, item)
        self.tabla_ventas_totales_diarias.horizontalHeader().setVisible(False)
        self.tabla_ventas_totales_diarias.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_ventas_totales_diarias.horizontalHeader().setHighlightSections(True)
        self.tabla_ventas_totales_diarias.horizontalHeader().setMinimumSectionSize(39)
        self.tabla_ventas_totales_diarias.horizontalHeader().setSortIndicatorShown(False)
        self.tabla_ventas_totales_diarias.horizontalHeader().setStretchLastSection(True)
        self.tabla_ventas_totales_diarias.verticalHeader().setVisible(False)
        self.tabla_ventas_totales_diarias.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_ventas_totales_diarias.verticalHeader().setHighlightSections(False)
        self.tabla_ventas_totales_diarias.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_16.addWidget(self.tabla_ventas_totales_diarias)
        self.verticalLayout_10.addWidget(self.frame_8)
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
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem16)
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
        self.combobox_ventas_totales_mensuales.addItem("")
        self.combobox_ventas_totales_mensuales.addItem("")
        self.combobox_ventas_totales_mensuales.addItem("")
        self.combobox_ventas_totales_mensuales.addItem("")
        self.combobox_ventas_totales_mensuales.addItem("")
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
        self.frame_15 = QtWidgets.QFrame(self.frame_13)
        self.frame_15.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_18 = QtWidgets.QLabel(self.frame_15)
        self.label_18.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 18px;\n"
"}")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_17.addWidget(self.label_18)
        self.label_porcentaje_ventas_totales_mensuales = QtWidgets.QLabel(self.frame_15)
        self.label_porcentaje_ventas_totales_mensuales.setStyleSheet("QLabel {\n"
"    color: #000000;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}")
        self.label_porcentaje_ventas_totales_mensuales.setObjectName("label_porcentaje_ventas_totales_mensuales")
        self.verticalLayout_17.addWidget(self.label_porcentaje_ventas_totales_mensuales)
        self.horizontalLayout_23.addLayout(self.verticalLayout_17)
        self.label_19 = QtWidgets.QLabel(self.frame_15)
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("resources/img/icono_estadistica.png"))
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_23.addWidget(self.label_19, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_22.addLayout(self.horizontalLayout_23)
        self.verticalLayout_15.addWidget(self.frame_15)
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
"    fo    nt-style: normal;\n"
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
"    fo    nt-style: normal;\n"
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
"    fo    nt-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_mes_ventas_totales_mensuales.setWordWrap(True)
        self.label_mes_ventas_totales_mensuales.setObjectName("label_mes_ventas_totales_mensuales")
        self.verticalLayout_20.addWidget(self.label_mes_ventas_totales_mensuales, 0, QtCore.Qt.AlignHCenter)
        self.frame_19 = QtWidgets.QFrame(self.frame_18)
        self.frame_19.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_28.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_28.setSpacing(6)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.tabla_ventas_totales_mensuales = QtWidgets.QTableWidget(self.frame_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabla_ventas_totales_mensuales.sizePolicy().hasHeightForWidth())
        self.tabla_ventas_totales_mensuales.setSizePolicy(sizePolicy)
        self.tabla_ventas_totales_mensuales.setStyleSheet("QTableWidget::item {\n"
"    border-bottom: 1px solid #C8D0DB;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"    color: #000000;\n"
"}\n"
"\n"
"\n"
"")
        self.tabla_ventas_totales_mensuales.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tabla_ventas_totales_mensuales.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_ventas_totales_mensuales.setProperty("showDropIndicator", False)
        self.tabla_ventas_totales_mensuales.setDragDropOverwriteMode(False)
        self.tabla_ventas_totales_mensuales.setAlternatingRowColors(False)
        self.tabla_ventas_totales_mensuales.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tabla_ventas_totales_mensuales.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabla_ventas_totales_mensuales.setTextElideMode(QtCore.Qt.ElideRight)
        self.tabla_ventas_totales_mensuales.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tabla_ventas_totales_mensuales.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tabla_ventas_totales_mensuales.setShowGrid(False)
        self.tabla_ventas_totales_mensuales.setGridStyle(QtCore.Qt.NoPen)
        self.tabla_ventas_totales_mensuales.setWordWrap(False)
        self.tabla_ventas_totales_mensuales.setCornerButtonEnabled(False)
        self.tabla_ventas_totales_mensuales.setObjectName("tabla_ventas_totales_mensuales")
        self.tabla_ventas_totales_mensuales.setColumnCount(2)
        self.tabla_ventas_totales_mensuales.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_ventas_totales_mensuales.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_ventas_totales_mensuales.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_totales_mensuales.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
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
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tabla_ventas_totales_mensuales.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_ventas_totales_mensuales.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_ventas_totales_mensuales.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_ventas_totales_mensuales.setItem(1, 1, item)
        self.tabla_ventas_totales_mensuales.horizontalHeader().setVisible(False)
        self.tabla_ventas_totales_mensuales.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_ventas_totales_mensuales.horizontalHeader().setHighlightSections(True)
        self.tabla_ventas_totales_mensuales.horizontalHeader().setMinimumSectionSize(39)
        self.tabla_ventas_totales_mensuales.horizontalHeader().setSortIndicatorShown(False)
        self.tabla_ventas_totales_mensuales.horizontalHeader().setStretchLastSection(True)
        self.tabla_ventas_totales_mensuales.verticalHeader().setVisible(False)
        self.tabla_ventas_totales_mensuales.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_ventas_totales_mensuales.verticalHeader().setHighlightSections(False)
        self.tabla_ventas_totales_mensuales.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_28.addWidget(self.tabla_ventas_totales_mensuales)
        self.verticalLayout_20.addWidget(self.frame_19)
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
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem17)
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
        self.frame_39 = QtWidgets.QFrame(self.frame_37)
        self.frame_39.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout(self.frame_39)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout()
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.label_28 = QtWidgets.QLabel(self.frame_39)
        self.label_28.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    font-size: 18px;\n"
"}")
        self.label_28.setObjectName("label_28")
        self.verticalLayout_36.addWidget(self.label_28)
        self.label_porcentaje_ventas_totales_anuales = QtWidgets.QLabel(self.frame_39)
        self.label_porcentaje_ventas_totales_anuales.setStyleSheet("QLabel {\n"
"    color: #000000;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"}")
        self.label_porcentaje_ventas_totales_anuales.setObjectName("label_porcentaje_ventas_totales_anuales")
        self.verticalLayout_36.addWidget(self.label_porcentaje_ventas_totales_anuales)
        self.horizontalLayout_52.addLayout(self.verticalLayout_36)
        self.label_29 = QtWidgets.QLabel(self.frame_39)
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap("resources/img/icono_estadistica.png"))
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_52.addWidget(self.label_29, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_51.addLayout(self.horizontalLayout_52)
        self.verticalLayout_34.addWidget(self.frame_39)
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
"    fo    nt-style: normal;\n"
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
"    fo    nt-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_43.setWordWrap(True)
        self.label_43.setObjectName("label_43")
        self.verticalLayout_39.addWidget(self.label_43, 0, QtCore.Qt.AlignHCenter)
        self.frame_43 = QtWidgets.QFrame(self.frame_42)
        self.frame_43.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout(self.frame_43)
        self.horizontalLayout_57.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_57.setSpacing(6)
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.tabla_ventas_totales_anuales = QtWidgets.QTableWidget(self.frame_43)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabla_ventas_totales_anuales.sizePolicy().hasHeightForWidth())
        self.tabla_ventas_totales_anuales.setSizePolicy(sizePolicy)
        self.tabla_ventas_totales_anuales.setStyleSheet("QTableWidget::item {\n"
"    border-bottom: 1px solid #C8D0DB;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"    color: #000000;\n"
"}\n"
"\n"
"\n"
"")
        self.tabla_ventas_totales_anuales.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tabla_ventas_totales_anuales.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_ventas_totales_anuales.setProperty("showDropIndicator", False)
        self.tabla_ventas_totales_anuales.setDragDropOverwriteMode(False)
        self.tabla_ventas_totales_anuales.setAlternatingRowColors(False)
        self.tabla_ventas_totales_anuales.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tabla_ventas_totales_anuales.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabla_ventas_totales_anuales.setTextElideMode(QtCore.Qt.ElideRight)
        self.tabla_ventas_totales_anuales.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tabla_ventas_totales_anuales.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tabla_ventas_totales_anuales.setShowGrid(False)
        self.tabla_ventas_totales_anuales.setGridStyle(QtCore.Qt.NoPen)
        self.tabla_ventas_totales_anuales.setWordWrap(False)
        self.tabla_ventas_totales_anuales.setCornerButtonEnabled(False)
        self.tabla_ventas_totales_anuales.setObjectName("tabla_ventas_totales_anuales")
        self.tabla_ventas_totales_anuales.setColumnCount(2)
        self.tabla_ventas_totales_anuales.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_ventas_totales_anuales.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_ventas_totales_anuales.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_totales_anuales.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
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
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tabla_ventas_totales_anuales.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_ventas_totales_anuales.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_ventas_totales_anuales.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_ventas_totales_anuales.setItem(1, 1, item)
        self.tabla_ventas_totales_anuales.horizontalHeader().setVisible(False)
        self.tabla_ventas_totales_anuales.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_ventas_totales_anuales.horizontalHeader().setHighlightSections(True)
        self.tabla_ventas_totales_anuales.horizontalHeader().setMinimumSectionSize(39)
        self.tabla_ventas_totales_anuales.horizontalHeader().setSortIndicatorShown(False)
        self.tabla_ventas_totales_anuales.horizontalHeader().setStretchLastSection(True)
        self.tabla_ventas_totales_anuales.verticalHeader().setVisible(False)
        self.tabla_ventas_totales_anuales.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_ventas_totales_anuales.verticalHeader().setHighlightSections(False)
        self.tabla_ventas_totales_anuales.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_57.addWidget(self.tabla_ventas_totales_anuales)
        self.verticalLayout_39.addWidget(self.frame_43)
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
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_59.addItem(spacerItem18)
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
        self.label_fecha_anio_en_curso_ventas_totales_anuales = QtWidgets.QLabel(self.frame_45)
        self.label_fecha_anio_en_curso_ventas_totales_anuales.setStyleSheet("QLabel {\n"
"    color: #416BBF;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 13px;\n"
"}")
        self.label_fecha_anio_en_curso_ventas_totales_anuales.setObjectName("label_fecha_anio_en_curso_ventas_totales_anuales")
        self.verticalLayout_41.addWidget(self.label_fecha_anio_en_curso_ventas_totales_anuales, 0, QtCore.Qt.AlignHCenter)
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
"    font-size: 13px;\n"
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
        self.label_ventas_totales_incluyendo_anio_en_curso_ventas_totales_anuales = QtWidgets.QLabel(self.frame_46)
        self.label_ventas_totales_incluyendo_anio_en_curso_ventas_totales_anuales.setStyleSheet("QLabel {\n"
"    color: #344050;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 700;\n"
"    font-size: 12px;\n"
"}")
        self.label_ventas_totales_incluyendo_anio_en_curso_ventas_totales_anuales.setObjectName("label_ventas_totales_incluyendo_anio_en_curso_ventas_totales_anuales")
        self.horizontalLayout_50.addWidget(self.label_ventas_totales_incluyendo_anio_en_curso_ventas_totales_anuales, 0, QtCore.Qt.AlignRight)
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
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem19)
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
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem20)
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
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem21)
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
"    fo    nt-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_33.setWordWrap(False)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_46.addWidget(self.label_33)
        self.label_dia_ventas_individuales_diarias = QtWidgets.QLabel(self.frame_28)
        self.label_dia_ventas_individuales_diarias.setStyleSheet("QLabel {\n"
"    color: #416BBF;    \n"
"    font-family: \'Montserrat\';\n"
"    fo    nt-style: normal;\n"
"    font-weight: 800;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"}")
        self.label_dia_ventas_individuales_diarias.setObjectName("label_dia_ventas_individuales_diarias")
        self.horizontalLayout_46.addWidget(self.label_dia_ventas_individuales_diarias)
        self.verticalLayout_24.addLayout(self.horizontalLayout_46)
        self.frame_29 = QtWidgets.QFrame(self.frame_28)
        self.frame_29.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_40.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_40.setSpacing(6)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.tabla_ventas_individuales_diarias = QtWidgets.QTableWidget(self.frame_29)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabla_ventas_individuales_diarias.sizePolicy().hasHeightForWidth())
        self.tabla_ventas_individuales_diarias.setSizePolicy(sizePolicy)
        self.tabla_ventas_individuales_diarias.setStyleSheet("QTableWidget::item {\n"
"    border-bottom: 1px solid #C8D0DB;\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: 600;\n"
"    color: #000000;\n"
"}\n"
"\n"
"\n"
"")
        self.tabla_ventas_individuales_diarias.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tabla_ventas_individuales_diarias.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_ventas_individuales_diarias.setProperty("showDropIndicator", False)
        self.tabla_ventas_individuales_diarias.setDragDropOverwriteMode(False)
        self.tabla_ventas_individuales_diarias.setAlternatingRowColors(False)
        self.tabla_ventas_individuales_diarias.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tabla_ventas_individuales_diarias.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabla_ventas_individuales_diarias.setTextElideMode(QtCore.Qt.ElideRight)
        self.tabla_ventas_individuales_diarias.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tabla_ventas_individuales_diarias.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tabla_ventas_individuales_diarias.setShowGrid(False)
        self.tabla_ventas_individuales_diarias.setGridStyle(QtCore.Qt.NoPen)
        self.tabla_ventas_individuales_diarias.setWordWrap(False)
        self.tabla_ventas_individuales_diarias.setCornerButtonEnabled(False)
        self.tabla_ventas_individuales_diarias.setObjectName("tabla_ventas_individuales_diarias")
        self.tabla_ventas_individuales_diarias.setColumnCount(2)
        self.tabla_ventas_individuales_diarias.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_ventas_individuales_diarias.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_ventas_individuales_diarias.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_individuales_diarias.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        item.setFont(font)
        item.setBackground(QtGui.QColor(248, 250, 255))
        brush = QtGui.QBrush(QtGui.QColor(52, 64, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tabla_ventas_individuales_diarias.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tabla_ventas_individuales_diarias.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_ventas_individuales_diarias.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_ventas_individuales_diarias.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabla_ventas_individuales_diarias.setItem(1, 1, item)
        self.tabla_ventas_individuales_diarias.horizontalHeader().setVisible(False)
        self.tabla_ventas_individuales_diarias.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_ventas_individuales_diarias.horizontalHeader().setHighlightSections(True)
        self.tabla_ventas_individuales_diarias.horizontalHeader().setMinimumSectionSize(39)
        self.tabla_ventas_individuales_diarias.horizontalHeader().setSortIndicatorShown(False)
        self.tabla_ventas_individuales_diarias.horizontalHeader().setStretchLastSection(True)
        self.tabla_ventas_individuales_diarias.verticalHeader().setVisible(False)
        self.tabla_ventas_individuales_diarias.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_ventas_individuales_diarias.verticalHeader().setHighlightSections(False)
        self.tabla_ventas_individuales_diarias.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_40.addWidget(self.tabla_ventas_individuales_diarias)
        self.verticalLayout_24.addWidget(self.frame_29)
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
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_49.addItem(spacerItem22)
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
        self.label_13 = QtWidgets.QLabel(self.pagina_ventas_individuales_mensuales)
        self.label_13.setGeometry(QtCore.QRect(290, 280, 381, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.stacked_widget_paginas.addWidget(self.pagina_ventas_individuales_mensuales)
        self.pagina_ventas_individuales_anuales = QtWidgets.QWidget()
        self.pagina_ventas_individuales_anuales.setObjectName("pagina_ventas_individuales_anuales")
        self.label_16 = QtWidgets.QLabel(self.pagina_ventas_individuales_anuales)
        self.label_16.setGeometry(QtCore.QRect(190, 295, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.stacked_widget_paginas.addWidget(self.pagina_ventas_individuales_anuales)
        self.pagina_empleados = QtWidgets.QWidget()
        self.pagina_empleados.setObjectName("pagina_empleados")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.pagina_empleados)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 731, 621))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_63 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        self.frame_47 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.widget_5 = QtWidgets.QWidget(self.frame_47)
        self.widget_5.setGeometry(QtCore.QRect(10, 10, 334, 70))
        self.widget_5.setMinimumSize(QtCore.QSize(0, 70))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_35.setContentsMargins(0, 0, 9, 9)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.label_tipo_usuario_empleados = QtWidgets.QLabel(self.widget_5)
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
        self.verticalLayout_35.addWidget(self.label_tipo_usuario_empleados)
        self.frame_48 = QtWidgets.QFrame(self.widget_5)
        self.frame_48.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_48.setMaximumSize(QtCore.QSize(16777215, 4))
        self.frame_48.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;")
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.verticalLayout_35.addWidget(self.frame_48, 0, QtCore.Qt.AlignTop)
        self.layoutWidget = QtWidgets.QWidget(self.frame_47)
        self.layoutWidget.setGeometry(QtCore.QRect(400, 10, 291, 68))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_64 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_64.setContentsMargins(0, 9, 0, 9)
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")
        self.frame_49 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_49.setMinimumSize(QtCore.QSize(0, 50))
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
        self.horizontalLayout_64.addWidget(self.frame_49)
        self.boton_buscar_empleados = QtWidgets.QPushButton(self.layoutWidget)
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
        self.widget_6 = QtWidgets.QWidget(self.frame_47)
        self.widget_6.setGeometry(QtCore.QRect(40, 110, 651, 471))
        self.widget_6.setObjectName("widget_6")
        self.widget_7 = QtWidgets.QWidget(self.widget_6)
        self.widget_7.setGeometry(QtCore.QRect(150, 10, 351, 70))
        self.widget_7.setMinimumSize(QtCore.QSize(0, 70))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_40.setContentsMargins(0, 0, 9, 9)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.label_tipo_usuario_empleados_2 = QtWidgets.QLabel(self.widget_7)
        self.label_tipo_usuario_empleados_2.setMinimumSize(QtCore.QSize(0, 40))
        self.label_tipo_usuario_empleados_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_tipo_usuario_empleados_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_tipo_usuario_empleados_2.setStyleSheet("QLabel {\n"
"    color: rgb(0, 85, 255);\n"
"    font-family: \'Montserrat\';\n"
"    font-style: normal;\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"}")
        self.label_tipo_usuario_empleados_2.setObjectName("label_tipo_usuario_empleados_2")
        self.verticalLayout_40.addWidget(self.label_tipo_usuario_empleados_2)
        self.frame_50 = QtWidgets.QFrame(self.widget_7)
        self.frame_50.setMinimumSize(QtCore.QSize(0, 3))
        self.frame_50.setMaximumSize(QtCore.QSize(16777215, 4))
        self.frame_50.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"border-radius: 2px;")
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.verticalLayout_40.addWidget(self.frame_50, 0, QtCore.Qt.AlignTop)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget_6)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 80, 611, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.horizontalLayout_67 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_67.setObjectName("horizontalLayout_67")
        self.tabla_empleados = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tabla_empleados.setAutoFillBackground(True)
        self.tabla_empleados.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.tabla_empleados.setObjectName("tabla_empleados")
        self.tabla_empleados.setColumnCount(4)
        self.tabla_empleados.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_empleados.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_empleados.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_empleados.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_empleados.setHorizontalHeaderItem(3, item)
        self.tabla_empleados.horizontalHeader().setDefaultSectionSize(150)
        self.horizontalLayout_67.addWidget(self.tabla_empleados)
        self.verticalLayout_46.addLayout(self.horizontalLayout_67)
        self.horizontalLayout_63.addWidget(self.frame_47)
        self.stacked_widget_paginas.addWidget(self.pagina_empleados)
        self.verticalLayout.addWidget(self.stacked_widget_paginas)
        self.horizontalLayout.addWidget(self.frame_informacion)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stacked_widget_paginas.setCurrentIndex(7)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_ventas_totales.setText(_translate("MainWindow", "Ventas totales"))
        self.boton_ventas_totales_diarias.setText(_translate("MainWindow", "Ventas diarias"))
        self.boton_ventas_totales_mensuales.setText(_translate("MainWindow", "Ventas mensuales"))
        self.boton_ventas_totales_anuales.setText(_translate("MainWindow", "Ventas anuales"))
        self.boton_ventas_individuales.setText(_translate("MainWindow", "Ventas individuales"))
        self.boton_ventas_individuales_diarias.setText(_translate("MainWindow", "Ventas diarias"))
        self.boton_ventas_individuales_mensuales.setText(_translate("MainWindow", "Ventas mensuales"))
        self.boton_ventas_individuales_anuales.setText(_translate("MainWindow", "Ventas anuales"))
        self.boton_empleados.setText(_translate("MainWindow", "Empleados"))
        self.boton_cerrar.setText(_translate("MainWindow", "Cerrar"))
        self.label.setText(_translate("MainWindow", "Soy la pagina por defecto"))
        self.label_2.setText(_translate("MainWindow", "prueba"))
        self.label_tipo_usuario_ventas_totales_diarias.setText(_translate("MainWindow", "TIPO DE USUARIO"))
        self.fecha_seleccionada_ventas_totales_diarias.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.boton_generar_ventas_totales_diarias.setText(_translate("MainWindow", "Generar"))
        self.label_5.setText(_translate("MainWindow", "Porcentaje de ventas:"))
        self.label_porcentaje_ventas_totales_diarias.setText(_translate("MainWindow", "--.--%"))
        self.label_8.setText(_translate("MainWindow", "Hora con más ventas:"))
        self.label_hora_mas_ventas_totales_diarias.setText(_translate("MainWindow", "--:-- pm/am - --:-- pm/am"))
        self.label_12.setText(_translate("MainWindow", "Hora con menos ventas:"))
        self.label_hora_menos_ventas_totales_diarias.setText(_translate("MainWindow", "--:-- pm/am - --:-- pm/am"))
        self.label_14.setText(_translate("MainWindow", "VENTAS TOTALES DE CAFÉ"))
        self.label_17.setText(_translate("MainWindow", "INDIGO POR DÍA:"))
        self.label_dia_ventas_totales_diarias.setText(_translate("MainWindow", "--/--/--"))
        self.tabla_ventas_totales_diarias.setSortingEnabled(False)
        item = self.tabla_ventas_totales_diarias.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tabla_ventas_totales_diarias.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tabla_ventas_totales_diarias.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hora"))
        item = self.tabla_ventas_totales_diarias.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ingresos totales"))
        __sortingEnabled = self.tabla_ventas_totales_diarias.isSortingEnabled()
        self.tabla_ventas_totales_diarias.setSortingEnabled(False)
        item = self.tabla_ventas_totales_diarias.item(0, 0)
        item.setText(_translate("MainWindow", "10:00 am - 11:00 am"))
        item = self.tabla_ventas_totales_diarias.item(0, 1)
        item.setText(_translate("MainWindow", "$15000.00"))
        item = self.tabla_ventas_totales_diarias.item(1, 0)
        item.setText(_translate("MainWindow", "11:00 am - 12:00 pm"))
        item = self.tabla_ventas_totales_diarias.item(1, 1)
        item.setText(_translate("MainWindow", "$10000.00"))
        self.tabla_ventas_totales_diarias.setSortingEnabled(__sortingEnabled)
        self.label_15.setText(_translate("MainWindow", "Total:"))
        self.label_total_ventas_totales_diarias.setText(_translate("MainWindow", "$--.--"))
        self.label_tipo_usuario_ventas_totales_mensuales.setText(_translate("MainWindow", "TIPO DE USUARIO"))
        self.combobox_ventas_totales_mensuales.setItemText(0, _translate("MainWindow", "2019"))
        self.combobox_ventas_totales_mensuales.setItemText(1, _translate("MainWindow", "2020"))
        self.combobox_ventas_totales_mensuales.setItemText(2, _translate("MainWindow", "2021"))
        self.combobox_ventas_totales_mensuales.setItemText(3, _translate("MainWindow", "2022"))
        self.combobox_ventas_totales_mensuales.setItemText(4, _translate("MainWindow", "2023"))
        self.boton_generar_ventas_totales_mensuales.setText(_translate("MainWindow", "Generar"))
        self.label_18.setText(_translate("MainWindow", "Porcentaje de ventas:"))
        self.label_porcentaje_ventas_totales_mensuales.setText(_translate("MainWindow", "--.--%"))
        self.label_21.setText(_translate("MainWindow", "Mes con más ventas:"))
        self.label_mes_mas_ventas_totales_mensuales.setText(_translate("MainWindow", "----"))
        self.label_23.setText(_translate("MainWindow", "Mes con menos ventas:"))
        self.label_mes_menos_ventas_totales_mensuales.setText(_translate("MainWindow", "----"))
        self.label_24.setText(_translate("MainWindow", "VENTAS TOTALES DE CAFÉ"))
        self.label_25.setText(_translate("MainWindow", "INDIGO POR MES:"))
        self.label_mes_ventas_totales_mensuales.setText(_translate("MainWindow", "----"))
        self.tabla_ventas_totales_mensuales.setSortingEnabled(False)
        item = self.tabla_ventas_totales_mensuales.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tabla_ventas_totales_mensuales.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tabla_ventas_totales_mensuales.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hora"))
        item = self.tabla_ventas_totales_mensuales.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ingresos totales"))
        __sortingEnabled = self.tabla_ventas_totales_mensuales.isSortingEnabled()
        self.tabla_ventas_totales_mensuales.setSortingEnabled(False)
        item = self.tabla_ventas_totales_mensuales.item(0, 0)
        item.setText(_translate("MainWindow", "10:00 am - 11:00 am"))
        item = self.tabla_ventas_totales_mensuales.item(0, 1)
        item.setText(_translate("MainWindow", "$15000.00"))
        item = self.tabla_ventas_totales_mensuales.item(1, 0)
        item.setText(_translate("MainWindow", "11:00 am - 12:00 pm"))
        item = self.tabla_ventas_totales_mensuales.item(1, 1)
        item.setText(_translate("MainWindow", "$10000.00"))
        self.tabla_ventas_totales_mensuales.setSortingEnabled(__sortingEnabled)
        self.label_26.setText(_translate("MainWindow", "Total:"))
        self.label_total_ventas_totales_mensuales.setText(_translate("MainWindow", "$--.--"))
        self.label_tipo_usuario_ventas_totales_anuales.setText(_translate("MainWindow", "TIPO DE USUARIO"))
        self.label_28.setText(_translate("MainWindow", "Porcentaje de ventas:"))
        self.label_porcentaje_ventas_totales_anuales.setText(_translate("MainWindow", "--.--%"))
        self.label_34.setText(_translate("MainWindow", "Año con más ventas:"))
        self.label_anio_mas_ventas_totales_anuales.setText(_translate("MainWindow", "----"))
        self.label_41.setText(_translate("MainWindow", "Año con menos ventas:"))
        self.label_anio_menos_ventas_totales_anuales.setText(_translate("MainWindow", "----"))
        self.label_42.setText(_translate("MainWindow", "VENTAS TOTALES ANUALES"))
        self.label_43.setText(_translate("MainWindow", "DE CAFÉ INDIGO"))
        self.tabla_ventas_totales_anuales.setSortingEnabled(False)
        item = self.tabla_ventas_totales_anuales.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tabla_ventas_totales_anuales.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tabla_ventas_totales_anuales.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Año"))
        item = self.tabla_ventas_totales_anuales.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ingresos totales"))
        __sortingEnabled = self.tabla_ventas_totales_anuales.isSortingEnabled()
        self.tabla_ventas_totales_anuales.setSortingEnabled(False)
        item = self.tabla_ventas_totales_anuales.item(0, 0)
        item.setText(_translate("MainWindow", "2019"))
        item = self.tabla_ventas_totales_anuales.item(0, 1)
        item.setText(_translate("MainWindow", "$15000.00"))
        item = self.tabla_ventas_totales_anuales.item(1, 0)
        item.setText(_translate("MainWindow", "2020"))
        item = self.tabla_ventas_totales_anuales.item(1, 1)
        item.setText(_translate("MainWindow", "$10000.00"))
        self.tabla_ventas_totales_anuales.setSortingEnabled(__sortingEnabled)
        self.label_44.setText(_translate("MainWindow", "Total:"))
        self.label_total_ventas_totales_anuales.setText(_translate("MainWindow", "$--.--"))
        self.label_6.setText(_translate("MainWindow", "Fecha de año en curso:"))
        self.label_fecha_anio_en_curso_ventas_totales_anuales.setText(_translate("MainWindow", "-- de -- del ----"))
        self.label_47.setText(_translate("MainWindow", "Ventas de año en curso:"))
        self.label_ventas_anio_en_curso_ventas_totales_anuales.setText(_translate("MainWindow", "$--.--"))
        self.label_49.setText(_translate("MainWindow", "Ventas totales incluyendo año en curso:"))
        self.label_ventas_totales_incluyendo_anio_en_curso_ventas_totales_anuales.setText(_translate("MainWindow", "$--.--"))
        self.label_tipo_usuario_ventas_individuales_diarias.setText(_translate("MainWindow", "TIPO DE USUARIO"))
        self.label_36.setText(_translate("MainWindow", "Ingresa número de empleado"))
        self.campo_num_empleado_ventas_individuales_diarias.setPlaceholderText(_translate("MainWindow", "Número empleado"))
        self.boton_buscar_ventas_individuales_diarias.setText(_translate("MainWindow", "Búscar"))
        self.label_37.setText(_translate("MainWindow", "Datos de empleado:"))
        self.label_4.setText(_translate("MainWindow", "Número de empleado ingresado:"))
        self.label_num_empleado_ventas_individuales_diarias.setText(_translate("MainWindow", "----"))
        self.label_27.setText(_translate("MainWindow", "Nombre:"))
        self.label_nombre_ventas_individuales_diarias.setText(_translate("MainWindow", "-------"))
        self.label_9.setText(_translate("MainWindow", "Estatus:"))
        self.label_estatus_ventas_individuales_diarias.setText(_translate("MainWindow", "------"))
        self.boton_generar_ventas_individuales_diarias.setText(_translate("MainWindow", "Generar"))
        self.label_31.setText(_translate("MainWindow", "Porcentaje de ventas:"))
        self.label_porcentaje_ventas_individuales_diarias.setText(_translate("MainWindow", "--.--%"))
        self.label_33.setText(_translate("MainWindow", "VENTAS DEL DÍA:"))
        self.label_dia_ventas_individuales_diarias.setText(_translate("MainWindow", "--/--/--"))
        self.tabla_ventas_individuales_diarias.setSortingEnabled(False)
        item = self.tabla_ventas_individuales_diarias.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tabla_ventas_individuales_diarias.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tabla_ventas_individuales_diarias.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Hora"))
        item = self.tabla_ventas_individuales_diarias.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Ingresos"))
        __sortingEnabled = self.tabla_ventas_individuales_diarias.isSortingEnabled()
        self.tabla_ventas_individuales_diarias.setSortingEnabled(False)
        item = self.tabla_ventas_individuales_diarias.item(0, 0)
        item.setText(_translate("MainWindow", "3:00 pm - 4:00 pm"))
        item = self.tabla_ventas_individuales_diarias.item(0, 1)
        item.setText(_translate("MainWindow", "$450.00"))
        item = self.tabla_ventas_individuales_diarias.item(1, 0)
        item.setText(_translate("MainWindow", "4:00 pm - 5:00 pm"))
        item = self.tabla_ventas_individuales_diarias.item(1, 1)
        item.setText(_translate("MainWindow", "$300.00"))
        self.tabla_ventas_individuales_diarias.setSortingEnabled(__sortingEnabled)
        self.label_38.setText(_translate("MainWindow", "Total:"))
        self.label_total_ventas_individuales_diarias.setText(_translate("MainWindow", "$--.--"))
        self.label_35.setText(_translate("MainWindow", "Hora con más ventas:"))
        self.label_hora_mas_ventas_individuales_diarias.setText(_translate("MainWindow", "--:-- pm - --:-- pm"))
        self.label_39.setText(_translate("MainWindow", "Hora con menos ventas:"))
        self.label_hora_menos_ventas_individuales_diarias.setText(_translate("MainWindow", "--:-- pm - --:-- pm"))
        self.label_13.setText(_translate("MainWindow", "Soy la pagina ventas individuales mensuales"))
        self.label_16.setText(_translate("MainWindow", "Soy la pagina ventas individuales anuales"))
        self.label_tipo_usuario_empleados.setText(_translate("MainWindow", "TIPO DE USUARIO"))
        self.campo_nombre_empleado_empleados.setPlaceholderText(_translate("MainWindow", "Número empleado"))
        self.boton_buscar_empleados.setText(_translate("MainWindow", "Búscar"))
        self.label_tipo_usuario_empleados_2.setText(_translate("MainWindow", "EMPLEADOS DE CAFE INDIGO"))
        item = self.tabla_empleados.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tabla_empleados.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Numero Empleado"))
        item = self.tabla_empleados.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tipo de empleado"))
        item = self.tabla_empleados.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Estatus"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

