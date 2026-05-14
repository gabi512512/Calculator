from constants import OPERATORS, INPUT_ERROR

def evaluateExpression(selection) -> float:
    selection = selection.replace(" ", "") # get rid of blank spaces
    # Shunting yard algorithm
    postfix = []
    operators = []
    operands = []
    buffer = ""
    i = 0
    while i < len(selection):
        char = selection[i]
        # numbers
        if char.isnumeric() or char == ".":
            buffer += char
            
            if(selection[i+1]) == "(":
                operators.append("*")
                postfix.append(float(buffer))
                buffer = ""

        # when we ecounter a (
        elif char == "(":
            if buffer != "":
                postfix.append(float(buffer))
                buffer = ""
            operators.append(char)

            # special case for when we write for example 1*(-2)
            if selection[i+1] == "-":
                buffer += "-"
                i += 1 # we skip the "-" in the expression
        
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

            if i+1 < len(selection) and selection[i+1] == "(":
                operators.append("*")
        
        # when we encounter an operator
        elif char in OPERATORS:
            if buffer != "":
                postfix.append(float(buffer))
                buffer = ""
            if not operators:
                operators.append(char)
            else:
                while operators and operators[-1] != "(" and OPERATORS.get(char) <= OPERATORS.get(operators[-1]):
                    postfix.append(operators.pop())
                operators.append(char)

        # when we encounter an invalid character
        else:
            print(INPUT_ERROR[1])
            return 0
        i += 1

    # adding the remaining operators+operands in the final post-fixed form
    if buffer != "":
        postfix.append(float(buffer))
        buffer = ""
    
    while operators:
        postfix.append(operators.pop())
    # here we have a final post-fixed form
    print(postfix)
    # the solver for the post-fixed form
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

    return operands[0] # we return the final result, which will be on the first position