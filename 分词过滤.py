#! /usr/bin/env python 

import os
import os.path
import string

def getwords(filename, wordslst, c):
    fr = open(filename, 'r')
    alltext = fr.readlines()
    for word in alltext:
        a = word.strip().split(':')
        for i in range(len(wordslst)):
            if a[0] == wordslst[i][0]:
                wordslst[i][c+1] = a[1]
                break
        else:
            b = ['0', '0', '0', '0', '0']
            b[0] = a[0]
            b[c+1] = a[1]
            wordslst.append(b)
    fr.close()

if __name__ == '__main__' :
    filelst = []
    wordslst = []
    
    for path, folderpath, filepath in os.walk('data'):
        if (path == 'data'):
            for filename in filepath:
                if filename.endswith('.log'):
                    filelst.append(os.path.join(path, filename))

    for c in range(len(filelst)):
        print('Reading ' + filelst[c])
        getwords(filelst[c], wordslst, c)
    
    fw = open('data/dump.txt', 'w')

    for word in wordslst:
        for i in range(5):
            fw.write(word[i])
            if i != 4:
                fw.write(':')
        fw.write('\n')
    fw.close()

