'''
Curso de creación de GUIs con Qt5 y Python

Author: Kiko Correoso
Website: pybonacci.org 
Licencia: MIT
'''

import os
os.environ['QT_API'] = 'pyside2'
import sys
from pathlib import Path

from qtpy.QtWidgets import QApplication, QWidget
from qtpy.QtGui import QIcon

if __name__ == '__main__':
    
    ruta_icono = Path('.', 'imgs', 'pybofractal.png')
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 300)
    w.move(0, 0)
    w.setWindowTitle('Hola, Icono')
    w.setWindowIcon(QIcon(str(ruta_icono)))
    w.show()

    sys.exit(app.exec_())
