import sys

def read_file(file_path):
    f = open(file_path, "r")
    fichier = f.read()
    f.close()
    return fichier

def loop(to_fill, line, value, list_of_symbols):
    for i in range(0, len(line)):
        if line[i] not in list_of_symbols:
            try:
                to_fill[line[i]] = value
            except Exception as e:
                pass
    return to_fill

def fill_dict(dico, target, line):
    if line == '' or line[0] == '#':
        return dico, target
    list_of_symbols = ['(', ')', '!', '+', '|', '^', '=', '>', '<', '?']
    if line[0] == '?':
        target = loop(target, line, None, list_of_symbols)
    else:
        if line[0] == '=':
            value = True
        else:
            value = False
        dico = loop(dico, line, value, list_of_symbols)
    return dico, target

def parse(file_path):
    fichier = read_file(file_path)
    fichier = fichier.strip()
    fichier = fichier.replace(" ", "")
    split = fichier.split('\n')
    dico = {}
    target = {}
    for line in split:
        dico, target = fill_dict(dico, target, line)
    print(dico)
    print(target)
    return fichier, dico, target

