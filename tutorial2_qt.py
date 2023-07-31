from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Primeira tela em PySide6")

button = QPushButton()
button.setText("Clique Aqui")

window.setCentralWidget(button)

window.show()
app.exec()