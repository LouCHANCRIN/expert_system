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

def not_function(dico, line):
    print("NOT")

def calcul(expression, i):
    return expression

def evaluate_1(expression, dico, list_of_symbols):
    expression = list(expression)
    print(expression)
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
    for i in range(0, len(expression)):
        if expression[i] in list_of_symbols:
           expression = calcul(expression, i)

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
