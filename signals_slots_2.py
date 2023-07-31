from PySide6.QtWidgets import QApplication,QPushButton
import sys
def button_clicked(data):
    print('Você clicou no botão! A prova:', data)

app = QApplication(sys.argv)
button = QPushButton("Clique aqui")
button.setCheckable(True) #isso torna o botão "checkable". Ele é "unchecked" por padrão

button.clicked.connect(button_clicked)

button.show()
app.exec()