from sys import argv
from pyparsing import *
import codecs
from subprocess import Popen

#usage: name of file to extract

dia_parser = ( "Dialogue:" + Word(nums + ",:.") + 
             Word(alphas+nums).setResultsName('type_of_dia') + 
             "," + Word(alphas) + "," + Word(nums+",",exact=5)
             + Word(nums+",",exact=5) + Word(nums+",",exact=5) 
             + "," + Optional(Word(alphas+nums+"{}\\")) + restOfLine.setResultsName('dialogue') )




def print_dialogue(file_path, encoding="utf-8", string="riwen"):
    output = "./out/" + file_path+".out"
    if encoding != "utf-8":
        convert(file_path)
        file_path = 'temp'
    with codecs.open(file_path,"r", 'utf-8') as f, codecs.open(output,"w", 'utf-8') as fout:
        for line in f:
            if line[0:3] == u"Dia":
                dia = dia_parser.parseString(line)
                if dia.type_of_dia == string:
                    fout.write(dia.dialogue)
    
def convert(file_path):
    with codecs.open("temp",'w', encoding='utf-8') as fout:
        p = Popen(['iconv', '-f', 'utf-16', 
            '-t', 'utf-8', file_path], stdout=fout)
        p.wait()


if __name__ == "__main__":
    if len(argv) == 4:
        print_dialogue(argv[1], argv[2], argv[3])
    elif len(argv) == 3:
        print_dialogue(argv[1], argv[2])
    else:
        print_dialogue(argv[1])
