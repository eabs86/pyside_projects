from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox


class QPush(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tela customizada")

        button = QPushButton("Clique Aqui")
        button.clicked.connect(self.button_clicked)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)

        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)

    def button_clicked(self):
        print("button clicked")

    def button_pressed(self):
        print("button pressed")

    def button_released(self):
        print("button released")
