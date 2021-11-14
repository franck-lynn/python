#nx: threaded

import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class sample_app(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupGUI()

    def setupGUI(self):
        self.resize(500, 300)
        self.setWindowTitle('Sample App 1')
        #! TODO
        self.label1 = QLabel("First Number")
        self.number1 = QLineEdit()
        self.label2 = QLabel("Second Number")
        self.number2 = QLineEdit()
        self.label3 = QLabel("结果")
        self.number3 = QLineEdit()
        
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.number1)
        vbox1.addWidget(self.label2)
        vbox1.addWidget(self.number2)
        vbox1.addWidget(self.label3)
        vbox1.addWidget(self.number3)
        vbox1.addStretch()
        # self.setLayout(vbox1)
        
        self.button1 = QPushButton("加")
        self.button2 = QPushButton("减")
        self.button3 = QPushButton("乘")
        self.button4 = QPushButton("除")
        
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.button1)
        vbox2.addWidget(self.button2)
        vbox2.addWidget(self.button3)
        vbox2.addWidget(self.button4)
        vbox2.addStretch()
        # self.setLayout(vbox2)
        
        hbox1 = QHBoxLayout()
        hbox1.addLayout(vbox1)
        hbox1.addLayout(vbox2)
        
        self.setLayout(hbox1)
        
        
        self.button1.clicked.connect(lambda: self.calculate('+'))
        self.button2.clicked.connect(lambda: self.calculate('-'))
        self.button3.clicked.connect(lambda: self.calculate('*'))
        self.button4.clicked.connect(lambda: self.calculate('/'))
        
    def calculate(self, operator):
        a = float(self.number1.text())
        b = float(self.number2.text())
        c = 0.0
        if operator == "+": c = a + b
        elif operator == "-": c = a - b
        elif operator == "*": c = a * b
        else: c = a / b
        self.number3.setText(str(c))
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = sample_app()
    form.show()

    app.exec()