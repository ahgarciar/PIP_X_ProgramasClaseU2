from QLabelClickeable import clickable

import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "P9_TextoMultilinea.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #self.textEdit.setPlainText("Hola! \n como estas ?  :D! ")
        #self.textEdit.setHtml("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0BF09F;\">TextLabel</span></p></body></html>")

        self.btn_cargar.clicked.connect(self.cargar)

    def cargar(self):
        try:
            archivo = open("ListaNombres.txt")
            contenidoArchivo = archivo.readlines()
            #self.textEdit.setPlainText(str(contenidoArchivo))
            print(contenidoArchivo)
            auxiliar = ""
            for index in range(len(contenidoArchivo)):
                contenidoArchivo[index] = contenidoArchivo[index].replace("\n","")
                print(contenidoArchivo[index])
                auxiliar += contenidoArchivo[index] + "\n"
            self.textEdit.setPlainText(auxiliar)
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())