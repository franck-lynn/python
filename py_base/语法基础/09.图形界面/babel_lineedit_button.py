#nx: threaded

import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class babel_lineedit_button(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupGUI()

    def setupGUI(self):
        self.resize(500,300)
        self.setWindowTitle("MAIN FORM")
        
        self.label1 = QLabel('Label 1')
        self.lineedit1 = QLineEdit()
        self.button1 = QPushButton("按钮")
        
        # vbox1 = QHBoxLayout()
        vbox1 = QVBoxLayout()
        vbox1.addStretch()
        
        vbox1.addWidget(self.label1)
        vbox1.addWidget((self.lineedit1))
        vbox1.addWidget(self.button1)
        
        self.setLayout(vbox1)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = babel_lineedit_button()
    form.show()

    app.exec()