# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HelloworldUI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_Helloworld(object):
    def setupUi(self, Helloworld):
        if not Helloworld.objectName():
            Helloworld.setObjectName(u"Helloworld")
        Helloworld.setWindowModality(Qt.ApplicationModal)
        Helloworld.resize(274, 145)
        self.label = QLabel(Helloworld)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 151, 91))
        self.label.setMaximumSize(QSize(151, 91))

        self.retranslateUi(Helloworld)

        QMetaObject.connectSlotsByName(Helloworld)
    # setupUi

    def retranslateUi(self, Helloworld):
        Helloworld.setWindowTitle(QCoreApplication.translate("Helloworld", u"\u5bf9\u8bdd\u6846\u7684\u6807\u9898", None))
        self.label.setText(QCoreApplication.translate("Helloworld", u"\u4e00\u4e2a\u7b80\u5355\u7684\u5bf9\u8bdd\u6846-\u6807\u7b7e", None))
    # retranslateUi

