# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expert_system.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lchancri <lchancri@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/08 15:50:35 by lchancri          #+#    #+#              #
#    Updated: 2019/10/08 19:04:29 by lchancri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
<=> if and only if
'''

def change_dict_value(expression, dico, first):
    return dico

def evaluate_2(dico, line, list_of_symbols):
    if_and_only_if = False
    if "<=>" in line:
        if_and_only_if = True
    expression = line.split("=")
    if if_and_only_if == True:
        tmp = expression[0]
        expression[0] = expression[1]
        expression[1] = tmp
    first = evaluate.evaluate_expression(expression[0], dico, list_of_symbols)
    second = evaluate.evaluate_expression(expression[1], dico, list_of_symbols)
    print(first)
    print(second)
    dico = change_dict_value(expression[1], dico, first)
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
