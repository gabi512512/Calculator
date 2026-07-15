from constants import INPUT_ERROR

class Calculator:
    def __init__(self) -> None:
        self.result = 0.0

    def getNumber(self, text):
        try:
            number = int(text)
            return number
        except ValueError:
            try:
                number = float(text)
                return number
            except ValueError:
                return INPUT_ERROR[0]

    def add(self, number):
        self.result += number

    def subtract(self, number):
        self.result -= number

    def multiply(self, number):
        self.result *= number

    def divide(self, number):
        try:
            self.result /= number
        except ZeroDivisionError:
            return INPUT_ERROR[1]
    
    def clear(self):
        self.result = 0.0