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

from qtpy.QtWidgets import QApplication, QMainWindow, QAction
from qtpy.QtGui import QIcon
import qtawesome as qta


class MiVentana(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self._create_ui()
        instance = QApplication.instance()
        self.menuBar().hovered.connect(instance.closeAllWindows)

    def _create_ui(self):
        self.resize(500, 300)
        self.move(0, 0)
        self.setWindowTitle('Hola, QMainWindow')
        ruta_icono = Path('.', 'imgs', 'pybofractal.png')
        self.setWindowIcon(QIcon(str(ruta_icono)))
        self.statusBar().showMessage('Ready')
        self._create_menu()

    def _create_menu(self):        
        menubar = self.menuBar()
        # File menu and its QAction's
        file_menu = menubar.addMenu('&File')
        exit_action = QAction(qta.icon('fa5.times-circle'),
                              '&Exit',
                              self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        file_menu.addAction(exit_action)
        # Help menu and its QAction's
        help_menu = menubar.addMenu('&Help')
        about_action = QAction(qta.icon('fa5s.info-circle'),
                               '&Exit',
                               self)
        about_action.setShortcut('Ctrl+I')
        about_action.setStatusTip('About...')
        help_menu.addAction(about_action)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = MiVentana()
    w.show()
    sys.exit(app.exec_())
