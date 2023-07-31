
from PySide6.QtWidgets import  QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Primeira tela em PySide6")
        self.button = QPushButton()
        self.button.setText("Clique Aqui")
        self.setCentralWidget(self.button)