#nx: threaded
# https://zetcode.com/pyqt6/firstprograms/
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox, QWidget

from PyQt6 import QtGui


class messagebox(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupGUI()

    def setupGUI(self):
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle("信息框")
    
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        reply = QMessageBox.question(self, "Message", 
            "确定退出? ", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else: 
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = messagebox()
    form.show()

    sys.exit(app.exec())