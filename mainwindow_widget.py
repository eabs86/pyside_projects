from PySide6.QtWidgets import  QMainWindow,QToolBar, QPushButton,QStatusBar
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app = app # essa sera a aplicação
        self.setWindowTitle("Tela Customizada")
        
        #menubar e menus
        
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        fechar_tela = file_menu.addAction("Fechar")
        fechar_tela.triggered.connect(self.fechar_app)
        
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copiar")
        edit_menu.addAction("Recortar")
        edit_menu.addAction("Colar")
        edit_menu.addAction("Desfazer")
        edit_menu.addAction("Refazer")
        
        menu_bar.addMenu("Janela")
        menu_bar.addMenu("Configurações")
        menu_bar.addMenu("Ajuda")
        
        #criando toolbars
        toolbar = QToolBar("Minha barra de ferramentas")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        
        #adicionando ações a toolbar
        toolbar.addAction(fechar_tela) #disparando a ação de fechar a tela
        
        #criando acoes
        
        action1 = QAction("Clique Aqui",self)
        action1.setStatusTip("Mensagem de Status para uma ação")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)
        
        action2 = QAction(QIcon("start.png"), "Inicia", self)
        action2.setStatusTip("Mensagem de Status para a ação 2 com icone")
        action2.triggered.connect(self.toolbar_button_click)
        action2.setCheckable(True)
        toolbar.addAction(action2)
        
        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Push Button"))
        
        
        #status bar
        
        self.setStatusBar(QStatusBar(self))
        
        
        
        
        
    def fechar_app(self):
        self.app.quit()
    
    def toolbar_button_click(self):
        print("action1 disparada!")
        self.statusBar().showMessage("A ação foi executada!",3000)
        
