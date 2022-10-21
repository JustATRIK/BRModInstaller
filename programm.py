import sys
import getpass
import logging

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QAbstractItemView, QFontDialog, \
    QMessageBox
from PySide6.QtGui import QPainter, QBrush, QPen, QColor
from PySide6.QtCore import Qt, QStringListModel
import os

import main
from design import Ui_MainWindow

from main import *
from threading import *

import time
logging.basicConfig(level=logging.INFO, filename="BRMIlog.log",filemode="w")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")
class Programmer(QMainWindow):
    def __init__(self):
        super(Programmer, self).__init__()
        self.setWindowIcon(QtGui.QIcon('ico.ico'))
        self.filesDir = ''
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.openFolderBut = self.ui.openModFolderBut
        self.installBut = self.ui.installBut
        self.openFolderBut.clicked.connect(self.selectTrackFile)
        self.installBut.clicked.connect(self.startInstall)
        self.folderPathLab = self.ui.modFolderDir
        self.autoInstallCheck = self.ui.autoInstCheckBox
        self.username = getpass.getuser()
        self.exception = ''
    def selectTrackFile(self) -> None:
        self.filesDir = str(QFileDialog().getExistingDirectory(self, 'Выберите папку с модом', f'C:/Users/{self.username}/Desktop'))
        self.folderPathLab.setText(self.filesDir)
        print(self.filesDir)
    def startInstall(self) -> None:
        if self.filesDir == '':
            self.filesDir = str(
                QFileDialog().getExistingDirectory(self, 'Выберите папку с модом', f'{os.getenv("SystemDrive")}/Users/{self.username}/Desktop'))
            self.folderPathLab.setText(self.filesDir)
        logging.info(f"Попытка установки")
        if not self.autoInstallCheck.isChecked():
            patch = self.filesDir
        else:
            patch = f"{os.getenv('SystemDrive')}/Users/{self.username}/AppData/Local/BrickRigs/SavedRemastered/Vehicles"
        logging.info(f"Путь установки {patch}")
        try:
            self.exception = main.installMods(self.filesDir, patch)
        except BaseException as err :
            logging.exception("Моды не установлены")
            msg = QMessageBox()
            msg.setWindowTitle("Установка не удалась")
            msg.setIcon(QMessageBox.Information)
            msg.setText("""Непревидиная ошибка, для получения информации, посмотрите логи!
Также можно отправить логи на GitHub, для получения справки: 
            """)
            x = msg.exec()
        if self.exception == "NoMods":
            msg = QMessageBox()
            msg.setWindowTitle("Установка не удалась")
            msg.setIcon(QMessageBox.Information)
            msg.setText("В папке не найдено модов!")
            logging.error(f"Модов не найдено")
            x = msg.exec()
        elif 'ModsAlredyInstalled' in self.exception:
            msg = QMessageBox()
            msg.setWindowTitle("Установка завершена")
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"Моды {self.exception.replace('ModsAlredyInstalled', '')}были заменены!")
            logging.info(f"Моды установлены, но {self.exception.replace('ModsAlredyInstalled', '')}были заменены!")
            x = msg.exec()
        elif self.exception == 'installed':
            msg = QMessageBox()
            msg.setWindowTitle("Установка завершена")
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"Моды установлены!")
            logging.info(f"Моды установлены")
            x = msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Programmer()
    window.show()

    sys.exit(app.exec())