import sys
from ventas import MainWindow
from login import Ui_Form
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    # comprueba que los datos de inicio de sesión sean correctos en la base de datos
    # si es así, abre la ventana principal

    if ui.boton_ingresar_login.clicked:
        ui = MainWindow()
        ui.show()
    
    sys.exit(app.exec_())