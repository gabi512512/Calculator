from operations import add, subtract, multiply, divide, clear, initialRead

class Calculator:
    # the starting menu message
    INITIAL_MESSAGE = """The calculator has been started, if you want to stop it just type stop | quit | q
Options:
'add' -> addition | 'substract' -> substraction | 'multiply' -> multiplication | 'divide' -> division
'clear' -> clears the result"""

    def __init__(self):
        self.result = 0.0

    def selector(self, selection):
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
            case _:
                print("Invalid option!")

    def print(self):
        if(self.result.is_integer()):
            print(int(self.result))
        else:
            print(self.result)

    def start(self):
        print(self.INITIAL_MESSAGE)
        initialRead(self)

        # infinite loop until you quit
        while True:
            selection = input("Your selection: ").lower()
            if (selection in ("stop", "quit", "q")):
                break
            else:
                self.selector(selection)