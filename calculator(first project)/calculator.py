class Calculator:
    def __init__(self) -> None:
        self.result = 0.0


    def add(self, number):
        self.result += number

    def substract(self, number):
        self.result -= number

    def multiply(self, number):
        self.result *= number

    def divide(self, number):
        self.result /= number
    
    def clear(self):
        self.result = 0.0