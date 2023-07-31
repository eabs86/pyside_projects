from PySide6.QtWidgets import QApplication,QPushButton
import sys
def button_clicked():
    print("O botão foi clicado!")

app = QApplication(sys.argv)
button = QPushButton('Clique Aqui')


button.clicked.connect(button_clicked)

button.show()
app.exec()