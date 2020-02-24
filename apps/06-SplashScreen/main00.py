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
import time ## NUEVA LÍNEA

from qtpy.QtCore import Qt
from qtpy.QtWidgets import QApplication, QMainWindow, QSplashScreen
from qtpy.QtGui import QIcon, QPixmap

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self._create_ui()

    def _create_ui(self):
        self.resize(500, 300)
        self.move(0, 0)
        self.setWindowTitle('Hola, QMainWindow')
        ruta_icono = Path('.', 'imgs', 'pybofractal.png')
        self.setWindowIcon(QIcon(str(ruta_icono)))
        self.statusBar().showMessage('Ready')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
	
    # Crea y muestra el splash screen
    path = Path('imgs', 'splashscreen_background.jpg')
    splash_pix = QPixmap(str(path))
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setEnabled(False)
    splash.show()
    
    # Esto es un simple contador/temporizador para mostrar en pantalla
    # el splash screen. En el futuro haremos que esto sea más útil.
    for i in range(0, 5):
        msg = (
            '<h1><font color="yellow">'
            f'Listo en {5 - i}s'
            '</font></h1>'
        )
        splash.showMessage(
            msg,
            int(Qt.AlignLeft) | int(Qt.AlignBottom),
            Qt.black
        )
        time.sleep(1)
        app.processEvents()

    w = MiVentana()
    splash.finish(w)
    sys.exit(app.exec_())
