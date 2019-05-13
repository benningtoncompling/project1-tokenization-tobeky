#!/usr/bin/env python3


import re

file_name = "Wikipedia-LexicalAnalysis.xml"
out_file_name = "lexical_analysis_out.txt"

with open(file_name, 'r') as open_book:
    with open(out_file_name, 'w') as open_out_book:
        text = open_book.read()
        text = re.sub(r'<[^(><)]+>', r'', text)
        text = re.sub(r'\[|]|"|\*|=|{|}|-|&|;|/|\||:|_|\(|\)|\+|!', r'', text)
        text = text.split(" ")
        wordList = {}

        for word in text:
            if word not in wordList:
                wordList[word] = 1
            elif word in wordList:
                wordList[word] = wordList[word] + 1

        for word in wordList:
            open_out_book.write(str(word) + "\t" + str(wordList[word]) + "\n")

# Sources:
# https://www.itworld.com/article/2784456/using-regular-expressions-to-identify-xml-tags.html
# python documentation
# worked with Sophia!
