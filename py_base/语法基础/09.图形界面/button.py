#nx: threaded

import sys
from PyQt6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget


class button(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupGUI()

    def setupGUI(self):
        self.resize(500, 300)
        self.setWindowTitle('learn button')
        #! TODO
        self.button1 = QPushButton('button 1')
        self.button2 = QPushButton('button 2')
        self.button3 = QPushButton('button 3')
        self.button4 = QPushButton('button 4')
        
        box = QGridLayout()
        box.addWidget(self.button1, 0, 0)
        box.addWidget(self.button2, 0, 1)
        box.addWidget(self.button3, 1, 0)
        box.addWidget(self.button4, 1, 1)
        
        self.setLayout(box)
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = button()
    form.show()

    app.exec()