# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expert_system.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lchancri <lchancri@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/08 15:50:35 by lchancri          #+#    #+#              #
#    Updated: 2019/10/09 17:02:28 by lchancri         ###   ########.fr        #
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

#def algo(word, fichier, dico, list_of_symbols, mots):
#    functions = []
#    mots.append(word)
#    for function in fichier:
#        if check_if_usefull(function, word) == True:
#            functions.append(function)
    #print(functions)
#    for function in functions:
#        tmp = function.split("=")
#        for i in range(0, len(function)):
#            if (function[i] not in list_of_symbols and dico[function[i]] == -1
#                    and function[i] not in  mots):
#                mot = function[i]
#                dico[mot] = algo(mot, fichier, dico, list_of_symbols, mots)
#        value = evaluation(dico, function, list_of_symbols, word)
#        if value == 1:
#            print(function, ":", value)
#            return 1
#        print(function, ":", -1)
#    return -1

def check(word, conclusion, i, length):
    undefined = ['^', '|']
    if ((i > 0 and conclusion[i-1] in undefined)
            or (i < length - 1 and conclusion[i+1] in undefined)):
        return 0
    if ((i > 1 and conclusion[i-1] == '!' and conclusion[i-2])):
        return -1
    return 1


def evaluation(dico, expression, conclusion, list_of_symbols, word):
    first = evaluate.evaluate_expression(expression, dico, list_of_symbols)
    if first == -1:
        return -1
    length = len(conclusion)
    for i in range(0, length):
        if conclusion[i] == word:
            a = check(word, conclusion, i, length)
            if a != 1:
                return a
    return 1

def check_if_usefull(line, target):
    if line == '' or line[0] == '=' or line[0] == '?':
        return False
    expression = line.split("=")
    for i in range(0, len(expression[1])):
        if expression[1][i] == target:
            return True
    return False

def check_contradiction(functions, values, word):
    if 1 in values and -1 in values:
        print("Il y a un contradiction")
        for i in range(0, len(values)):
            print(functions[i], "=", values[i])
        return -2
    if 1 in values:
        for i in range(0, len(values)):
            if values[i] == 1:
                print(functions[i], ':', word, ": 1")
                return 1
    if 0 in values:
        for i in range(0, len(values)):
            if values[i] == 1:
                print(functions[i], ':', word, ": 1")
                return 0
        #print(word, ": 0")
        #return 0 
    print(word, ": -1")
    return -1


def algo(word, fichier, dico, list_of_symbols, mots):
    functions = []
    mots.append(word)
    for function in fichier:
        if check_if_usefull(function, word) == True:
            functions.append(function)
    indetermine = 0
    values = []
    for function in functions:
        expression, conclusion = function.split("=")
        for i in range(0, len(expression)):
            if (expression[i] not in list_of_symbols
                    and dico[expression[i]] == -1
                    and expression[i] not in  mots):
                mot = expression[i]
                dico[mot] = algo(mot, fichier, dico, list_of_symbols, mots)
        value = evaluation(dico, expression, conclusion, list_of_symbols, word)
        values.append(value)
    return check_contradiction(functions, values, word)
        #if value == 1:
        #    print(function, ":", word, "=", value)
        #    return 1
        #if value == 0:
        #    indetermine = 1
        #print(function, ":", word, "=", value)
    #if indetermine == 1:
    #    print(word, "est indeterminé.")
    #    return 0
    #return -1

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
        target = algo(word, fichier, dico, list_of_symbols, [])
        print("Règle " + word + " :", target, "\n")

if __name__ == "__main__":
    main()
