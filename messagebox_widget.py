from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox


class MessageBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message Boxes utilizando QMessageBox")

        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_clicked_hard)

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_clicked_question)

        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)

        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)

    # the hard way
    def button_clicked_hard(self):
        message = QMessageBox()
        message.setMinimumSize(700, 200)
        message.setWindowTitle("Titulo da Mensagem")
        message.setText("Algo aconteceu")
        message.setInformativeText("Você que fazer algo com relação a isso?")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)

        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("você escolheu Ok")
        else:
            print("Você escolheu Cancelar")

    def button_clicked_critical(self):
        # the soft way: uso de método estático
        ret = QMessageBox.critical(self,
                                   "Título",
                                   "Algo aconteceu!",
                                   QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("Você escolheu Ok")
        else:
            print("Você escolheu Cancelar")

    def button_clicked_question(self):
        ret = QMessageBox.question(self,
                            "Título",
                            "Tem alguma pergunta?",
                            QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("Você escolheu Ok")
        else:
            print("Você escolheu Cancelar")

    def button_clicked_information(self):
        ret = QMessageBox.information(self,
                            "Título",
                            "Está é uma informação",
                            QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("Você escolheu Ok")
        else:
            print("Você escolheu Cancelar")

    def button_clicked_warning(self):
        ret = QMessageBox.warning(self,
                            "Título",
                            "Este é um aviso!",
                            QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("Você escolheu Ok")
        else:
            print("Você escolheu Cancelar")

    def button_clicked_about(self):
        ret = QMessageBox.about(self,
                            "Título",
                            "Mensagem qualquer")
        if ret == QMessageBox.Ok:
            print("Você escolheu Ok")
        else:
            print("Você escolheu Cancelar")
