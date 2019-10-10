# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    evaluate.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lchancri <lchancri@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/08 17:23:50 by lchancri          #+#    #+#              #
#    Updated: 2019/10/10 15:52:47 by lchancri         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def clean(expression):
    # Remove <, >, ! because we dont need them anymore to evaluate
    if ">" in expression:
        expression.remove(">")
    if "<" in expression:
        expression.remove("<")
    length = len(expression)
    i = 0
    while i < length:
        if expression[i] == '!' and expression[i+1] not in ['(', ')']:
            del expression[i]
            i -= 1
            length -= 1
        i += 1
    return expression

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
    del expression[i]
    del expression[i]
    return expression

def index_parenthese(expression):
    a = 0
    b = 0
    for i in range(0, len(expression)):
        if expression[i] == ')':
            b = i
            break
    for i in range(b, 0, -1):
        if expression[i] == '(':
            a = i
            break
    return a, b + 1

def calcul_parenthese(expression):
# Fait les calcul dans les parenthèses
    length = len(expression)
    i = 0
    while ("(" or ")") in expression:
        a, b = index_parenthese(expression)
        result = calcul(expression[a+1:b-1], 1)
        while b > a + 1:
            del expression[a]
            b -= 1
        if a > 0 and expression[a-1] == '!':
            del expression[a]
            expression[a-1] = result[0] * -1
        else:
            expression[a] = result[0]
    return(expression)

def evaluate_expression(expression, dico, list_of_symbols):
    expression = list(expression)
    # Replace characters with value 1 or -1
    for i in range(0, len(expression)):
        if expression[i] not in list_of_symbols:
            expression[i] = dico[expression[i]]
    # Turn !-1 in 1 and !1 in -1
    for i in range(0, len(expression)):
        if expression[i] == '!' and expression[i+1] not in ['(', ')']:
            expression[i+1] *= -1
    expression = clean(expression)
    expression = calcul_parenthese(expression)
    length = len(expression)
    i = 0
    while i < length:
        if expression[i] in list_of_symbols:
            expression = calcul(expression, i)
            length -= 2
            i -= 1
        i += 1
    return int(expression[0])
