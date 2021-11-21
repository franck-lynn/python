# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'httpclient.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(749, 757)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.editUrl = QLineEdit(Form)
        self.editUrl.setObjectName(u"editUrl")

        self.horizontalLayout.addWidget(self.editUrl)

        self.buttonSend = QPushButton(Form)
        self.buttonSend.setObjectName(u"buttonSend")

        self.horizontalLayout.addWidget(self.buttonSend)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label)

        self.buttonAddHeader = QPushButton(Form)
        self.buttonAddHeader.setObjectName(u"buttonAddHeader")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.buttonAddHeader.sizePolicy().hasHeightForWidth())
        self.buttonAddHeader.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.buttonAddHeader)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.buttonDelHeader = QPushButton(Form)
        self.buttonDelHeader.setObjectName(u"buttonDelHeader")
        sizePolicy2.setHeightForWidth(self.buttonDelHeader.sizePolicy().hasHeightForWidth())
        self.buttonDelHeader.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.buttonDelHeader)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.headersTable = QTableWidget(Form)
        if (self.headersTable.columnCount() < 2):
            self.headersTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.headersTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.headersTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.headersTable.setObjectName(u"headersTable")

        self.verticalLayout.addWidget(self.headersTable)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 9, -1, 9)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.label_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.editBody = QPlainTextEdit(Form)
        self.editBody.setObjectName(u"editBody")

        self.verticalLayout_2.addWidget(self.editBody)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.outputWindow = QPlainTextEdit(Form)
        self.outputWindow.setObjectName(u"outputWindow")

        self.verticalLayout_3.addWidget(self.outputWindow)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buttonClearLog = QPushButton(Form)
        self.buttonClearLog.setObjectName(u"buttonClearLog")
        sizePolicy.setHeightForWidth(self.buttonClearLog.sizePolicy().hasHeightForWidth())
        self.buttonClearLog.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.buttonClearLog)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"HTTP \u63a5\u53e3\u6d4b\u8bd5", None))
        self.buttonSend.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6d88\u606f\u5934", None))
        self.buttonAddHeader.setText(QCoreApplication.translate("Form", u"+", None))
        self.buttonDelHeader.setText(QCoreApplication.translate("Form", u"-", None))
        ___qtablewidgetitem = self.headersTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.headersTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u503c", None));
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6d88\u606f\u4f53", None))
        self.buttonClearLog.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
    # retranslateUi

