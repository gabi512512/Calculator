GENERAL_MESSAGE = "Operation: {operation} | Your number: "

def initialRead(calculator):
    calculator.result = readFloat("Insert your starting number: ")

def readFloat(message= "Your number: "):
        return float(input(message))

def add(calculator):
    calculator.result += readFloat(GENERAL_MESSAGE.format(operation = "add"))
    calculator.print()

def subtract(calculator):
    calculator.result -= readFloat(GENERAL_MESSAGE.format(operation = "subtract"))
    calculator.print()

def multiply(calculator):
    calculator.result *= readFloat(GENERAL_MESSAGE.format(operation = "multiplication"))
    calculator.print()

def divide(calculator):
        calculator.result /= readFloat(GENERAL_MESSAGE.format(operation = "division"))
        calculator.print()

def clear(calculator):
    print("Cleared")
    initialRead(calculator)