GENERAL_MESSAGE = "Your desired number to {operation} to the result: "

def initialRead(calculator):
    calculator.result = readFloat("Insert your starting number: ")

def readFloat(message= "Your number: "):
        return float(input(message))

def add(calculator):
    calculator.result += readFloat(GENERAL_MESSAGE.format(operation = "add"))
    calculator.print()

def substract(calculator):
    calculator.result -= readFloat(GENERAL_MESSAGE.format(operation = "substract"))
    calculator.print()

def multiply(calculator):
    calculator.result *= readFloat(GENERAL_MESSAGE.format(operation = "multiply"))
    calculator.print()

def divide(calculator):
        calculator.result /= readFloat(GENERAL_MESSAGE.format(operation = "divide"))
        calculator.print()

def clear(calculator):
    print("Cleared")
    initialRead(calculator)