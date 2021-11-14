#nx: threaded

import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLabel, QWidget


class label(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupGUI()

    def setupGUI(self):
        self.resize(400, 200)
        self.setWindowTitle("learn label")
        
        self.label1 = QLabel("label 1")
        self.label2 = QLabel("label 2")
        self.label3 = QLabel("label 3")
        self.label4 = QLabel("label 4")
        
        # 水平布局 horizontal layout
        box = QHBoxLayout()
        box.addWidget(self.label1)
        box.addWidget(self.label2)
        box.addWidget(self.label3)
        box.addWidget(self.label4)
        
        self.setLayout(box)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = label()
    form.show()

    app.exec()