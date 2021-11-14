#nx: threaded

import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

class BasicForm(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupGUI()
    
    def setupGUI(self):
        self.resize(300, 300)
        self.label = QLabel("Hello world!!!")
        self.label.setParent(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    form = BasicForm()
    form.show()
    app.exec()
    