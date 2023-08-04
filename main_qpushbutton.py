from PySide6.QtWidgets import QApplication
from qpushbutton_widget import QPush
import sys


app = QApplication(sys.argv)
window = QPush()
window.show()

app.exec()