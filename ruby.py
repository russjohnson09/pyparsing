#!/usr/local/bin/python
#coding: utf-8

#Converts a file to rubystyle using chasen.
from __future__ import print_function
from sys import argv

from pyparsing import *
from subprocess import check_output


ruby_parser = (CharsNotIn(u"()、！…。"+unichr(32) + unichr(10)).setResultsName("word") + "(" +
              CharsNotIn("()").setResultsName("kana") +  ")")

def chasen_call(file_path):
    return check_output('chasen -i w -F "%r ()" <' + file_path,
                shell=True).decode('utf-8')

def convert_string(string):
    start = 0
    result = ""
    for t,s,e in ruby_parser.scanString(string):
        if start != s:
            result += string[start:s]
        start = e
        i,j = match(t.word,t.kana)
        if i == None:
            result += format("%s" % (t.word))
            print("%s" % (t.word), end="")
            pass
        elif i == -1:
            result += format("%s{%s}" % (t.word,t.kana))
            print("%s{%s}" % (t.word,t.kana), end = "\n")
        else:
            result += format("%s{%s}%s" % (t.word[:i],t.kana[:i],t.word[i:]))
            print("%s{%s}%s" % (t.word[:i],t.kana[:i],t.word[i:]), end="\n")
            pass
    return result + string[start:]

def match(word,kana):
    word_kana = ""
    for c in word:
        # is in hiragana range
        if ord(u'ぁ') <= ord(c) and ord(c) <= ord(u'ゖ'):
            word_kana += unichr(ord(c) + (ord(u'ァ')-ord(u'ぁ')))
        else:
            word_kana += c
#    print(word_kana)
    if word_kana == kana:
        return None, None
    else:
        #print("w: %s, wk: %s, k: %s" % (word,word_kana,kana))
        return match2(word_kana,kana)

def match2(w1,w2):
    for i in range(len(w1)):
        for j in range(len(w2)):
            if w1[i:] == w2[j:]:
                return i,j
    return -1,-1
            

if __name__ == "__main__":
    string = chasen_call(argv[1])
    string = convert_string(string)
    print(string,end="")



