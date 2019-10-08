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

def fill_dict(dico, target, line, list_of_symbols):
    if line == '' or line[0] == '#':
        return dico, target
    if line[0] == '?':
        target = loop(target, line, None, list_of_symbols)
    else:
        if line[0] == '=':
            value = 1
        else:
            value = -1
        dico = loop(dico, line, value, list_of_symbols)
    return dico, target

def clear_text(split):
    length = len(split)
    i = 0
    while i < length:
        line = split[i]
        if line == "" or line[0] == '#':
            split.remove(split[i])
            length -= 1
            i -= 1
        else:
            for j in range(0, len(line)):
                if line[j] == '#':
                    split[i] = line[:j]
                    print(line)
                    break
        i += 1
    return split

def parse(file_path, list_of_symbols):
    fichier = read_file(file_path)
    fichier = fichier.strip()
    fichier = fichier.replace(" ", "")
    split = fichier.split('\n')
    dico = {}
    target = {}
    split = clear_text(split)
    for line in split:
        dico, target = fill_dict(dico, target, line, list_of_symbols)
    print(dico)
    print(target)
    return split, dico, target

