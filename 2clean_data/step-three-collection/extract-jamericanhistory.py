#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 09:11:33 2018

Modified on 9 September 2019

@author: briancroxall

Script to extract info from HTML of Journal of American History,
which Jeremy scraped for our mid-2019 gathering of data for the AQ project.

This script is more or less identical to that which I created for the
second-pass on the data in 2018 in the (poorly named) Proquest repo
(https://github.com/briancroxall/proquest). 
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


def get_fpage(file):
    # Function to get the page number that is built into the filename
    name = file.split('/')[-1]
    fpage = name.split('_')[3]
    return fpage


def get_id(file):
    # Function to get the ID number for each file
    name = file.split('/')[-1]
    no_ext = name.split('.')[0]
    id_ = no_ext.split('_')[-1]
    return id_


# Directory Management
if not os.path.isdir('jamericanhistory-txt'):
    os.mkdir('jamericanhistory-txt')
    
if not os.path.isdir('jamericanhistory-dec2019-txt'):
    os.mkdir('jamericanhistory-dec2019-txt')
    
#corpora
test = ['jamericanhistory/articles/jamericanhistory_106_3_835_5628997.html']
corpus = glob('jamericanhistory/articles/*.html')

# Counters
counter = 0

# For loop
print('Processing files')
for article in corpus:
    counter += 1  # increment counter
    print('.', end='', flush=True)  # print progress dots
    journal = get_journal(article)  # get journal for article from filename
    voliss = get_voliss(article)
    file_id = get_id(article)  # get article id from filename
    fpage = get_fpage(article)  # get first page from filename
    soup = make_soup(article)  # create soup object
    lpage_tag = soup.find('meta', {'name' : 'citation_lastpage'})  # find a meta tag with a key 'name' and a value 'citation_lastpage' and then turn that into a soup object that functions like a dictionary.
    lpage = lpage_tag['content']  # hit that soup object dictionary for the value of the 'content' key
    year_tag = soup.find('meta', {'name' : 'citation_publication_date'}) 
    year_full = year_tag['content']
    year = year_full.split('/')[0]  # since the above returns a date in 2012/01/01 format, split it out to just the year
    body_tag = soup.find('div', {'data-widgetname' : 'ArticleFulltext'})  # find a div tag with key/value paid as listed
    body = body_tag.get_text(' ')
#    works_cited = soup.find(class_='ref-list')
    body_fixed = re.sub(r'© The Author 20.+', '', body, flags=re.I)
    with open('jamericanhistory-dec2019-txt/' + journal + '_' + year + '_' + voliss + '_' + 
              fpage + '-' + lpage + '_' + file_id + '.txt', 'w') as new_file:
        print(body_fixed, file=new_file)
print('\nNumber of files processed: ', counter)
