# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from controlador_base_datos import verifica_login
from ventas import MainWindow

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/img/icono_cafe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.widget.setStyleSheet("border-radius: 10px;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.label.setPixmap(QtGui.QPixmap("resources/img/login-background.png"))
        self.label.setScaledContents(True)
        self.label.setText("")
        self.label.setObjectName("label")
        self.campo_num_emp_login = QtWidgets.QLineEdit(self.widget)
        self.campo_num_emp_login.setGeometry(QtCore.QRect(55, 280, 280, 40))
        self.campo_num_emp_login.setStyleSheet("QLineEdit{\n"
"Padding-left:10px;\n"
"Padding-right:10px;\n"
"}")
        self.campo_num_emp_login.setText("")
        self.campo_num_emp_login.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.campo_num_emp_login.setObjectName("campo_num_emp_login")
        self.campo_contrasenia_login = QtWidgets.QLineEdit(self.widget)
        self.campo_contrasenia_login.setGeometry(QtCore.QRect(55, 350, 280, 40))
        self.campo_contrasenia_login.setStyleSheet("QLineEdit{\n"
"border-radius: 10px;\n"
"Padding-left:10px;\n"
"Padding-right:10px;\n"
"}")
        self.campo_contrasenia_login.setText("")
        self.campo_contrasenia_login.setEchoMode(QtWidgets.QLineEdit.Password)
        self.campo_contrasenia_login.setObjectName("campo_contrasenia_login")
        self.boton_ingresar_login = QtWidgets.QPushButton(self.widget)
        self.boton_ingresar_login.setGeometry(QtCore.QRect(100, 425, 180, 35))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.boton_ingresar_login.setFont(font)
        self.boton_ingresar_login.setStyleSheet("QPushButton#boton_ingresar_login{\n"
"    border-radius: 10px;\n"
"    border: 2px solid #FFFFFF;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton#boton_ingresar_login:pressed{\n"
"    background-color: #FFFFFF;\n"
"    color: #005db1;\n"
"}")
        self.boton_ingresar_login.setObjectName("boton_ingresar_login")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.boton_ingresar_login.clicked.connect(lambda: self.loggedin(Form))

    def loggedin(self,Form):
        if verifica_login(self.campo_num_emp_login.text(), self.campo_contrasenia_login.text()) == True:
            Form.close()
            window = MainWindow()
            window.show()



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.campo_num_emp_login.setPlaceholderText(_translate("Form", "Número de empleado"))
        self.campo_contrasenia_login.setPlaceholderText(_translate("Form", "Contraseña"))
        self.boton_ingresar_login.setText(_translate("Form", "Ingresar"))

if __name__ == "__main__":
    print("Este archivo no se ejecuta directamente")