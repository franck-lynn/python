#nx: threaded
# https://zetcode.com/pyqt6/menustoolbars/
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow


class statusbar(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupGUI()

    def setupGUI(self):
        self.statusBar().showMessage("Ready")
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Statusbar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = statusbar()
    form.show()

    app.exec()