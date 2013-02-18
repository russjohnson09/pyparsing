from __future__ import print_function
from sys import argv

def newline(file_path, seperator, num):
    with open(file_path,"r") as f:
        for line in f:
            line = line.rstrip()
            print(line,end="")
            for i in range(num):
                print(seperator,end="")
            print(" ",end="")
    


if __name__ == "__main__":
    newline(argv[1], argv[2], int(argv[3]))
