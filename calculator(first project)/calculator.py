from operations import add, subtract, multiply, divide, clear, initialRead, evaluateExpression

class Calculator:
    # the starting menu message
    INITIAL_MESSAGE = """The calculator has been started, if you want to stop it just type stop | quit | q
You can use 'mode' -> select the operation mode if you want to change the operation mode(more infos when you type 'mode')
Insert your starting mode: """
    NORMAL_MESSAGE = """Options:
'add' -> addition | 'substract' -> substraction | 'multiply' -> multiplication | 'divide' -> division
'clear' -> clears the result"""
    COMPLETE_MESSAGE = """Just type in the expression that you want to evaluate(for example: 1+2+3*(4/5))"""
    MODES_MESSAGE = """Modes: 'Normal' -> you insert the desired operation and operand one by one
'Complete' -> you can insert a whole expressions
Your Mode: """
    MODES_ERROR = """ERROR: You entered an invalid mode!"""
    MODES = ["Normal", "Complete"]
    OPERATORS = {"+":1, "-":1, "*":2, "/":2} # key = operator, value = priority

    def __init__(self) -> None:
        self.result = 0.0

        initial_mode = input(Calculator.INITIAL_MESSAGE)
        if initial_mode in Calculator.MODES:
            self.mode = initial_mode
        else:
            while initial_mode not in Calculator.MODES:
                print(Calculator.MODES_ERROR)
                initial_mode = input("Your starting mode: ")
            self.mode = initial_mode


    def start(self) -> None:
        if self.mode == "Normal":
            print(Calculator.NORMAL_MESSAGE)
            initialRead(self)
        else:
            print(Calculator.COMPLETE_MESSAGE)

        # infinite loop until you quit
        while True:
            selection = input("Your input: ").lower()
            if (selection in ("stop", "quit", "q")):
                break
            else:
                self.selector(selection)


    def selector(self, selection) -> None:
        match selection:
            case "add" if self.mode == "Normal":
                add(self)
            case "substract" if self.mode == "Normal":
                subtract(self)
            case "multiply" if self.mode == "Normal":
                multiply(self)
            case "divide" if self.mode == "Normal":
                divide(self)
            case "clear":
                clear(self)
                if self.mode == "Normal":
                    initialRead(self)
            case "mode":
                self.selectMode()
            case _:
                if Calculator.isExpression(selection) and self.mode == "Complete":
                    self.result = evaluateExpression(selection)
                    print(self)
                    return
                print("Invalid option!")


    def selectMode(self):
        mode = input(Calculator.MODES_MESSAGE)
        if mode in Calculator.MODES and mode != self.mode:
            self.mode = mode
            if mode == "Normal":
                print(Calculator.NORMAL_MESSAGE)
                initialRead(self)


    def __str__(self):
        return f"Result: {self.result:g}"


    @staticmethod
    def isExpression(selection) -> bool:
        for char in selection:
            if char in Calculator.OPERATORS:
                return True
        return False