#nx: threaded
# https://zetcode.com/pyqt6/firstprograms/
import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QToolTip, QWidget

from PyQt6.QtGui import QFont


class tooltip(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupGUI()

    def setupGUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip("This is a <b>QWidget</b> widget")
        
        btn = QPushButton("按钮", self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        
        # 对话框距离屏幕上, 左边距, 以及宽, 高
        self.setGeometry(600, 300, 300, 200)
        self.setWindowTitle('Quit button')
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = tooltip()
    form.show()

    app.exec()