import sys
from functools import partial
from calculator import Calculator
from constants import OPERATORS, CONSTANTS, INPUT_ERROR
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QPushButton, QLineEdit, 
                             QWidget, QGridLayout, QVBoxLayout)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calc = Calculator()
        self.setWindowTitle("Calculator")
        self.setGeometry(200, 100, 480, 720)
        self.title = QLabel("Calculator")
        self.input = QLineEdit()
        self.result = QLabel(f"Result: {self.calc.result:g}")
        self.error = QLabel()
        self.btn1 = QPushButton("1")
        self.btn2 = QPushButton("2")
        self.btn3 = QPushButton("3")
        self.btn4 = QPushButton("4")
        self.btn5 = QPushButton("5")
        self.btn6 = QPushButton("6")
        self.btn7 = QPushButton("7")
        self.btn8 = QPushButton("8")
        self.btn9 = QPushButton("9")
        self.btn0 = QPushButton("0")
        self.btn_add = QPushButton("+")
        self.btn_sub = QPushButton("-")
        self.btn_mul = QPushButton("*")
        self.btn_div = QPushButton("/")
        self.btn_clr = QPushButton("Clear")
        self.grid = grid = QGridLayout()
        self.initName()
        self.initUI()


    def initUI(self):
        central_widget = QWidget()
        vbox = QVBoxLayout()
        self.setCentralWidget(central_widget)

        self.grid.addWidget(self.btn1, 0, 0)
        self.grid.addWidget(self.btn2, 0, 1)
        self.grid.addWidget(self.btn3, 0, 2)
        self.grid.addWidget(self.btn4, 1, 0)
        self.grid.addWidget(self.btn5, 1, 1)
        self.grid.addWidget(self.btn6, 1, 2)
        self.grid.addWidget(self.btn7, 2, 0)
        self.grid.addWidget(self.btn8, 2, 1)
        self.grid.addWidget(self.btn9, 2, 2)
        self.grid.addWidget(self.btn0, 3, 1)
        self.grid.addWidget(self.btn_add, 0, 3)
        self.grid.addWidget(self.btn_sub, 1, 3)
        self.grid.addWidget(self.btn_mul, 2, 3)
        self.grid.addWidget(self.btn_div, 3, 3)

        self.align()

        vbox.addWidget(self.title)
        vbox.addWidget(self.input)
        vbox.addWidget(self.result)
        vbox.addWidget(self.error)
        vbox.addLayout(self.grid)
        vbox.addWidget(self.btn_clr)
        vbox.setSpacing(10)
        central_widget.setLayout(vbox)

        self.commonListener()


    def commonListener(self):
        all_buttons = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, 
                       self.btn6, self.btn7, self.btn8, self.btn9, self.btn0,
                       self.btn_add, self.btn_sub, self.btn_mul, self.btn_div, self.btn_clr]

        for btn in all_buttons:
            btn.clicked.connect(partial(self.on_button_click, btn.text()))


    def on_button_click(self, text):
        if text in OPERATORS.keys():
            number = self.calc.getNumber(self.input.text())
            if number == INPUT_ERROR[0]:
                self.error.setText(INPUT_ERROR[0])
                error_occured = True
            else:
                if text == "+":
                    self.calc.add(number)
                    error_occured = False
                elif text == "-":
                    self.calc.subtract(number)
                    error_occured = False
                elif text == "*":
                    self.calc.multiply(number)
                    error_occured = False
                elif text == "/":
                    if self.calc.divide(number) == INPUT_ERROR[1]:
                        self.error.setText(INPUT_ERROR[1])
                        error_occured = True
                    else:
                        error_occured = False
                
                self.result.setText(f"Result: {self.calc.result:g}")
                self.input.setText("")
                if not error_occured:
                    self.error.setText("")

        elif text == "Clear":
            self.calc.clear()
            self.result.setText(f"Result: {self.calc.result:g}")
            self.input.setText("")

        else:
            self.input.setText(self.input.text() + text)


    @staticmethod
    def start():
        app = QApplication(sys.argv)
        with open("calculator\style.qss", "r") as f:
            app.setStyleSheet(f.read())
        window = MainWindow()
        window.show()
        sys.exit(app.exec())


    def align(self):
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setMaximumHeight(50)
        self.input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.result.setMaximumHeight(50)
        self.error.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.error.setMaximumHeight(50)
        self.grid.setAlignment(Qt.AlignmentFlag.AlignCenter)


    def initName(self):
        self.title.setObjectName("title")
        self.input.setObjectName("input")
        self.result.setObjectName("result")
        self.error.setObjectName("error")
        
        """self.btn1.setObjectName("btn1")
        self.btn2.setObjectName("btn2")
        self.btn3.setObjectName("btn3")
        self.btn4.setObjectName("btn4")
        self.btn5.setObjectName("btn5")
        self.btn6.setObjectName("btn6")
        self.btn7.setObjectName("btn7")
        self.btn8.setObjectName("btn8")
        self.btn9.setObjectName("btn9")
        self.btn0.setObjectName("btn0")
        self.btn_add.setObjectName("btn_add")
        self.btn_sub.setObjectName("btn_sub")
        self.btn_mul.setObjectName("btn_mul")
        self.btn_div.setObjectName("btn_div")"""