'''
Curso de creación de GUIs con Qt5 y Python

Author: Kiko Correoso
Website: pybonacci.org 
Licencia: MIT
'''

import os
os.environ['QT_API'] = 'pyside2'
import sys

from qtpy.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 300)
    w.move(0, 0)
    w.setWindowTitle('Hola, Mundo')
    w.show()

    sys.exit(app.exec_())
