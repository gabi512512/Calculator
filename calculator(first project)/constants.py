import math

OPERATORS = {"+":1, "-":1, "*":2, "/":2} # key = operator, value = priority
CONSTANTS = {
    "pi": math.pi,
    "e":  math.e
}

INPUT_ERROR = ("ERROR: Invalid option!",
               "ERROR: Invalid input expression!")