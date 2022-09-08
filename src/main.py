import sys
import os.path
from read import read_file
from format import get_dict
from moteur import inference

def main(path_to_file):
    rules, facts, queries = read_file(path_to_file)
    dictionnaire, facts, queries, initial_fatcs = get_dict(rules, facts, queries)
    inference(rules, facts, queries, dictionnaire, initial_fatcs)

if __name__ == "__main__":
    ### check number argument, one argument must be present
    if len(sys.argv) <= 1 or len(sys.argv) > 2:
        sys.exit("Missing file to analyse.\nUsage: pythonX.X example_input.txt")
    ### check if file exists
    if os.path.exists(sys.argv[1]) == False:
        sys.exit("%s doesn't exists" %sys.argv[1])
    ### check if argv is a file
    if os.path.isfile(sys.argv[1]) == False:
        sys.exit("%s isn't a file" %sys.argv[1])
    main(sys.argv[1])