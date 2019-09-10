#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:52:32 2019

@author: briancroxall

Script to extract info from HTML of American Literature, which I hand
downloaded in September 2019 as part of the third round of data gathering.

This script is based on extract-jamericanhistory.py and extract-amerquar.py
in the same folder. 
"""

from bs4 import BeautifulSoup
from glob import glob
import os
import re

def make_soup(file):
    # Function to open file and run it through BeautifulSoup
    with open(file) as html_file:
        soup = BeautifulSoup(html_file, 'html5lib')
        return soup


def get_voliss(file):
    # Function to get volume and issue from filename
    name = file.split('/')[-1]
    voliss_split = name.split('_')[1:3]
    voliss = ('_').join(voliss_split)
    return voliss


def get_id(file):
    # Function to get the ID number for each file
    name = file.split('/')[-1]
    no_ext = name.split('.')[0]
    id_ = no_ext.split('_')[-1]
    return id_


# Regex
re_endpage = r'\s+\[End Page (?:[ivx]|\d)+\]\s+'  # https://regex101.com/r/Mr0kWf/2

# Directory Management
if not os.path.isdir('amerquar-txt'):
    os.mkdir('amerquar-txt')
    


#corpora
test = ['amerlite/Archives_of_Flesh-African_America,_Spain,_and_Post-Humanist_CritiqueIncomparable_Empires-Modernism_and_the_Translation_of_Spanish_and_American_Literature-American_Literature.html',
        'amerlite/Islam,_Puritanism,_and_Secular_Time-American_Literature.html']
corpus = glob('amerlite/*.html')

# Counters
counter = 0


# For loop
print('Processing files')
for article in test:
    counter += 1  # increment counter
    print('.', end='', flush=True)  # print progress dots
    journal = 'amerlite'
    voliss = get_voliss(article)
    file_id = get_id(article)  # get article id from filename
    soup = make_soup(article)  # create soup object
    title_tag = soup.find('div', {'id' : 'article-title'})
    title = title_tag.get_text(' ')
    fpage_tag = soup.find('meta', {'name' : 'citation_firstpage'})
    fpage = fpage_tag['content']
    lpage_tag = soup.find('meta', {'name' : 'citation_lastpage'})  # find a meta tag with a key 'name' and a value 'citation_lastpage' and then turn that into a soup object that functions like a dictionary.
    lpage = lpage_tag['content']  # hit that soup object dictionary for the value of the 'content' key
    year_tag = soup.find('meta', {'name' : 'citation_year'}) 
    year = year_tag['content']
    body_tag = soup.find('div', {'id' : 'body'})  # find a div tag with key/value paid as listed
    body = body_tag.get_text(' ')
    clean_body = re.sub(re_endpage, ' ', body, flags=re.I)  
    try:
        notes_tag = soup.find('div', {'class' : 'fn-group'})
        notes = notes_tag.get_text(' ')
        clean_notes = re.sub(re_endpage, ' ', notes, flags=re.I)
    except AttributeError:
        clean_notes = ''
#    works_cited = soup.find(class_='ref-list')
    with open('amerquar-txt/' + journal + '_' + year + '_' + voliss + '_' + 
              fpage + '-' + lpage + '_' + file_id + '.txt', 'w') as new_file:
        print(title, '\n', clean_body, '\n', clean_notes,
              file=new_file)
print('\nNumber of files processed: ', counter)
