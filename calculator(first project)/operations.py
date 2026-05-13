import math

GENERAL_MESSAGE = "Operation: {operation} | Your number: "
CONSTANTS = {
    "pi": math.pi,
    "e": math.e
}

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


def evaluateExpression(selection) -> float:
    # Shunting yard algorithm
    from calculator import Calculator
    postfix = []
    operators = []
    operands = []
    buffer = ""
    for char in selection:
        # numbers
        if char.isnumeric() or char == ".":
            buffer += char

        # when we ecounter a (
        elif char == "(":
            if buffer != "":
                postfix.append(float(buffer))
                buffer = ""
            operators.append(char)
        
        # when we encounter a )
        elif char == ")":
            if buffer != "":
                postfix.append(float(buffer))
                buffer = ""
            item = operators.pop()
            while(item != "("):
                postfix.append(item)
                item = operators.pop()
            item = ""
        
        # when we encounter an operator
        elif char in Calculator.OPERATORS:
            if buffer != "":
                postfix.append(float(buffer))
                buffer = ""
            if not operators:
                operators.append(char)
            else:
                while operators and operators[-1] != "(" and Calculator.OPERATORS.get(char) <= Calculator.OPERATORS.get(operators[-1]):
                    postfix.append(operators.pop())
                operators.append(char)
    
    if buffer != "":
        postfix.append(float(buffer))
        buffer = ""
    
    while operators:
        postfix.append(operators.pop())

    print(postfix)

    for item in postfix:
        if isinstance(item, float):
            operands.append(item)
        else:
            a = operands.pop()
            b = operands.pop()
            match item:
                case "+": aux = a + b
                case "-": aux = b - a
                case "*": aux = a * b
                case "/": aux = b / a
            operands.append(aux)

    return operands[0]