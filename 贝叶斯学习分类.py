#! /usr/bin/env python

import os
import codecs
import re

def getmax(py):
    pymax = 0
    for n in range(3):
        if py[pymax]<py[n+1]:
            pymax = n+1
    return pymax

def classify(filename, training, pc):
    fr = codecs.open(filename, 'r', encoding='utf-8', errors='ignore')
    readtext = fr.read()
    fr.close()

    py = [pc[0],pc[1],pc[2],pc[3]]

    readwords = re.split('\W+', readtext)
    for word in readwords:
        if (word.isspace()):
            continue
        elif not word.isalnum():
            continue
        elif word.isdigit():
            continue
        elif word in filtered:
            continue

        loword = word.lower()

        for n in range(len(training)):
            if loword == training[n][0]:
                for c in range(4):
                    py[c] *= training[n][c+1]

    
    print(filename)
    print(getmax(py))


if __name__ == '__main__' :
    readlst = []

    # Reading the filtered words
    filtered = []
    fr = open('data/passed.txt', 'r')
    for i in fr.readlines():
        filtered.append(i.strip().split(':')[0])
    fr.close()

    # Reading data of wordlist
    fr = open('data/stayed.txt', 'r')
    for i in fr.readlines():
        readlst.append(i.strip().split(':'))
    fr.close()
wordlst = []

    for word in readlst:
        a = []
        a.append(word[0])
        for n in range(1, 5):
            a.append(float(word[n])+1)
        wordlst.append(a)

    # |Vocabulary| of words
    vocabulary = len(readlst)
    # P(ck)
    pc = [100/400, 100/400, 100/400, 100/400]
    # length of every class by words
    sumclass = [0, 0, 0, 0]
    # 
    sumtotal = 0

    for word in wordlst:
        for n in range(4):
            sumclass[n] += word[n+1]
            sumtotal += word[n+1]

    training = []
    for word in wordlst:
        a = []
        a.append(word[0])
        for n in range(4):
            a.append(word[n+1]/sumclass[n]*10000)
        training.append(a)

    # classify
    for path, folderpath, filepath in os.walk('data'):
        if (path == 'data'):
            continue
        for filename in filepath:
            if (filename.startswith('.')):
                continue

            classify(os.path.join(path,filename), training, pc)
