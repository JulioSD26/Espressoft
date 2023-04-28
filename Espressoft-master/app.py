import sys
from login import Ui_Form
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    app.exec_()

if __name__ == "__main__":
    main()