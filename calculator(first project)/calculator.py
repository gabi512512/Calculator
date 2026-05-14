from operations import add, subtract, multiply, divide, clear, initialRead
from evaluate_expression import evaluateExpression
from constants import INPUT_ERROR, OPERATORS

class Calculator:
    # the starting menu message
    INITIAL_MESSAGE = """The calculator has been started, if you want to stop it just type stop | quit | q
You can use 'mode' -> select the operation mode if you want to change the operation mode(more infos when you type 'mode')"""
    # modes messages
    MODES_MESSAGE = ("""Modes: 
-> 'Normal': you insert the desired operation and operand one by one
-> 'Complete': you can insert a whole expressions
Your Mode: """,
    """Options:
'add' -> addition | 'substract' -> substraction | 'multiply' -> multiplication | 'divide' -> division
'clear' -> clears the result""",
    """Just type in the expression that you want to evaluate(for example: 1+2+3*(4/5))""")
    # Error messages
    MODES_ERROR = ("ERROR: You entered an invalid mode!",
                   "ERROR: You are already in this mode!")
    
    MODES = ["Normal", "Complete"]

    def __init__(self) -> None:
        self.result = 0.0
        self.mode = None


    def start(self) -> None:
        print(Calculator.INITIAL_MESSAGE)
        self.selectMode()

        # infinite loop until you quit
        while True:
            selection = input("Your input: ").lower()
            if (selection in ("stop", "quit", "q")):
                break
            else:
                self.selector(selection)


    def selector(self, selection) -> None:
        if self.mode == "Normal":
            match selection:
                case "add":
                    add(self)
                case "substract":
                    subtract(self)
                case "multiply":
                    multiply(self)
                case "divide":
                    divide(self)
                case "clear":
                    clear(self)
                    initialRead(self)
                case _:
                    print(INPUT_ERROR[0])
        else:
            match selection:
                case "clear":
                    clear(self)
                case "mode":
                    self.selectMode()
                case _:
                    if Calculator.isExpression(selection):
                        self.result = evaluateExpression(selection)
                        print(self)
                        return
                    print(INPUT_ERROR[0])


    def selectMode(self):
        mode = input(Calculator.MODES_MESSAGE[0])
        while mode not in Calculator.MODES:
            print(Calculator.MODES_ERROR[0])
            mode = input(Calculator.MODES_MESSAGE[0])

        if mode != self.mode:
            if mode == "Normal":
                print(Calculator.MODES_MESSAGE[1])
                initialRead(self)
            else:
                print(Calculator.MODES_MESSAGE[2])
                
            if(self.mode != None):
                clear(self)
            self.mode = mode
        else:
            print(Calculator.MODES_ERROR[1])
        

    def __str__(self):
        return f"Result: {self.result:g}"


    @staticmethod
    def isExpression(selection) -> bool:
        for char in selection:
            if char in OPERATORS:
                return True
        return False