from PySide6.QtWidgets import QApplication
from qlabel_qline import Qlabel_Qline
import sys


app = QApplication(sys.argv)
window = Qlabel_Qline()
window.show()

app.exec()