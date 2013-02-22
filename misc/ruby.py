#!/usr/local/bin/python
#coding: utf-8

#Converts a file to rubystyle using chasen.
from __future__ import print_function
from sys import argv

import codecs

from pyparsing import *
from subprocess import *


ruby_parser = (CharsNotIn(u"()、！…。」「"+unichr(32) + unichr(10) + unichr(11) + unichr(12) + unichr(13)).setResultsName("word") + "(" +
              CharsNotIn("()").setResultsName("kana") +  ")")

def chasen_call(file_path):
    with open(".temp", "w") as f1, open(file_path,'r') as f2:
        p = Popen(['chasen', '-i', 'w', '-F', '%r ()'], stdout=f1, stdin=f2)
        p.wait()

def convert_file(fout):
    with open(".temp", "r") as f1, codecs.open(fout,'a','utf-8-sig') as f2:
        f2.flush()
        for line in f1:
            string = convert_string(line.decode('utf-8'))
            f2.write(string)
        

def convert_string(string, hiragana = True, ruby = False):
    start = 0
    result = ""
    for t,s,e in ruby_parser.scanString(string):
        if start != s:
            result += string[start:s]
        start = e
        i,j = match(t.word,t.kana)
        if hiragana:
            kana = ""
            for c in t.kana:
                kana += unichr(ord(c)-(ord(u'ァ')-ord(u'ぁ')))
        else:
            kana = t.kana
                
        if i == None:
            result += format("%s" % (t.word))
        elif i == -1:
            if ruby:
                result += format("\\ruby{%s}{%s}" % (t.word,kana))
            else:
                result += format("%s(%s)" % (t.word,kana))
        else:
            if ruby:
                result += format("\\ruby{%s}{%s}%s" % (t.word[:i],
                                kana[:j],t.word[i:]))
            else:
                result += format("%s(%s)%s" %
                        (t.word[:i],kana[:j],t.word[i:]))

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
#    print(kana)
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
#    chasen_call(argv[1])
    convert_file(argv[2])



