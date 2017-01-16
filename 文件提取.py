#! /usr/bin/env python
#  Separate words of texts 

import os
import os.path
import codecs
import re

def count(path, filename, wordlist):
    fr = codecs.open(os.path.join(path,filename), 'r', encoding='utf-8', errors='ignore')
    try:
        alltext = fr.read()
        allwords = re.split('\W+', alltext)

        for word in allwords:
            if (word.isspace()):
                continue
            elif not word.isalnum():
                continue
            elif word.isdigit():
                continue

            loword = word.lower()

            if loword in wordlist:
                wordlist[loword] += 1
            else:
                wordlist[loword] = 1

    finally:
        fr.close()

def writelog(logname, dictlst):
    fw = open(logname, 'w')
    for word in dictlst:
        fw.write('%s:%d\n' % (word[0], word[1]))
    fw.close()
    return

if __name__ == '__main__' :
    for path, folderpath, filepath in os.walk('data'):
        if (path == 'data'):
            continue

        wordlist = {} 
        for filename in filepath:
            if (filename.startswith('.')):
                continue
            count(path, filename, wordlist)
        
        dictlst = sorted(wordlist.items(), key=lambda d:d[1], reverse = True)
        logname = path + '.log'
        writelog(logname, dictlst)
