import sys
import parse

'''
() = priority order
! = NOT
+ = AND
| = OR
^ = XOR
=> implies
<=> if and only if (implies in both way)
'''

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

def evaluate_1(expression, dico, list_of_symbols):
    expression = list(expression)
    print(expression)
    # Remove < because it is useless to evaluate the expression
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

def evaluate(dico, line, list_of_symbols):
    expression = line.split("=")
    first = evaluate_1(expression[0], dico, list_of_symbols)
#    dico = evaluate_2(expression[1], dico, first)
    print("Expression   :", expression)
    print("Dictionnaire :", dico)
    print("\n")
    return dico

def algo(fichier, dico, target, list_of_symbols):
    exceptions = ['=', '?', '#']
    for line in fichier:
        if line == '' or line[0] in exceptions:
            pass
        else:
            dico = evaluate(dico, line, list_of_symbols)

def main():
    try:
        file_path = sys.argv[1]
    except:
        print("Il faut donner un fichier au script")
    list_of_symbols = ['(', ')', '!', '+', '|', '^', '=', '>', '<', '?']
    fichier, dico, target = parse.parse(file_path, list_of_symbols)
    print('\n')
    target = algo(fichier, dico, target, list_of_symbols)

if __name__ == "__main__":
    main()
