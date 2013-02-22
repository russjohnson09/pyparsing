from __future__ import print_function
from sys import argv
import codecs



def newline(file_path, seperator, num):
    output = file_path + ".wikia"
    with codecs.open(file_path,"r","utf-8") as f, codecs.open(output, "w", "utf-8") as fout:
        for line in f:
            fout.write(line.rstrip())
            for i in range(num):
                fout.write(seperator)
    


if __name__ == "__main__":
    newline(argv[1], argv[2], int(argv[3]))
