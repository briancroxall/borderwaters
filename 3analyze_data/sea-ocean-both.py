#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 14:44:52 2019

@author: briancroxall

Script to count the appearance of ocean, sea, or both in a single article.
"""

from glob import glob
import re
# from collections import defaultdict as dd


def get_journal(file):
    # Function to get journal abbreviation
    short = file.split('/')[-1]
    j_name = short.split('_')[0]
    return j_name


def get_year(file):
    # Function to get article year
    short = file.split('/')[-1]
    year = short.split('_')[1]
    return year


# create dictionaries
count_dict = {}
j_out = {'amerquar': 'American Quarterly',
         'amerlite': 'American Literature',
         'amerlitehist': 'American Literary History',
         'jamericanhistory': 'Journal of American History',
         'jamerstud': 'Journal of American Studies'}
# regex
re_ocean = r'((?:\b\w+\b-)?\b\w*[o0]cean.*?\b(?:\'s|-\w*)?)'
re_sea = r'sea-|seas-|(\bsea(?:s)?\b)'  # https://regex101.com/r/nCtp0I/4 should capture only "sea" and "seas" and no hyphenates

# create term lists
journals = ['amerquar', 'amerlite', 'amerlitehist', 'jamericanhistory',
            'jamerstud']
terms = ['sea', 'ocean', 'both']

# create output file
with open('sob-results-2010s.tsv', 'w') as output:
    print('Journal', 'Ocean Count', 'Sea Count', 'Both count', sep='\t',
          file=output)

# corpus
test = glob('test/*.txt')
corpus = glob('articles/*.txt')

for journal in journals:
    count_dict[journal] = {term: 0 for term in terms}

for counter, article in enumerate(corpus):
    if counter % 100 == 0:
        print('.', end='', flush=True)
    journal = get_journal(article)
    year = get_year(article)
    if year.startswith('201'):
        with open(article) as file:
            text = file.read()
        match_ocean = re.search(re_ocean, text, flags=re.I)
        match_sea = re.search(re_sea, text, flags=re.I)
        if match_ocean:
            if match_sea:
                count_dict[journal]['both'] += 1
            else:
                count_dict[journal]['ocean'] += 1
        elif match_sea:
            count_dict[journal]['sea'] += 1
        else:
            continue
    else:
        continue

with open('sob-results-2010s.tsv', 'a') as output:
    for each in count_dict:
        print(j_out[each], str(count_dict[each]['ocean']),
              str(count_dict[each]['sea']), str(count_dict[each]['both']),
              sep='\t', file=output)



"""
for article in test:
    journal = get_journal(article)
    with open(article) as file:
        text = file.read()
    match_ocean = re.search(re_ocean, text, flags=re.I)
    match_sea = re.search(re_sea, text, flags=re.I)
    if match_ocean:
        if match_sea:
            both.append(article)
            print(article, 'Found both!\n')
        else:
            ocean_articles.append(article)
            print(article, 'Found an ocean!\n')
    elif match_sea:
        sea_articles.append(article)
        print(article, 'Found a sea!\n')
    else:
        print(article, 'Nope!')
print('Number of Sea-only articles: ', len(sea_articles))
print('Number of Ocean-only articles: ', len(ocean_articles))
print('Number of both articles: ', len(both))
"""
