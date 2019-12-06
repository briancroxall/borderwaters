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
    
"""    
def get_html_title(file):
    # function to extract first 50 characters of title from HTML file
    no_dir = file.split('/')[-1]
    no_ext = no_dir.split('.')[0]
    return no_ext[:50]
"""

# Regex
re_notes = r'(\d+)([A-Z])'  # https://regex101.com/r/EwpLIn/2
re_ref1 = r'(References)([A-Z])'  # https://regex101.com/r/WX1gxg/2
re_ref2 = r'([A-Z][a-z]+)([A-Z])'  # https://regex101.com/r/WX1gxg/1


# Directory Management
if not os.path.isdir('amerlite-txt'):
    os.mkdir('amerlite-txt')
    
if not os.path.isdir('amerlite-dec2019-txt'):
    os.mkdir('amerlite-dec2019-txt')
    
"""
with open('amerlite-check.tsv', 'w') as new_file:
    print('Number', 'HTML title', 'Extracted Title', 'New Name', 
          sep='\t', file=new_file)
"""

#corpora
test = ['amerlite/Choosing-Death-The-Making-of-Martyrs-in-Early-American-Criminal-Narratives.html',
        'amerlite/Dead-Letters-Sent-Queer-Literary-TransmissionOld-Futures-Speculative-Fiction-and-Queer-PossibilityCirculating-Queerness-Before-the-Gay-and-Lesbian-NovelMelodrama-An-Aesthetics-of-Impossibility.html']
corpus = glob('amerlite/*.html')

# Counters
counter = 0

# loop
print('Processing files')
for article in test:
    counter += 1  # increment counter
    print('.', end='', flush=True)  # print progress dots
    journal = 'amerlite'
#    html_title = get_html_title(article)
    soup = make_soup(article)  # create soup object
    year_tag = soup.find('meta', {'name' : 'citation_publication_date'}) 
    year = year_tag['content'].split('/')[0]
    vol_tag = soup.find('meta', {'name' : 'citation_volume'})
    vol = vol_tag['content']
    iss_tag = soup.find('meta', {'name' : 'citation_issue'})
    iss = iss_tag['content']
    fpage_tag = soup.find('meta', {'name' : 'citation_firstpage'})
    fpage = fpage_tag['content']
    lpage_tag = soup.find('meta', {'name' : 'citation_lastpage'})  # find a meta tag with a key 'name' and a value 'citation_lastpage' and then turn that into a soup object that functions like a dictionary.
    lpage = lpage_tag['content']  # hit that soup object dictionary for the value of the 'content' key
    file_id_tag = soup.find('meta', {'name' : 'citation_xml_url'})
    file_id_full = file_id_tag['content']
    file_id = file_id_full.split('/')[-1]
    title_tag = soup.find('meta', {'name' : 'citation_title'})
    title = title_tag['content']
    body_tag = soup.find('div', {'data-widgetname' : 'ArticleFulltext'})  # find a div tag with key/value paid as listed
    try:
        body_tag.h2.extract()  # This looks for this particular tag within body_tag and then pops it out of body_tag
    except AttributeError:
        pass
    try:
        body_tag.section.extract()
    except AttributeError:
        pass
    try:
        body_tag.find('div', {'class': 'article-metadata-panel clearfix'}).extract()
    except AttributeError:
        pass
    body = body_tag.get_text()
    fixed_notes = re.sub(re_notes, r'\n\1 \2', body, flags=0)
    ref_fix1 = re.sub(re_ref1, r'References \2', fixed_notes, flags=0)
    ref_fix2 = re.sub(re_ref2, r'\1, \2', ref_fix1, flags=0)
    with open('amerlite-dec2019-txt/' + journal + '_' + year + '_' + vol + '_'
              + iss + '_' + fpage + '-' + lpage + '_' + file_id + '.txt',
              'w') as new_file:
        print(title, ref_fix2, file=new_file)
"""    
    with open('amerlite-check.tsv', 'a') as output_file:
        print(counter, html_title, title[:50], journal + '_' + year + '_' + vol
              + '_' + iss + '_' + fpage + '-' + lpage + '_' + file_id,
              sep='\t', file=output_file)
"""
print('\nNumber of files processed: ', counter)
