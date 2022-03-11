from QLabelClickeable import clickable

import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "P16_RadioButtonsCheckBox_v2.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.rb_carrera_isc.clicked.connect(self.isc)
        self.rb_carrera_ii.clicked.connect(self.ii)
        self.rb_carrera_ic.clicked.connect(self.ic)

        self.rb_universidad_unam.toggled.connect(self.unam)
        self.rb_universidad_tecm.toggled.connect(self.tecm)
        self.rb_universidad_uat.toggled.connect(self.uat)


        self.rb_carrera_isc.setChecked(True)

    #ejercicio abierto en el que se utilice checkbox y radiobuttons almenos una vés cada uno

    def isc(self):
        print("ISC", self.rb_carrera_isc.isChecked() )

    def ii(self):
        print("II", self.rb_carrera_ii.isChecked() )

    def ic(self):
        print("IC", self.rb_carrera_ic.isChecked() )

    def unam(self):
        print("UNAM", self.rb_universidad_unam.isChecked() )

    def tecm(self):
        print("TECNM", self.rb_universidad_tecm.isChecked() )

    def uat(self):
        print("UAT", self.rb_universidad_uat.isChecked() )

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())