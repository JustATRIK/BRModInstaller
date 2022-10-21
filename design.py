

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(782, 135)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(782, 135))
        MainWindow.setMaximumSize(QSize(782, 135))
        icon = QIcon()
        icon.addFile(u":/icons/ico.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"\n"
"QMainWindow::setFixedSize(sizeHint())")
        MainWindow.setIconSize(QSize(128, 128))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 561, 51))
        sizePolicy.setHeightForWidth(self.verticalLayoutWidget.sizePolicy().hasHeightForWidth())
        self.verticalLayoutWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.modFolderDir = QTextEdit(self.verticalLayoutWidget)
        self.modFolderDir.setObjectName(u"modFolderDir")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.modFolderDir.sizePolicy().hasHeightForWidth())
        self.modFolderDir.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.modFolderDir.setFont(font)
        self.modFolderDir.setReadOnly(True)

        self.verticalLayout.addWidget(self.modFolderDir)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(560, 0, 221, 51))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.openModFolderBut = QPushButton(self.verticalLayoutWidget_2)
        self.openModFolderBut.setObjectName(u"openModFolderBut")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.openModFolderBut.sizePolicy().hasHeightForWidth())
        self.openModFolderBut.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(20)
        self.openModFolderBut.setFont(font1)

        self.verticalLayout_2.addWidget(self.openModFolderBut)

        self.installBut = QPushButton(self.centralwidget)
        self.installBut.setObjectName(u"installBut")
        self.installBut.setGeometry(QRect(310, 60, 219, 41))
        sizePolicy2.setHeightForWidth(self.installBut.sizePolicy().hasHeightForWidth())
        self.installBut.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(22)
        self.installBut.setFont(font2)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(710, 110, 71, 21))
        self.autoInstCheckBox = QCheckBox(self.centralwidget)
        self.autoInstCheckBox.setObjectName(u"autoInstCheckBox")
        self.autoInstCheckBox.setGeometry(QRect(10, 110, 361, 20))
        self.autoInstCheckBox.setChecked(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BRModInstaller", None))
        self.modFolderDir.setMarkdown(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u043e\u0439\u0442\u0435 \u043f\u0430\u043f\u043a\u0443 \u0441 \u043c\u043e\u0434\u0430\u043c\u0438\n"
"\n"
"", None))
        self.modFolderDir.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041e\u0442\u043a\u0440\u043e\u0439\u0442\u0435 \u043f\u0430\u043f\u043a\u0443 \u0441 \u043c\u043e\u0434\u0430\u043c\u0438</p></body></html>", None))
        self.openModFolderBut.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.installBut.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"By JustATRIK", None))
        self.autoInstCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e-\u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430(\u0432\u044b\u043a\u043b\u044e\u0447\u0438\u0442\u0435, \u0435\u0441\u043b\u0438 \u043c\u043e\u0434\u044b \u043d\u0435 \u0443\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u044e\u0442\u0441\u044f)", None))
    # retranslateUi

