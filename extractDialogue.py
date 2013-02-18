from sys import argv
from pyparsing import *

dia_parser = ( "Dialogue:" + Word(nums + ",:.") + 
             Word(alphas).setResultsName('type_of_dia') + 
             "," + Word(alphas) + "," + Word(nums+",",exact=5)
             + Word(nums+",",exact=5) + Word(nums+",",exact=5) 
             + "," + Optional(Word(alphas+nums+"{}\\")) + restOfLine.setResultsName('dialogue') )




def print_dialogue(file_path):
    with open(file_path,"r") as f:
        for line in f:
            if line[0:3] == "Dia":
                dia = dia_parser.parseString(line)
                if dia.type_of_dia == "riwen":
                    print dia.dialogue
    


if __name__ == "__main__":
    print_dialogue(argv[1])
