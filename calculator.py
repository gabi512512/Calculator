class Calculator:
    def __init__(self):
        self.result = float(input("Your first number: "))

    def add(self):
        number = float(input("Your desired number to be added to result: "))
        self.result += number
        self.print()

    def substract(self):
        number = float(input("Your desired number to be substracted from the result: "))
        self.result -= number
        self.print()

    def multiply(self):
        number = float(input("Your desired number to multiply the result by: "))
        self.result *= number
        self.print()

    def divide(self):
        number = float(input("Your desired number to divide the result by: "))
        self.result /= number
        self.print()

    def clear(self):
        print("You choosed clear")
        self.result = float(input("Insert your starting number: "))

    def selector(self, selection):
        if (selection == "add"):
            self.add()
        elif (selection == "substract"):
            self.substract()
        elif (selection == "multiply"):
            self.multiply()
        elif (selection == "divide"):
            self.divide()
        elif (selection == "clear"):
            self.clear()
        else:
            print("Invalid option!")

    def print(self):
        if(self.result.is_integer()):
            print(int(self.result))
        else:
            print(self.result)

    def start(self):
        print("The calculator has been started, if you want to stop it just type stop"
              "Options:\n"
              "'add' -> addition | 'substract' -> substraction | 'multiply' -> multiplication | 'divide' -> division\n"
              "'clear' -> clears the result")
        while True:
            selection = input("Your selection: ").lower()
            if (selection == "stop"):
                break
            else:
                self.selector(selection)
