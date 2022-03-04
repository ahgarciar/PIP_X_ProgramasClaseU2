from QLabelClickeable import clickable

import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "P10_CatalogoPersonajes.ui"  # Nombre del archivo

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
            archivo = open("DescripcionPersonajes.csv")
            contenidoArchivo = archivo.readlines()
            #self.textEdit.setPlainText(str(contenidoArchivo))
            print(contenidoArchivo)


            listaProcesada = [ i.split("\t") for i in contenidoArchivo ] #Lista de Comprensión
            print(listaProcesada)

            auxiliar = ""
            for index in range(len(listaProcesada)):
                listaProcesada[index][0] = listaProcesada[index][0].replace("\n","")
                print(listaProcesada[index][0])
                auxiliar += listaProcesada[index][0] + "\n"
            self.textEdit.setPlainText(auxiliar)
        except Exception as ex:
            print(ex)

    #Investigacion. Listas de Comprensión
    #Investigación. Como trabajar con archivos en python (Escribir archivos ('w' y 'a'))
        # archivo = open("DescripcionPersonajes.csv",'w')
        # archivo = open("DescripcionPersonajes.csv",'a')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())