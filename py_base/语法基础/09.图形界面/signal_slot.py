#nx: threaded

import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QPushButton, QWidget


class signal_slot(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupGUI()

    def setupGUI(self):
        self.resize(500, 300)
        self.setWindowTitle('SIGNAL & SLOT')
        
        #! TODO
        self.textBox1 = QLineEdit()
        self.button1 = QPushButton("清除")
        self.button2 = QPushButton("退出")
        box = QHBoxLayout()
        box.addWidget(self.textBox1)
        box.addWidget(self.button1)
        box.addWidget(self.button2)
        
        self.setLayout(box)
        
        self.button1.clicked.connect(self.textBox1.clear)
        self.button2.clicked.connect(self.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = signal_slot()
    form.show()

    app.exec()