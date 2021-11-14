#nx: threaded

import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget


class quit_button(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupGUI()

    def setupGUI(self):
        qbtn = QPushButton("退出", self) # 第2个参数是父小部件
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        
        self.setGeometry(400, 400, 350, 250)
        self.setWindowTitle("退出按钮")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = quit_button()
    form.show()

    app.exec()