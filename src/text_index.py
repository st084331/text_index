#!/usr/bin/python
import argparse
import codecs
import os

def parser_args():
    p = argparse.ArgumentParser()
    p.add_argument('--file', type=str)
    p.add_argument('--mode', type=str)
    p.add_argument('--word', type=str)
    return p

def page_count(text):
    demo_text = text + '\n'
    pages = 0
    while demo_text != '':
        str_end = demo_text.index('\n')
        pages += 1
        demo_text = demo_text[(str_end + 1):]
    return pages

def word_places(text):
    places = []
    demo_text = text.replace()

parser = parser_args()
#word = parser.parse_args().word
#mode = parser.parse_args().mode
name_file = parser.parse_args().file + '.txt'
#for Mac
dirpath = os.path.dirname(__file__)
filepath = os.path.join(dirpath, name_file)
file = open(filepath.replace('.', '/Users/akabynda/pyhonProject/text_index/data', 1))
#for Windows
text = file.read()
print(text)
pages = page_count(text)
print(pages)