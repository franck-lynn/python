#nx: threaded

import sys
from PyQt6.QtWidgets import QApplication, QGridLayout, QLineEdit, QWidget


class lineedit(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupGUI()

    def setupGUI(self):
        self.resize(500, 300)
        self.setWindowTitle('learn textbox')
        #! TODO
        self.textbox1 = QLineEdit('Edit Text 1')
        self.textbox2 = QLineEdit('Edit Text 2')
        self.textbox3 = QLineEdit('Edit Text 3')
        self.textbox4 = QLineEdit('Edit Text 4')
        
        box = QGridLayout()
        box.addWidget(self.textbox1, 0, 0)
        box.addWidget(self.textbox2, 0, 1)
        box.addWidget(self.textbox3, 1, 0)
        box.addWidget(self.textbox4, 1, 1)
        
        self.setLayout(box)
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = lineedit()
    form.show()

    app.exec()