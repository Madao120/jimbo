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

        eleccionCiegas = QWidget()
        layout_principal = QGridLayout()

        # Dinero, Rondas y Ante

        dinero = QLabel("100$")
        ronda = QLabel("Round: 0")
        ante = QLabel("Ante: 0/8")

        layout_principal.addWidget(dinero, 0, 0)
        layout_principal.addWidget(ronda, 1, 0)
        layout_principal.addWidget(ante, 2, 0)

        # Ciegas y skips

        ciega1 = QVBoxLayout()
        btn_toCiega1 = QPushButton("Ciega 1")
        btn_toCiega1.clicked.connect(self.to_ciega)
        btn_ciega1 = QPushButton("Skip 1")
        btn_ciega1.clicked.connect(self.skip1)
        ciega1.addWidget(btn_toCiega1)
        ciega1.addWidget(btn_ciega1)

        ciega2 = QVBoxLayout()
        btn_toCiega2 = QPushButton("Ciega 2")
        btn_toCiega2.clicked.connect(self.to_ciega)
        btn_ciega2 = QPushButton("Skip 2")
        btn_ciega2.clicked.connect(self.skip2)
        ciega2.addWidget(btn_toCiega2)
        ciega2.addWidget(btn_ciega2)

        ciega3 = QVBoxLayout()
        btn_toCiega3 = QPushButton("Boss")
        btn_toCiega3.clicked.connect(self.to_ciega)
        ciega3.addWidget(btn_toCiega3)

        layout_principal.addLayout(ciega1, 0, 1,3,1)
        layout_principal.addLayout(ciega2, 0, 2,3,1)
        layout_principal.addLayout(ciega3, 0, 3,2,1)

        eleccionCiegas.setLayout(layout_principal)

        self.ciega = QWidget()

        self.cards.addWidget(eleccionCiegas)
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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    variable = JimboStore()
    variable.show()
    app.exec()


