from QLabelClickeable import clickable

import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "P8_CambioImagenes.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #self.img.clicked.connect(self.clicImage) #No se puede con labels
        clickable(self.img).connect(self.clicImage)

        self.btn_borrar.clicked.connect(self.borrar)


        ##############
        self.dial.setMinimum(0)
        self.dial.setMaximum(4)
        self.dial.setValue(0)
        self.dial.setSingleStep(1)
        self.dial.valueChanged.connect(self.cambioImg)
        ##############################
        self.txt_imagen.setText("1")

        self.lista_imagenes = [":/Numeros/uno.png",
                          ":/Numeros/dos.png",
                          ":/Numeros/tres.png",
                          ":/Numeros/cuatro.png",
                          ":/Numeros/cinco.png"
                          ]
        
        self.lista_detallesPersona = [["nombre", "edad","oficio"],
                                      ["nombre", "edad","oficio"],
                                      ["nombre", "edad","oficio"],
                                      ["nombre", "edad","oficio"],
                                      ["nombre", "edad","oficio"]
                                      ]

        self.img.setPixmap(QtGui.QPixmap(self.lista_imagenes[0])) #carga la primera imagen

    def cambioImg(self):
        valor = self.dial.value()

        self.img.setPixmap( QtGui.QPixmap(self.lista_imagenes[valor]) )

        self.txt_imagen.setText(str(valor+1))

    def clicImage(self):
        print("Hiciste clic")
        self.txt_Nombre.setText("Paco")
        self.txt_Edad.setText("6")
        self.txt_Ocupacion.setText("Asesino")

    def borrar(self):
        self.txt_Nombre.setText("")
        self.txt_Edad.setText("")
        self.txt_Ocupacion.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())