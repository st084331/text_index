#!/usr/bin/python
import argparse
import collections
from collections import Counter
import re
import string
import io
import codecs
import os

def parser_args():
    p = argparse.ArgumentParser()
    p.add_argument('--file', type=str)
    p.add_argument('--mode', type=str)
    p.add_argument('--word', type=str)
    p.add_argument('--num', type=str)
    return p


def find_word(text, word):
    page = 1
    pages = []
    word = ' '+word+' '
    counter = 0
    while text != '':
        str_end = text.index('\n')
        str_page = ' ' + text[:str_end] + ' '
        print(str_page)
        if (str_page.find(word) != -1):
            bul = 0
            for i in pages:
                if(i == page):
                    bul = 1
            if (bul == 0):
                pages.append(page)
        if counter == 45:
            counter = 0
            page += 1
        counter += 1
        text = text[(str_end + 1):]
    print(word.replace(' ', ''), end=' ')
    print(pages)

def common_words(text):



parser = parser_args()
word = parser.parse_args().word
#mode = parser.parse_args().mode
name_file = parser.parse_args().file + '.txt'
#for Windows
#file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', name_file))
#for Mac
file = io.open('/Users/akabynda/pyhonProject/text_index/data/' + name_file, encoding="utf - 8")
#for Windows
text = file.read()
e = '.', ',', ' " ', ';', ':', '-', '!', '?'
demo_text = text.lower() + '\n'
for i in range(len(e)):
    demo_text = demo_text.replace(e[i], "")
print(file)
find_word(demo_text, word)
