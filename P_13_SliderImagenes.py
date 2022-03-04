from QLabelClickeable import clickable

import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "P13_SliderImagenes.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.temporizador)

        self.valor = 0

        ##############################
        self.txt_imagen.setText("1")

        self.lista_imagenes = [":/Numeros/uno.png",
                               ":/Numeros/dos.png",
                               ":/Numeros/tres.png",
                               ":/Numeros/cuatro.png",
                               ":/Numeros/cinco.png"
                               ]

        self.lista_detallesPersona = [["Paco", "6", "Asesino"],
                                      ["Aquino", "7", "Velador"],
                                      ["Gerardo", "10", "Narco"],
                                      ["Miguel", "9", "Diller"],
                                      ["Clara", "11", "Cheff"]
                                      ]

        self.img.setPixmap(QtGui.QPixmap(self.lista_imagenes[0]))  # carga la primera imagen

        ##################################
        self.segundoPlano.start(1000)

    def temporizador(self):
        self.img.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.valor]))
        self.txt_imagen.setText(str(self.valor + 1))


        ############
        personaje = self.lista_detallesPersona[self.valor]

        self.txt_Nombre.setText(personaje[0])
        self.txt_Edad.setText(personaje[1])
        self.txt_Ocupacion.setText(personaje[2])
        ################


        self.valor += 1

        if self.valor == 5:
            self.valor = 0

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())