#separando o conteúdo do tutorial2_qt.py em classes

import sys
from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder
        
app = QApplication(sys.argv)
win = ButtonHolder()
win.show()
app.exec()