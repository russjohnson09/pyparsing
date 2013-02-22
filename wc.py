from __future__ import print_function
from sys import argv
from operator import itemgetter


def word_count(file_path, string):
    wc = {}
    with open(file_path,"r") as f:
        print(string)
        for line in f:
            tup = line.split()
            if len(tup) > 3:
                #two characters in unicode is 6 long
                word_type = tup[3][:6]
                word = tup[2]
                if wc.has_key(word) and word_type == string:
                    wc[word] += 1
                elif word_type == string:
                    wc[word] = 1
    return wc
    


if __name__ == "__main__":
    wc = word_count(argv[1], argv[2])
    top_words = sorted(wc.items(), key=itemgetter(1),
                 reverse=True)[:int(argv[3])]
    for word, frequency in top_words:
        print ("%s %d" % (word, frequency))
