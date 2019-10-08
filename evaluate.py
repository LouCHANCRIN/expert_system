def and_function(expression, i):
    if expression[i-1] == 1 and expression[i+1] == 1:
        expression[i-1] = 1
    else:
        expression[i-1] = -1
    return expression

def or_function(expression, i):
    if expression[i-1] == 1 or expression[i+1] == 1:
        expression[i-1] = 1
    else:
        expression[i-1] = -1
    return expression

def xor_function(expression, i):
    if ((expression[i-1] == 1 and expression[i+1] == -1)
            or (expression[i-1] == -1 and expression[i+1] == 1)):
        expression[i-1] = 1
    else:
        expression[i-1] = -1
    return expression

def calcul(expression, i):
    if expression[i] == '+':
        expression = and_function(expression, i)
    if expression[i] == '|':
        expression = or_function(expression, i)
    if expression[i] == '^':
        expression = xor_function(expression, i)
    expression.remove(expression[i])
    expression.remove(expression[i])

    print(expression)
    return expression

def evaluate_expression(expression, dico, list_of_symbols):
    expression = list(expression)
    print(expression)
    # Remove < because it is useless to evaluate the expression
    if ">" in expression:
        expression.remove(">")
    if "<" in expression:
        expression.remove("<")
    # Replace characters with value 1 or -1
    for i in range(0, len(expression)):
        if expression[i] not in list_of_symbols:
            expression[i] = dico[expression[i]]
    # Turn !-1 in 1 and !1 in -1
    for i in range(0, len(expression)):
        if expression[i] == '!':
            expression[i+1] *= -1
    if "!" in expression:
        expression.remove("!")

    print(expression)
    length = len(expression)
    i = 0
    while i < length:
        if expression[i] in list_of_symbols:
           expression = calcul(expression, i)
           length -= 2
           i -= 1
        i += 1
    return int(expression[0])
