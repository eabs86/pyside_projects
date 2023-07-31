from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider
import sys

# o slot: responde quando algo acontece

def respond_to_slider(data):
    print("o slider foi movido para:", data)
    
app = QApplication(sys.argv)

slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)


slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()