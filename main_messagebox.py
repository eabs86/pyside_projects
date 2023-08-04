from PySide6.QtWidgets import QApplication
from messagebox_widget import MessageBox
import sys


app = QApplication(sys.argv)
window = MessageBox()
window.show()

app.exec()