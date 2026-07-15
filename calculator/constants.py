import math

OPERATORS = {"+":1, "-":1, "*":2, "/":2} # key = operator, value = priority
CONSTANTS = {
    "pi": math.pi,
    "e":  math.e
}

INPUT_ERROR = ('<span style="color:#CC0606;">ERROR:</span> Input is not a number!',
               '<span style="color:#CC0606;">ERROR:</span> Division to 0!')