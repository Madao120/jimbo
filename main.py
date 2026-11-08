import sys
from PyQt6.QtWidgets import *

class JimboStore(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)

        self.setWindowTitle("Jimbo")
        self.setMinimumSize(1000, 600)
        self.setMaximumSize(1200, 700)



        layout_principal = QGridLayout()

        # Columna 1
        dinero = QLabel("100")
        layout_principal.addWidget(dinero, 0, 0, 1, 1)

        ronda = QLabel("0/3")
        ante = QLabel("0/8")
        layout_principal.addWidget(ronda, 1, 0, 1, 1)
        layout_principal.addWidget(ante, 2, 0, 1, 1)

        #Columna 2
        ciega1 = QVBoxLayout()
        ciega1.addWidget(QLabel("Ciega 1"))
        btn_ciega1 = QPushButton("Ciega")
        btn_ciega1.clicked.connect(self.to_ciega)
        ciega1.addWidget(btn_ciega1)
        ciega2 = QVBoxLayout()
        ciega2.addWidget(QLabel("Ciega 2"))
        ciega2.addWidget(QPushButton("Seleccionar"))
        ciega3 = QVBoxLayout()
        ciega3.addWidget(QLabel("Ciega Jefe"))
        ciega3.addWidget(QPushButton("Seleccionar"))

        layout_principal.addLayout(ciega1, 0, 1, 1, 1)
        layout_principal.addLayout(ciega2, 0, 2, 1, 1)
        layout_principal.addLayout(ciega3, 0, 3, 1, 1)


        contenedor = QWidget()
        contenedor.setLayout(layout_principal)
        self.setCentralWidget(contenedor)


        ### Layout de card

    def to_ciega(self):
        self.card.currentWidget().show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    variable = JimboStore()
    variable.show()
    app.exec()


