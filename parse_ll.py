from collections import namedtuple
import string
import sys

''' Documentation : https://eli.thegreenplace.net/2012/08/02/parsing-expressions-by-precedence-climbing'''

OpInfo = namedtuple('OpInfo', 'prec assoc')

priority_order = {'^': OpInfo(1, "LEFT"),
                  '|': OpInfo(2, "LEFT"),
                  '+': OpInfo(3, "LEFT"),
                  '!': OpInfo(4, "LEFT"),
                  '(': OpInfo(5, "LEFT"),
                  ')': OpInfo(5, "LEFT")}

Tok = namedtuple('Tok', 'name value')

class tokenizer():

    def __init__(self, expression):
        self.token_generator = self.generate_token(expression)
        self.cur_token = None

    def get_next_token(self):
        try:
            self.cur_token = next(self.token_generator)
        except StopIteration:
            self.cur_token = None
        return self.cur_token

    def generate_token(self, expression):
        for char in expression:
            if char.isalpha():
                yield Tok("ALPHA", char)
            elif char == '(':
                yield Tok("PARENTHESE_GAUCHE", char)
            elif char == ')':
                yield Tok("PARENTHESE_DROITE", char)
            else:
                yield Tok("OPETATEUR", char)


def xor_op(left, right):
    if ((left == True and right == False)
        or (left == False and right == True)):
        return True
    return False

def or_op(left, right):
    if left == True or right == True:
        return True
    return False

def and_op(left, right):
    if left == True and right == True:
        return True
    return False

def compute_op(op, left, right):
    if op == '^':   return xor_op(left, right)
    elif op == '|': return or_op(left, right)
    elif op == '+': return and_op(left, right)
    #elif op == '!': return not_op(left, right)
    else:
        parse_error('unknown operator "%s"' % op)






def calcul(tokens):
    return


def read_file(file_path):
    f = open(file_path, "r")
    fichier = f.read()
    f.close()
    return fichier

def create_ast(file_path):
    fichier = read_file(file_path)
    fichier = fichier.strip()
    fichier = fichier.replace(" ", "")
    split = fichier.split('\n')
    split.remove("")
    for line in split:
        tokens = tokenizer(line)
        t = tokens.get_next_token()
        ast = calcul(t)

def main():
    trees = create_ast(sys.argv[1])

if __name__ == "__main__":
    main()