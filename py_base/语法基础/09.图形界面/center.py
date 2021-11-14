#nx: threaded

import sys
from PyQt6.QtWidgets import QApplication, QWidget


class center(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupGUI()

    def setupGUI(self):
        self.resize(350, 250)
        self.center()

        self.setWindowTitle('Center')
    
    def center(self):
        qr = self.frameGeometry()
        # 查询屏幕尺寸
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = center()
    form.show()

    app.exec()