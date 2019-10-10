# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expert_system.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lchancri <lchancri@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/08 15:50:35 by lchancri          #+#    #+#              #
#    Updated: 2019/10/10 17:12:18 by lchancri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import parse
import evaluate
import copy

'''
() = priority order
! = NOT
+ = AND
| = OR
^ = XOR
=> implies
<=> if and only if
'''

def check(conclusion, i, length):
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
            a = check(conclusion, i, length)
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

def check_contradiction(functions, values, word, dico):
    for i in range(0, len(values)):
        print(functions[i], "}--->>>", word, "=", values[i])
    if not values:
        #print("Est-ce un cas indefini lorsqu'il n'y a pas d'expression permettant de déterminer la valeur d'une lettre ?")
        return -1
    if 1 in values and -1 in values:
        print("Il y a une contradiction")
        #for i in range(0, len(values)):
        #    print(functions[i], "=", values[i])
        return -2
    if 1 in values:
        #for i in range(0, len(values)):
        #    if values[i] == 1:
        #        print(functions[i], '-->', word, ": 1")
        #        return 1
        return 1
    if 0 in values:
        #for i in range(0, len(values)):
        #    if values[i] == 0:
        #        print(functions[i], '-->', word, ": 0")
        #        return 0
        return 0
    #for i in range(0, len(values)):
    #    if values[i] == -1:
    #        print(functions[i], "-->", word, ": -1")
    return -1

def algo(word, fichier, dico, list_of_symbols, mots):
    functions = []
    mots.append(word)
    for function in fichier:
        if check_if_usefull(function, word) == True:
            functions.append(function)
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
    return check_contradiction(functions, values, word, dico)

def main():
    try:
        file_path = sys.argv[1]
    except:
        print("Il faut donner un fichier au script")
    list_of_symbols = ['(', ')', '!', '+', '|', '^', '=', '>', '<', '?']
    fichier, dico, target = parse.parse(file_path, list_of_symbols)
    for word in target:
        #print("Word :", word)
        tmp = copy.copy(dico)
        print(dico)
        target = algo(word, fichier, tmp, list_of_symbols, [])
        if target == 1:
            print("Règle " + word + " : Vraie\n")
        if target == 0:
            print("Règle " + word + " : Indéfinie\n")
        if target == -1:
            print("Règle " + word + " : Fausse\n")
        if target == -2:
            print("Règle " + word + " : Il y a eu une contradiction\n")

if __name__ == "__main__":
    try:
        sys.argv[2]
        print("Il ne doit y avoir qu'un seul argument : le chemin du fichier.")
    except:
        main()
