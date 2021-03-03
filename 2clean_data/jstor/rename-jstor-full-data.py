a#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 22 May 2018

@author: briancroxall

Script for renaming all JSTOR files based on metadata. This is based on a 
script that tackled only American Quarterly. That script is rename-jstor.py and
is in the jstor-aq-only-stuff directory.

Renamed files take the following format:
journal_year_vol_issue_fpage-lpage_ID

The ID is taken from the original files received from JSTOR. Allows finding
original file if necessary and prevents overwriting for some files that would
have identical names.


Possible journal names:
 'amerlite',
 'amerlitehist',
 'amerquar',
 'j100068',
 'j100078',
 'j100204',
 'j100807',
 'j50000251',
 'jamericanhistory',
 'jamerstud'


"""
import os
from bs4 import BeautifulSoup
from glob import glob


# Test objects
one_meta = ['test/journal-article-10.2307_2710055.xml']
one_article = ['test/journal-article-10.2307_2710055.txt']

two_meta = ['test/journal-article-10.2307_2710055.xml',
            'test/journal-article-10.2307_2710056.xml']
two_article = ['test/journal-article-10.2307_2710055.txt',
               'test/journal-article-10.2307_2710056.txt']

test_articles = glob('test/*.txt')
test_metadata = glob('test/*.xml')

metadata = sorted(glob('jstor-all-data/metadata/*.xml'))


def make_soup(metadata):
    """ Function to open file and run it through Beautiful Soup"""
    with open(metadata) as xml_file:
        soup = BeautifulSoup(xml_file, 'lxml-xml')
        return soup


def get_name(file):
    """ Function to extract file name so I can match txt and xml"""
    name = file.split('/')[-1]
    shorter = name.split('.')[:2]
    rejoin = ('.').join(shorter)
    return rejoin


def get_id(file):
    """ Function to extract short ID number from file. Will help prevent
    overwriting probles"""
    name = file.split('/')[-1]
    shorter = name.split('_')[-1]
    no_dot = shorter.split('.')[0]
    return no_dot


if not os.path.isdir('renamed-articles'):
    os.mkdir('renamed-articles')

if not os.path.isdir('renamed-metadata'):
    os.mkdir('renamed-metadata')

if not os.path.isdir('bad-data'):
    os.mkdir('bad-data')

if not os.path.isdir('bad-data/ocr'):
    os.mkdir('bad-data/ocr')

if not os.path.isdir('bad-data/metadata'):
    os.mkdir('bad-data/metadata')
    
if not os.path.isdir('front-matter'):
    os.mkdir('front-matter')

if not os.path.isdir('front-matter/ocr'):
    os.mkdir('front-matter/ocr')

if not os.path.isdir('front-matter/metadata'):
    os.mkdir('front-matter/metadata')

print('Renaming files')
for item in metadata:
    name = get_name(item)  # extract name for later
    id_ = get_id(item)  # extract ID number for later
    with open(item) as the_file:
        xml = the_file.read()
    soup = make_soup(item)
    j_name = [journal.get_text() for journal in soup.find_all('journal-id')]
    try:
        fpage = soup.find('fpage').get_text()
    except AttributeError:
        fpage = 'none'  # Not all articles have the <fpage> tag
    try:
        lpage = soup.find('lpage').get_text()
    except AttributeError:
        lpage = 'none' # Not all articles have the <lpage> tag
    j_name = [journal.get_text() for journal in soup.find_all('journal-id')]
    year = soup.find('year').get_text()
    try:
        volume = soup.find('volume').get_text()
    except AttributeError:
        volume = 'no-vol'
    try:
        issue = soup.find('issue').get_text()
    except AttributeError:
        issue = 'no-iss'
    try:
        title = soup.find('article-title').get_text()
    except AttributeError:
        title = 'M!ssing'
    # Two lists for elif statements later
    matter_title = ['Front Matter', 'Back Matter', 'Volume Information',
                    'Notes on the Contributors']
    fmatter_pages = ['', 'none']
    """
    Line that follows is a way around issues that are numbered as 1/2. If that
    turns up, the issue number is rewritten as 1-2.
    """
    iss_fix = issue.replace('/', '-')
    new_name = f'{j_name[0]}_{year}_{volume}_{iss_fix}_{fpage}-{lpage}_{id_}'
    # weed out front matter etc. based on title
    if title in matter_title:
        with open('front-matter/metadata/' + new_name + '.xml', 'w') as fm:
            print(xml, file=fm)
        with open('jstor-all-data/ocr/' + name + '.txt') as text_file:
            text = text_file.read()
        with open('front-matter/ocr/' + new_name + '.txt', 'w') as front_text:
            print(text, file=front_text)
    # weed out frontmatter based on empty or 'none' page strings
    # commenting it out for now as it only catches 5 things and I'm not sure 
    # that they are front matter
#    elif fpage in fmatter_pages:
#        with open('front-matter/metadata/' + new_name + '.xml', 'w') as f_meta:
#            print(xml, file=f_meta)
#        with open('aq-only-jstor-data/ocr/' + name + '.txt') as text_file:
#            text = text_file.read()
#        with open('front-matter/ocr/' + new_name + '.txt', 'w') as front_text:
#            print(text, file=front_text)
#        with open('missing.txt', 'a') as missing:  # check whether this captures anything useful
#            print(new_name + ' page issues', file=missing)
    # send everything else to the articles and metadata folders
    elif issue == 'no-iss':
        with open('no_issue.txt', 'a') as file:
            print(new_name, file=file)
        with open('renamed-metadata/' + new_name + '.xml', 'w') as output:
            print(xml, file=output)
        with open('jstor-all-data/ocr/' + name + '.txt') as text_file:
            text = text_file.read()
        with open('renamed-articles/' + new_name + '.txt', 'w') as output2:
            print(text, file=output2)
    elif volume == 'no-vol':
        with open('no_vol.txt', 'a') as file:
            print(new_name, file=file)
    else:
        print(name, 'becomes', new_name)
        with open('renamed-metadata/' + new_name + '.xml', 'w') as output:
            print(xml, file=output)
        with open('jstor-all-data/ocr/' + name + '.txt') as text_file:
            text = text_file.read()
        with open('renamed-articles/' + new_name + '.txt', 'w') as output2:
            print(text, file=output2)
print('\nFile renaming complete')


"""
Not using:
journal_names = set()
for item in metadata:
    print('.', end='', flush=True)  # show progress; print 1 dot per file
    with open(item) as the_file:
        xml = the_file.read()
    soup = make_soup(item)
    j_name = [journal.get_text() for journal in soup.find_all('journal-id')]
    journal_names.update(j_name)
print()
print(journal_names)  
    

"""
