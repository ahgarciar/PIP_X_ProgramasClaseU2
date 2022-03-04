from QLabelClickeable import clickable

import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui

qtCreatorFile = "P11_Temporizador.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_iniciar.clicked.connect(self.iniciar)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.temporizador)

        self.valor = 0

    def iniciar(self):
        #pass   #pass      continue       break
        self.valor = int(self.txt_tiempo.text())
        self.txt_temporizador.setText(str(self.valor))
        print(self.valor)
        self.valor -= 1
        self.segundoPlano.start(1000)

    def temporizador(self):
        self.txt_temporizador.setText(str(self.valor))
        print(self.valor)
        self.valor -= 1

        if self.valor == -1:
            self.segundoPlano.stop()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())