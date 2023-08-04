from PySide6.QtWidgets import QWidget, QLineEdit, QLabel, QPushButton, QHBoxLayout, QVBoxLayout


class Qlabel_Qline(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel e QLineEdit")

        # A set of signals we can connect to

        label = QLabel("Nome Completo:")
        # necessario utilizar o self para acessar os atributos do objeto
        # sem a necessidade de um outro método
        self.line_edit = QLineEdit()
        # self.line_edit.textChanged.connect(self.text_changed)
        # self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        # self.line_edit.editingFinished.connect(self.editing_finished)
        # self.line_edit.returnPressed.connect(self.return_pressed)
        # self.line_edit.selectionChanged.connect(self.selection_changed)
        self.line_edit.textEdited.connect(self.text_edited)
        
        
        button = QPushButton("Imprimir texto")
        button.clicked.connect(self.button_clicled)

        self.text_holder_label = QLabel("Eu estou aqui!")

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        self.setLayout(v_layout)
        
    #slots
    def button_clicled(self):
        self.text_holder_label.setText(self.line_edit.text())
    
    def text_changed(self):
        self.text_holder_label.setText(self.line_edit.text())

    def cursor_position_changed(self,old,new):
        print("cursor old position:", old, "- cursor new position:", new)
    
    def editing_finished(self):
        print("Texto finalizado") #vai imprimir quando teclar enter ou clicar no botão.
    
    def return_pressed(self):
        print("Enter pressionado")#acionado quando enter é pressionado, porém não é acionado com o botão
        
    def selection_changed(self):
        print("Selecão: ",self.line_edit.selectedText()) 
    
    def text_edited(self,new_text):
        print("Texto editado: ", new_text)