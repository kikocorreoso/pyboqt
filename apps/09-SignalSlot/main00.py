import os
os.environ['QT_API'] = 'pyside2'
import sys

from qtpy.QtWidgets import QApplication, QPushButton
from qtpy.QtCore import Slot

@Slot()
def say_hello():
 print("Button pulsado, ¡Hola!")

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    boton = QPushButton("Pulsa")
    boton.clicked.connect(say_hello)
    boton.show()
    sys.exit(app.exec_())
