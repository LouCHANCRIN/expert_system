import sys
import parse
import evaluate

'''
() = priority order
! = NOT
+ = AND
| = OR
^ = XOR
=> implies
<=> if and only if (implies in both way)
'''

def change_dict_value(expression, dico, first, if_and_only_if):

    return dico

def evaluate_2(dico, line, list_of_symbols):
    if "<=>" in line:
        if_and_only_if = True
    else:
        if_and_only_if = False
    expression = line.split("=")
    first = evaluate.evaluate_expression(expression[0], dico, list_of_symbols)
    print(first)
    dico = change_dict_value(expression[1], dico, first, if_and_only_if)
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
            dico = evaluate_2(dico, line, list_of_symbols)

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
