#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 13:52:16 2019

@author: briancroxall

Script to rename the _American Literature_ PDFs and XML from Duke UP
in accordance to their metadata.

This script is designed to take care of everything at once, and needs to be
run from inside the amerlite/articles-from-duke folder.
"""

import os
from shutil import copy2
from pathlib import Path
from glob import glob  # needed for bunching files
from bs4 import BeautifulSoup


def make_soup(metadata):
    """ Function to open XML file and run it through Beautiful Soup"""
    with open(metadata) as xml_file:
        soup = BeautifulSoup(xml_file, 'lxml')  # lxml-xml doesn't work;unclear
        return soup


# destination folders
home = os.path.expanduser('~')
parent = home + '/Documents/github/amerlite/'

if not os.path.isdir(parent + 'scripted-renamed'):
    os.mkdir(parent + 'scripted-renamed')
if not os.path.isdir(parent + 'scripted-renamed/pdfs'):
    os.mkdir(parent + 'scripted-renamed/pdfs')
if not os.path.isdir(parent + 'scripted-renamed/metadata'):
    os.mkdir(parent + 'scripted-renamed/metadata')
if not os.path.isdir(parent + 'scripted-renamed/metadata/bookreviews'):
    os.mkdir(parent + 'scripted-renamed/metadata/bookreviews')
if not os.path.isdir(parent + 'scripted-renamed/pdfs/bookreviews'):
    os.mkdir(parent + 'scripted-renamed/pdfs/bookreviews')

md_dest = parent + 'scripted-renamed/metadata/'
pdf_dest = parent + 'scripted-renamed/pdfs/'
work_dir = parent + 'articles-from-duke/'
md_br_dest = parent + 'scripted-renamed/metadata/bookreviews/'
pdf_br_dest = parent + 'scripted-renamed/pdfs/bookreviews/'

# create error log
with open(parent + 'error_log.txt', 'w') as f:
    print('XML File', 'Missing PDF name', 'Year', 'Vol', 'Iss', 'FPage', 
          'LPage', sep='\t', file=f)
err_log = parent + 'error_log.txt'

# test corpora
#small_test = ['/Users/briancroxall/Desktop/00720001-tree.xml']
#test_metadata = sorted(glob('test/al_72_1_xml/*.xml'))
#test_articles = sorted(glob('test/al_72_1_pdf/*.pdf'))

# real corpora
#dir_contents = os.listdir() Only useful when I was working in a single dir

# for loop
counter = 1
for p in Path('.').glob('*'):
    if p.is_dir():
        loc = work_dir + p.name + '/'
        new_items = os.listdir(loc)
        for item in new_items:
            if item.endswith('_pdf'):
                pdfloc = loc + item + '/'
                continue
            elif item.endswith('_xml'):
                xmlloc = loc + item + '/'
                xmlglob = glob(xmlloc + '*.xml')
            else:
                continue
        for file in xmlglob:
            """
            This portion of the for-loop opens and soups the XML and then
            saves various portions to variables for renaming the files.
            """
            with open(file) as the_file:
                xml = the_file.read()
            soup = make_soup(file)
            try:
                year = soup.find('year').get_text()
            except AttributeError:
                year = 'none'
            try:
                vol = soup.find('volume').get_text()
            except AttributeError:
                vol = 'none'
            try:
                iss = soup.find('issue').get_text()
            except AttributeError:
                iss = 'none'
            iss_fix = iss.replace('/', '-')  # in case we have split issues
            try:
                pdf = soup.find('self-uri').get('xlink:href')
            except AttributeError:
                print('Problem with ' + file)
            if pdf.endswith('.pdf'):
                pdf = pdf[:-4]
            try:
                fpage = soup.find('fpage').get_text()
            except AttributeError:
                fpage = 'none'
            try:
                lpage = soup.find('lpage').get_text()
            except AttributeError:
                lpage = 'none'
            try:
                id_ = soup.find('article-id').get_text()
            except AttributeError:
                id_ = str(counter).zfill(8)
                counter += 1
            id_fix = id_.replace('/', '-')
            type_ = soup.find('article').get('article-type')
            if type_ == 'book-review':
                id_fix = id_fix + 'br'
            new_name = f'amerlite_{year}_{vol}_{iss_fix}_{fpage}-{lpage}_{id_fix}'
            if type_ == 'book-review':
                with open(md_br_dest + new_name + '.xml', 'w') as new_xml:
                    print(xml, file=new_xml)
                try:
                    copy2(pdfloc + pdf + '.pdf', pdf_br_dest + new_name +
                          '.pdf')
                except FileNotFoundError:
                    with open(err_log, 'a') as error_log:
                        print(file, pdfloc + pdf + '.pdf', year, vol, iss_fix, 
                              fpage, lpage, sep='\t', file=error_log)
            else:
                with open(md_dest + new_name + '.xml', 'w') as new_xml:
                    print(xml, file=new_xml)
                try:
                    copy2(pdfloc + pdf + '.pdf', pdf_dest + new_name + '.pdf')
                except FileNotFoundError:
                    with open(err_log, 'a') as error_log:
                        print(file, pdfloc + pdf + '.pdf', year, vol, iss_fix, 
                              fpage, lpage, sep='\t', file=error_log)


"""
Stuff that I'm not using at the moment

#md = {}  # create master dictionary
#
#for item in test_metadata:
#    md[item] = {}
#    with open(item) as the_file:
#        xml = the_file.read()
#    soup = make_soup(item)
#    md[item]['year'] = soup.find('year').get_text()
#    md[item]['vol'] = soup.find('volume').get_text()
#    md[item]['iss'] = soup.find('issue').get_text()
#    md[item]['pdf'] = soup.find('self-uri').get('xlink:href')
#    md[item]['fpage'] = soup.find('fpage').get_text()
#    md[item]['lpage'] = soup.find('lpage').get_text()
#    print(md[item])
##print(md)

td = {}  # create test dictionary

for item in test_metadata:
    counter = 1
    soup = make_soup(item)
    try:
        id_ = soup.find('article-id').get_text()
    except AttributeError:
        id_ = str(counter).zfill(8)
        counter += 1
    td[id_] = soup.find('self-uri').get('xlink:href')
print(td)
print()
print('No duplicates? (True means no duplicates; False means duplicates): ',
      len(td.values()) == len(set(td.values())))
print()
if len(td.values()) == len(set(td.values())):
    print('All\'s well!')
else:
    dup_dict = dd(set)
    for k, v in td.items():
        dup_dict[v].add(k)
    dup_dict = { k : v for k, v in dup_dict.items() if len(v) > 1 }
    print(dup_dict)



walk_glob = []

for location, folders, files in os.walk('Documents/github/amerlite/test/'):
    for file in files:
        if file.endswith('.pdf'):
            walk_glob.append(file)
"""
