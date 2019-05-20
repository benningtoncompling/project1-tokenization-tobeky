#!/usr/bin/env python3


import re

file_name = "Wikipedia-LexicalAnalysis.xml"
out_file_name = "lexical_analysis_out.txt"

with open(file_name, 'r') as open_book:
    with open(out_file_name, 'w') as open_out_book:
        text = open_book.read()
        text = re.sub(r'<[^(><)]+>', r'', text)
        text = re.sub(r'\[|]|"|\*|=|{|}|-|&|;|/|\||:|_|\(|\)|\+|!|\s|\t', r' ', text)
        text = text.split(" ")
        wordList = {}

        for word in text:
            if word == "":
                continue
            if word not in wordList:
                wordList[word] = 1
            elif word in wordList:
                wordList[word] = wordList[word] + 1

        for word in wordList:
            wordList[word] = int(wordList[word])

        sorted_wordList = sorted(wordList.items(), key=lambda wl: wl[0])
        best_wordList = sorted(sorted_wordList, key=lambda wl: wl[1], reverse=True)
        for word, count in best_wordList:
            open_out_book.write(str(word) + "\t" + str(count) + "\n")

#   Sources:
#   https://www.itworld.com/article/2784456/using-regular-expressions-to-identify-xml-tags.html
#   python documentation
#   https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/ for lambda
#   worked with Sophia!
