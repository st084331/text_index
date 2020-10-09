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
#demo_text = text
pages = 0
