from constants import CONSTANTS

GENERAL_MESSAGE = "Operation: {operation} | Your number: "
    

def readFloat(message= "Your number: ") -> float:
    inputVal = input(message).lower()
    if inputVal in CONSTANTS:
        inputVal = CONSTANTS[inputVal]
    return float(inputVal)


def initialRead(calculator) -> None:
    calculator.result = readFloat("Insert your starting number: ")


def add(calculator) -> None:
    calculator.result += readFloat(GENERAL_MESSAGE.format(operation = "addition"))
    print(calculator)


def subtract(calculator) -> None:
    calculator.result -= readFloat(GENERAL_MESSAGE.format(operation = "subtraction"))
    print(calculator)


def multiply(calculator) -> None:
    calculator.result *= readFloat(GENERAL_MESSAGE.format(operation = "multiplication"))
    print(calculator)


def divide(calculator) -> None:
    calculator.result /= readFloat(GENERAL_MESSAGE.format(operation = "division"))
    print(calculator)


def clear(calculator) -> None:
    calculator.result = 0
    print("Cleared")