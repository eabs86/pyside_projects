from PySide6.QtWidgets import QPushButton,QWidget,QHBoxLayout,QVBoxLayout

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")
        
        button1 = QPushButton("Botão 1")
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("Botão 2")
        button2.clicked.connect(self.button2_clicked)

        
        #necessidade de adicionar o botão no layout
        # widget_layout = QHBoxLayout() #horizontal
        widget_layout = QVBoxLayout() #vertical
        widget_layout.addWidget(button1)
        widget_layout.addWidget(button2)
        self.setLayout(widget_layout)
    
    def button1_clicked(self):
        print("Botão 1 foi clicado!")
    
    def button2_clicked(self):
        print("Botão 2 foi clicado!")