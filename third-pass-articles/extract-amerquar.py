#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 09:11:33 2018

Modified on 9 September 2019

@author: briancroxall

Script to extract info from HTML of American Quarterly,which Jeremy scraped for
our mid-2019 gathering of data for the AQ project.

This script is based on the extract-jamericanhistory.py in the same folder. 
"""

from bs4 import BeautifulSoup
from glob import glob
import os

def make_soup(file):
    # Function to open file and run it through BeautifulSoup
    with open(file) as html_file:
        soup = BeautifulSoup(html_file, 'html5lib')
        return soup

    
def get_journal(file):
    # Function to get journal from filename 
    name = file.split('/')[-1]
    journal = name.split('_')[0]
    return journal


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


# Directory Management
if not os.path.isdir('amerquar-txt'):
    os.mkdir('amerquar-txt')
    
#corpora
test = ['amerquar/articles/amerquar_70_1_689161.html']
corpus = glob('amerquar/articles/*.html')

# Counters
counter = 0

# For loop
print('Processing files')
for article in test:
    counter += 1  # increment counter
    print('.', end='', flush=True)  # print progress dots
    journal = get_journal(article)  # get journal for article from filename
    voliss = get_voliss(article)
    file_id = get_id(article)  # get article id from filename
    soup = make_soup(article)  # create soup object
    fpage_tag = soup.find('meta', {'name' : 'citation_firstpage'})
    fpage = fpage_tag['content']
    lpage_tag = soup.find('meta', {'name' : 'citation_lastpage'})  # find a meta tag with a key 'name' and a value 'citation_lastpage' and then turn that into a soup object that functions like a dictionary.
    lpage = lpage_tag['content']  # hit that soup object dictionary for the value of the 'content' key
    year_tag = soup.find('meta', {'name' : 'citation_year'}) 
    year = year_tag['content']
#    body = soup.find('div', {'data-widgetname' : 'ArticleFulltext'})  # find a div tag with key/value paid as listed
#    works_cited = soup.find(class_='ref-list')
    with open('amerquar-txt/' + journal + '_' + year + '_' + voliss + '_' + 
              fpage + '-' + lpage + '_' + file_id + '.txt', 'w') as new_file:
        print('I don\'t have a body yet!', file=new_file)
print('\nNumber of files processed: ', counter)
