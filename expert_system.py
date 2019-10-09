# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expert_system.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lchancri <lchancri@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/08 15:50:35 by lchancri          #+#    #+#              #
#    Updated: 2019/10/09 13:41:33 by lchancri         ###   ########.fr        #
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

#def evaluate_2(dico, line, list_of_symbols):
#    if_and_only_if = False
#    if "<=>" in line:
#        if_and_only_if = True
#    expression = line.split("=")
#    if if_and_only_if == True:
#        tmp = expression[0]
#        expression[0] = expression[1]
#        expression[1] = tmp
#    first = evaluate.evaluate_expression(expression[0], dico, list_of_symbols)
#    return first
#    second = evaluate.evaluate_expression(expression[1], dico, list_of_symbols)
#    print(first)
#    print(second)
#    print("Expression   :", expression)
#    print("Dictionnaire :", dico)
#    print("\n")
#    return dico

#def algo(fichier, dico, target, list_of_symbols):
#    exceptions = ['=', '?', '#']
#    for line in fichier:
#        if line == '' or line[0] in exceptions:
#            pass
#        else:
#            dico = evaluate_2(dico, line, list_of_symbols)

#def vrai_algo(word, fichier, dico, list_of_symbols):
#    functions = []
#    print("Word :", word)
#    for i in range(0, len(fichier)):
#        if check_if_usefull(fichier[i], word) == True:
#            functions.append(i)
#    print(functions)
#    for i in functions:
#        for j in range(0, len(functions[i])):
#            if functions[i][j] not in list_of_symbols and dico[functions[i][j]] == -1:
#                dico[functions[i][j]] = vrai_algo(functions[i][j], fichier, dico, list_of_symbols)
#        value = evaluate_2(dico, fichier[i], list_of_symbols)
#        if value == 1:
#            return 1
#        print("Value :", value)
#        print(fichier[i])
#    return -1





def evaluate_2(dico, expression, list_of_symbols):
    first = evaluate.evaluate_expression(expression, dico, list_of_symbols)
    #second = evaluate.evaluate_expression(expression[1], dico, list_of_symbols)
    return first

def check_if_usefull(line, target):
    if line == '' or line[0] == '=' or line[0] == '?':
        return False
    expression = line.split("=")
    for i in range(0, len(expression[1])):
        if expression[1][i] == target:
            return True
    return False

def vrai_algo(word, fichier, dico, list_of_symbols, mots):
    functions = []
    mots.append(word)
    for function in fichier:
        if check_if_usefull(function, word) == True:
            functions.append(function)
    #print(functions)
    for function in functions:
        for i in range(0, len(function)):
            if (function[i] not in list_of_symbols and dico[function[i]] == -1
                    and function[i] not in  mots):
                mot = function[i]
                dico[mot] = vrai_algo(mot, fichier, dico, list_of_symbols, mots)
        value = evaluate_2(dico, function, list_of_symbols)
        if value == 1:
            print(function, ":", value)
            return 1
        print(function)
    return -1

def main():
    try:
        file_path = sys.argv[1]
    except:
        print("Il faut donner un fichier au script")
    list_of_symbols = ['(', ')', '!', '+', '|', '^', '=', '>', '<', '?']
    fichier, dico, target = parse.parse(file_path, list_of_symbols)
    print('\n')
    for word in target:
        print("Word :", word)
        target = vrai_algo(word, fichier, dico, list_of_symbols, [])
        print("Règle " + word + " :", target, "\n\n")
#    target = algo(fichier, dico, target, list_of_symbols)

if __name__ == "__main__":
    main()
