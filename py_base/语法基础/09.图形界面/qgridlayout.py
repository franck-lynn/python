#nx: threaded
# https://www.bilibili.com/video/BV1pM4y1K7Xc?p=3&spm_id_from=pageDriver
import sys
from PyQt6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

class GridBox(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupGUI()
    
    def setupGUI(self):
        self.resize(500, 500)
        self.setWindowTitle("VERIACAL BOX")
        
        self.buttonA = QPushButton("ButtonA")
        self.buttonB = QPushButton("ButtonB")
        self.buttonC = QPushButton("ButtonC")
        self.buttonD = QPushButton("ButtonD")
        
        layout = QGridLayout()
        layout.addWidget(self.buttonA, 0, 0)
        layout.addWidget(self.buttonB, 0, 1)
        layout.addWidget(self.buttonC, 1, 0)
        layout.addWidget(self.buttonD, 1, 1)
        
        self.setLayout((layout))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    form = GridBox()
    form.show()
    
    app.exec()