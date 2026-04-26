GENERAL_MESSAGE = "Operation: {operation} | Your number: "

def initialRead(calculator) -> None:
    calculator.result = readFloat("Insert your starting number: ")

def readFloat(message= "Your number: ") -> float:
        return float(input(message))

def add(calculator) -> None:
    calculator.result += readFloat(GENERAL_MESSAGE.format(operation = "addition"))
    calculator.print()

def subtract(calculator) -> None:
    calculator.result -= readFloat(GENERAL_MESSAGE.format(operation = "subtraction"))
    calculator.print()

def multiply(calculator) -> None:
    calculator.result *= readFloat(GENERAL_MESSAGE.format(operation = "multiplication"))
    calculator.print()

def divide(calculator) -> None:
        calculator.result /= readFloat(GENERAL_MESSAGE.format(operation = "division"))
        calculator.print()

def clear(calculator) -> None:
    print("Cleared")
    initialRead(calculator)