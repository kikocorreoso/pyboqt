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
from time import time, sleep

from qtpy.QtWidgets import ( ##
    QApplication, QMainWindow, QAction, QMessageBox, QPushButton##
) ##
from qtpy.QtGui import QIcon
from qtpy.QtCore import Signal, Slot, QObject, QTimer ## NUEVA LÍNEA
import qtawesome as qta


class MiVentana(QMainWindow):
    started = Signal(str) ##
    finished = Signal(str) ##

    def __init__(self):
        super().__init__()
        self._create_ui()
        #self._infor = Informador(self)
        self.started.connect(self._update_status_bar)
        self.finished.connect(self._update_status_bar)

    def _create_ui(self):
        self.resize(500, 300)
        #self.move(0, 0)
        self.setWindowTitle('Hola, QMainWindow')
        ruta_icono = Path('.', 'imgs', 'pybofractal.png')
        self.setWindowIcon(QIcon(str(ruta_icono)))
        self.statusBar().showMessage('Ready')
        self._create_menu()        
        self._set_central_widget()
        self.show()

    def _create_menu(self):        
        menubar = self.menuBar()
        # File menu and its QAction's
        file_menu = menubar.addMenu('&File')
        exit_action = QAction(qta.icon('fa5.times-circle'),
                              '&Exit',
                              self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(QApplication.instance().closeAllWindows)
        file_menu.addAction(exit_action)
        # Help menu and its QAction's
        help_menu = menubar.addMenu('&Help')
        about_action = QAction(qta.icon('fa5s.info-circle'),
                               '&About',
                               self)
        about_action.setShortcut('Ctrl+I')
        about_action.setStatusTip('About...')
        about_action.triggered.connect(self._show_about_dialog)
        help_menu.addAction(about_action)
    
    def _set_central_widget(self):
        self.btn = QPushButton(self)
        self.btn.setText('dale')
        self.btn.pressed.connect(self._read)
        self.btn.released.connect(self._process)
        self.setCentralWidget(self.btn)
    
    @Slot()
    def _read(self):
        self.started.emit('Reading...')
    
    @Slot(str)
    def _update_status_bar(self, msg):
        self.statusBar().showMessage(msg)

    @Slot()
    def _show_about_dialog(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("Pybonacci app v -37.3")
        msg_box.setWindowTitle("Ejemplo de Slot")
        msg_box.setStandardButtons(QMessageBox.Close)
        msg_box.exec_()
    
    def _process(self):
        # Aquí procesaríamos algo, por ejemplo, leer un fichero grande
        t0 = time()
        while t0 + 3 >= time() >= t0:
            sleep(1)
        # Fin del proceso largo
        self.finished.emit('Finished!!!')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = MiVentana()
    sys.exit(app.exec_())
