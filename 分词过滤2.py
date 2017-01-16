#! /usr/bin/env python
#  Separate words of texts 

import os
import os.path

def notbalance(word):
    num = []
    for i in range(1, 5):
        num.append(float(word[i]))

    for n in num:
        if n < 10:
            return True
    else:
        fsum = sum(num)
        for n in num:
            if n/fsum > 0.65:
                return True
        else:
            return False

def filtered(word, stayed, passed):
    if notbalance(word):
        stayed.append(word)
    else:
        passed.append(word)


if __name__ == '__main__' :
    wordslst = []
    fr = open('data/dump.txt', 'r')
    for i in fr.readlines():
        wordslst.append(i.strip().split(':'))
    fr.close()

    stayed = []
    passed = []
    for word in wordslst:
        filtered(word, stayed, passed)

    fs = open('data/stayed.txt', 'w')
    fp = open('data/passed.txt', 'w')

    for word in stayed:
        for i in range(5):
            fs.write(word[i])
            if i != 4:
                fs.write(':')
        fs.write('\n')

    for word in passed:
        for i in range(5):
            fp.write(word[i])
            if i != 4:
                fp.write(':')
        fp.write('\n')

    fs.close()
    fp.close()

