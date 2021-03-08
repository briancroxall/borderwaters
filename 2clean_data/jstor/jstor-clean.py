#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 16:13:46 2018

@author: briancroxall

Script to clean JSTOR OCR
"""

import re
import os
from glob import glob

def get_name(file):
    # Function to get file name w/o directory so I can save it again
    name = file.split('/')[-1]
    return name


def get_journal(file):
    # Function to get journal abbreviation 
    short = file.split('/')[-1]
    j_name = short.split('_')[0]
    return j_name
    

# test files
test = glob('clean-test/*.txt')

# actual corpus
articles = glob('renamed-articles/*.txt')

# create directories
if not os.path.isdir('simple-cleaned-articles'):
    os.mkdir('simple-cleaned-articles')
#if not os.path.isdir('simple-cleaned-articles/amerquar'):
#    os.mkdir('simple-cleaned-articles/amerquar')
#if not os.path.isdir('simple-cleaned-articles/amerlite'):
#    os.mkdir('simple-cleaned-articles/amerlite')
#if not os.path.isdir('simple-cleaned-articles/amerlitehist'):
#    os.mkdir('simple-cleaned-articles/amerlitehist')
#if not os.path.isdir('simple-cleaned-articles/jamericanhistory'):
#    os.mkdir('simple-cleaned-articles/jamericanhistory')
#if not os.path.isdir('simple-cleaned-articles/jamerstud'):
#    os.mkdir('simple-cleaned-articles/jamerstud')

# Regex for cleaning
regex_xml = r'(<plain_text>|</plain_text>|<page sequence="[0-9]+?">|</page>)'  # regex for page break tags
regex_lb = r'\b(\w+?)-\s(\w+?)\b'  # regex for line breaks

print('Initializing cleaning')
#For-loop
for article in articles:
    with open(article) as file:
        text = file.read() 
        no_xml = re.sub(regex_xml, '', text)
        no_lb = re.sub(regex_lb, r'\1\2', no_xml)
        with open('simple-cleaned-articles/' + get_name(article), 'w') as the_file:
                print(no_lb, file=the_file)
print('\nCleaning completed')