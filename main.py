import sys
from PyQt6.QtWidgets import *

class JimboStore(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)

        self.setWindowTitle("Jimbo")
        self.setMinimumSize(1000, 600)
        self.setMaximumSize(1200, 700)

        self.cards = QStackedLayout()

        self.eleccionCiegas = QWidget()
        layout_principal = QGridLayout()

        # Dinero, Rondas y Ante

        dineroTXT = "100$"
        rondaTXT = "Round: 0"
        anteTXT = "Ante: 0/8"

        dinero = QLabel(dineroTXT)
        ronda = QLabel(rondaTXT)
        ante = QLabel(anteTXT)

        self.datos = QVBoxLayout()

        self.datos.addWidget(dinero)
        self.datos.addWidget(ronda)
        self.datos.addWidget(ante)

        layout_principal.addLayout(self.datos, 0, 0)

        # Ciegas y skips

        btn_toCiega1 = QPushButton("Ciega 1")
        btn_toCiega1.clicked.connect(self.to_ciega)
        btn_ciega1 = QPushButton("Skip 1")
        btn_ciega1.clicked.connect(self.skip1)

        layout_principal.addWidget(btn_toCiega1, 0, 1)
        layout_principal.addWidget(btn_ciega1, 1, 1)


        btn_toCiega2 = QPushButton("Ciega 2")
        btn_toCiega2.clicked.connect(self.to_ciega)
        btn_ciega2 = QPushButton("Skip 2")
        btn_ciega2.clicked.connect(self.skip2)

        layout_principal.addWidget(btn_toCiega2, 0, 2)
        layout_principal.addWidget(btn_ciega2, 1, 2)


        btn_toCiega3 = QPushButton("Boss")
        btn_toCiega3.clicked.connect(self.to_ciega)

        layout_principal.addWidget(btn_toCiega3, 0, 3)

        self.eleccionCiegas.setLayout(layout_principal)

        #---------------------------------------

        self.datosC = QVBoxLayout()

        dineroC = QLabel(dineroTXT)
        rondaC = QLabel(rondaTXT)
        anteC = QLabel(anteTXT)

        self.datosC.addWidget(dineroC)
        self.datosC.addWidget(rondaC)
        self.datosC.addWidget(anteC)

        self.ciega = QWidget()
        layout_ciegas = QGridLayout()
        layout_ciegas.addLayout(self.datosC, 0, 0)
        btn_pasar = QPushButton("Pasar")
        layout_ciegas.addWidget(btn_pasar, 0, 1)


        self.ciega.setLayout(layout_ciegas)







        self.cards.addWidget(self.eleccionCiegas)
        self.cards.addWidget(self.ciega)

        contenedor = QWidget()
        contenedor.setLayout(self.cards)
        self.setCentralWidget(contenedor)


    def to_ciega(self):
        self.cards.setCurrentWidget(self.ciega)

    def skip1(self):
        pass

    def skip2(self):
        pass

    def start(self):
        self.cards.setCurrentIndex(0)

    def to_tienda(self):
        self.cards.setCurrentWidget(self.tienda)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    variable = JimboStore()
    variable.show()
    app.exec()


