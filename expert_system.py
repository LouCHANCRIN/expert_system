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

def algo(fichier, dico, target):
    exceptions = ['=', '?']
    for line in fichier:
        if line == '' or line[0] in exceptions:
            pass
        else:
            print('a')

def main():
    try:
        file_path = sys.argv[1]
    except:
        print("Il faut donner un fichier au script")
    fichier, dico, target = parse.parse(file_path)
    target = algo(fichier, dico, target)

if __name__ == "__main__":
    main()
