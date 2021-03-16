#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:46:37 2019

@author: briancroxall

Script to clean the extracted text from the Duke corpus.
Problems:
    Ligatures: ﬀ ﬁ ﬂ
    Hyphenated words across page breaks
    the 'theor y' problem
    first-character / drop cap problem
    smart quotes / apostrophes

"""
import os
from glob import glob
import re


def get_name(file):
    # function to get file name so it can be saved again
    no_dir = file.split('/')[-1]
    return no_dir

# directories
if not os.path.isdir('cleaned-text'):
    os.mkdir('cleaned-text')

# corpora
test = ['extracted-text/amerlite_2002_74_4_779-806_00740779.txt',
        'extracted-text/amerlite_2017_89_2_213-223_10.1215-00029831-3861481.txt']
corpus = sorted(glob('extracted-text/*.txt'))

# regex for 'theor y' problem
regex_y = r'\b\sy\b'  # https://regex101.com/r/M1jpe6/1

# regex for word hyphenation across page breaks
regex_ws = r'\b-$\s*?\f*?\b'  # https://regex101.com/r/hFECO4/1

# regex for first-character / drop cap problem
regex_first = r'(\w)\n\n(\w*)\b'  # https://regex101.com/r/KUI710/1

# regex for smart punctuation
regex_sq = r'“|”'
regex_apo = r'’|‘'
regex_double_apo = r'\'\''

# for-loop
for file in corpus:
    name = get_name(file)
    with open(file) as read_file:
        text = read_file.read()
        ff = text.replace('ﬀ', 'ff')
        fi = ff.replace('ﬁ', 'fi')
        fl = fi.replace('ﬂ', 'fl')
        fix_y = re.sub(regex_y, 'y', fl, flags=re.I)
        no_ws = re.sub(regex_ws, '', fix_y, flags=re.M)
        fix_first = re.sub(regex_first, r'\1\2', no_ws, flags=re.I)
        fix_sq = re.sub(regex_sq, '"', fix_first)
        fix_apo = re.sub(regex_apo, '\'', fix_sq)
        no_double = re.sub(regex_double_apo, '"', fix_apo)
#    with open('test/test-cleaned/cleaned-' + name , 'w') as file:
#        print(no_double, file=file)
    with open('cleaned-text/' + name, 'w') as file:
        print(no_double, file=file)
