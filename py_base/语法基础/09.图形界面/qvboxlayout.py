#nx: threaded
# https://www.bilibili.com/video/BV1pM4y1K7Xc?p=3&spm_id_from=pageDriver
import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

class VerticalBox(QWidget):
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
        self.buttonE = QPushButton("ButtonA")
        
        layout = QVBoxLayout()
        layout.addWidget(self.buttonA)
        layout.addWidget(self.buttonB)
        layout.addWidget(self.buttonC)
        layout.addWidget(self.buttonD)
        layout.addWidget(self.buttonE)
        
        self.setLayout((layout))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    form = VerticalBox()
    form.show()
    
    app.exec()