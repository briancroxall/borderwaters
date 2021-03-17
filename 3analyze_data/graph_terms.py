#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:22:56 2018

@author: briancroxall
"""

from collections import defaultdict as dd
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from datetime import datetime
import os

# Establish timestamps
now = datetime.now()
year = str(now.year)
month = str(now.month)
day = str(now.day)

# Directories
saveloc = 'images/' + year + '_' +  month + '_' + day
raw = saveloc + '/raw'
normalized = saveloc + '/normed' 
counts_dir = 'counts'
total_counts_dir = 'counts/total'
article_counts_dir = 'counts/article'

if not os.path.isdir(saveloc):
    os.mkdir(saveloc)
if not os.path.isdir(raw):
    os.mkdir(raw)
if not os.path.isdir(normalized):
    os.mkdir(normalized)
if not os.path.isdir(counts_dir):
    os.mkdir(counts_dir)
if not os.path.isdir(total_counts_dir):
    os.mkdir(total_counts_dir)
if not os.path.isdir(article_counts_dir):
    os.mkdir(article_counts_dir)
    

journals = ['amerquar', 'amerlitehist', 'jamerstud', 'jamericanhistory',
            'amerlite']
terms = ['word_count', 'archi', 'archi_yn', 'ocean', 'ocean_yn', 'isl', 
         'isl_yn', 'cont', 'cont_yn', 'water', 'water_yn', 'sea', 'sea_yn', 
         'mainland', 'mainland_yn', 'insular', 'insular_yn', 'transnational',
         'transnational_yn', 'pacific', 'pacific_yn', 'atlantic', 
         'atlantic_yn']

article_count_terms = ['archi_yn', 'ocean_yn', 'isl_yn', 'cont_yn', 'water_yn',
                       'sea_yn', 'mainland_yn', 'insular_yn',
                       'transnational_yn', 'pacific_yn', 'atlantic_yn']
total_count_terms = ['archi', 'ocean', 'isl', 'cont', 'water', 'sea',
                     'mainland', 'insular', 'transnational', 'pacific',
                     'atlantic']


terms_dict = {'word_count': 2,
              'archi': 3,
              'archi_yn': 4,
              'ocean': 6,
              'ocean_yn': 7,
              'isl': 9,
              'isl_yn': 10,
              'cont': 12,
              'cont_yn': 13,
              'water': 15,
              'water_yn': 16,
              'sea': 17,
              'sea_yn': 18,
              'mainland': 19,
              'mainland_yn': 20,
              'insular': 22,
              'insular_yn': 23,
              'transnational': 25,
              'transnational_yn': 26,
              'pacific': 28,
              'pacific_yn': 29,
              'atlantic': 31,
              'atlantic_yn': 32}

journals_full = {'amerquar': 'American Quarterly',
                 'amerlitehist': 'American Literary History',
                 'jamerstud': 'Journal of American Studies',
                 'jamericanhistory': 'Journal of American History',
                 'amerlite': 'American Literature'}

journals_abbrev = {'amerquar': 'AQ',
                   'amerlitehist': 'ALH',
                   'jamerstud': 'JAS',
                   'jamericanhistory': 'JAH',
                   'amerlite': 'AL'}

terms_full = {'archi': '*archipel*',
              'archi_yn': '*archipel*',
              'ocean': '*ocean*',
              'ocean_yn': '*ocean*',
              'isl': '*isl*',
              'isl_yn': '*isl*',
              'cont': '*continent*',
              'cont_yn': '*continent*',
              'water': 'water',
              'water_yn': 'water',
              'sea': 'sea|seas',
              'sea_yn': 'sea|seas',
              'mainland': '*mainland*',
              'mainland_yn': '*mainland*',
              'insular': '*insular*',
              'insular_yn': '*insular*',
              'transnational': '*transnational*',
              'transnational_yn': '*transnational*',
              'pacific': '*pacific',
              'pacific_yn': '*pacific',
              'atlantic': '*atlantic',
              'atlantic_yn': '*atlantic'}

terms_save = {'archi_yn': 'archi',
              'ocean_yn': 'ocean',
              'isl_yn': 'isl',
              'cont_yn': 'cont',
              'water_yn': 'water',
              'sea_yn': 'sea',
              'mainland_yn': 'mainland',
              'insular_yn': 'insular',
              'transnational_yn': 'transnational',
              'pacific_yn': 'pacific',
              'atlantic_yn': 'atlantic'}


# create TSVs for counts
for journal in journals:
    for term in total_count_terms:
        with open(total_counts_dir + '/' + journal + '_' + term +
                  '_years_counts.tsv', 'w') as count_file:
            print('Year', 'Count', sep='\t', file=count_file)
        with open(total_counts_dir + '/' + journal + '_' + term +
                  '_decades_counts.tsv', 'w') as count_file:
                print('Year', 'Count', sep='\t', file=count_file) 
    for term in article_count_terms:
        with open(article_counts_dir + '/' + journal + '_' + terms_save[term] +
                  '_years_article_counts.tsv', 'w') as count_file:
            print('Year', 'Count', sep='\t', file=count_file)
        with open(article_counts_dir + '/' + journal + '_' + terms_save[term] +
                  '_decades_article_counts.tsv', 'w') as count_file:
                print('Year', 'Count', sep='\t', file=count_file)


md = {}  # create master dictionary
ad = {}  # create dictionary for article counts

"""
for journal in journals:
    years = set()
    decades = set()
    with open(journal + '.tsv') as open_tsv:
        for line in open_tsv:
            line = line.split('\t')
            try:
                year = int(line[1])
                years.add(year)
                decade = line[1][:-1] + '0s'
                decades.add(decade)
            except ValueError:
                continue
    ad[journal] = {years: dd(int) for year in years}
    with open(journal + '.tsv') as open_tsv:
        for line in open_tsv:
            line = line.split('\t')
            try:
                year = int(line[1])
                decade = line[1][:-1] + '0s'
            except ValueError:
                continue
            ad[journal][year] += int()
"""


# md[journal][term][year]

for journal in journals:
    md[journal] = {term: dd(int) for term in terms}
    with open(journal + '.tsv') as open_tsv:
        for line in open_tsv:
            line = line.split('\t')
            try:
                year = int(line[1])
                decade = line[1][:-1] + '0s' 
            except ValueError:
                continue
            for term in terms:
                md[journal][term][year] += int(line[terms_dict[term]])
                md[journal][term][decade] += int(line[terms_dict[term]])

for journal in journals:
    # generate "total mentions" graphs. This should be the graphs that count all appearances of the term.
    for term in total_count_terms:
        counts = md[journal][term].items()
        year_counts = sorted([(year, count) for year, count in counts if isinstance(year, int)])
        norm_year_counts = sorted([(year, count / md[journal]['word_count'][year]) for year, count in counts if isinstance(year, int)])
        decade_counts = sorted([(year, count) for year, count in counts if isinstance(year, str)])  # This works because the decades are strings in the 'year' value of the dictionary, whereas the years are ints
        norm_decade_counts = sorted([(year, count / md[journal]['word_count'][year]) for year, count in counts if isinstance(year, str)])
        
        # print total counts to TSVs
        for year, counts in year_counts:
            with open(total_counts_dir + '/' + journal + '_' + term + '_years_counts.tsv', 'a') as count_file:
                print(year, counts, sep='\t', file=count_file)
        for year, counts in decade_counts:
            with open(total_counts_dir + '/' + journal + '_' + term + '_decades_counts.tsv', 'a') as count_file:
                print(year, counts, sep='\t', file=count_file)        
        
        # generate year graphs
        plt.plot(*zip(*year_counts))
        plt.xlabel('Years')
        plt.ylabel('Counts')
        plt.title('Total uses of ' + f'$\it{terms_full[term]}$' + ' in ' +
                  f'$\it{journals_abbrev[journal]}$' + ' per year')
        plt.savefig(raw + '/' + journal + '_' + term +
                    '_totals_years.png')
        plt.clf()
        
        # generate normalized year graphs
        plt.plot(*zip(*norm_year_counts))
        plt.xlabel('Years')
        plt.ylabel('Normalized counts')
        plt.title('Normalized mentions of ' + f'$\it{terms_full[term]}$' + ' in ' +
                  f'$\it{journals_abbrev[journal]}$' + ' per year')
        plt.savefig(normalized + '/' + journal + '_' + term +
                    '_normalized_totals_years.png')
        plt.clf()
        
        #generate decade graphs
        plt.plot(*zip(*decade_counts))
        plt.xlabel('Decades')
        plt.ylabel('Counts')
        plt.title('Total uses of ' + f'$\it{terms_full[term]}$' + ' in ' + 
                  f'$\it{journals_abbrev[journal]}$' + ' per decade')
        plt.savefig(raw + '/' + journal + '_' + term +
                    '_totals_decades.png')
        plt.clf()
        
        # generate normalized decade graphs
        plt.plot(*zip(*norm_decade_counts))
        plt.xlabel('Decades')
        plt.ylabel('Normalized counts')
        plt.title('Normalized mentions of ' + f'$\it{terms_full[term]}$' + ' in ' +
                  f'$\it{journals_abbrev[journal]}$' + ' per decade')
        plt.savefig(normalized + '/' + journal + '_' + term +
                    '_normalized_totals_decades.png')
        plt.clf()
        
    # generate "article mentions" graphs. These should be graphs that show either a 1 or a 0 for each article
    for term in article_count_terms:
        counts = md[journal][term].items()
        year_counts = sorted([(year, count) for year, count in counts if isinstance(year, int)])
        decade_counts = sorted([(year, count) for year, count in counts if isinstance(year, str)])
        
        # print "article mentions" counts to TSVs
        for year, counts in year_counts:
            with open(article_counts_dir + '/' + journal + '_' + terms_save[term] +
                      '_years_article_counts.tsv', 'a') as count_file:
                print(year, counts, sep='\t', file=count_file)
        for year, counts in decade_counts:
            with open(article_counts_dir + '/' + journal + '_' + terms_save[term] +
                      '_decades_article_counts.tsv', 'a') as count_file:
                print(year, counts, sep='\t', file=count_file) 
        
        # generate year graphs
        plt.plot(*zip(*year_counts))
        plt.xlabel('Years')
        plt.ylabel('Counts')
        plt.title('Articles that use ' + f'$\it{terms_full[term]}$' + ' in ' +
                  f'$\it{journals_abbrev[journal]}$' + ' per year')
        plt.savefig(raw + '/' + journal + '_' + terms_save[term] +
                    '_mentions_articles_years.png')
        plt.clf()
        
        #generate decade graphs
        plt.plot(*zip(*decade_counts))
        ax = plt.gca()  # This and next line force the y-axis to be an integer
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.xlabel('Decades')
        plt.ylabel('Counts')
        plt.title(f'Articles that use $\it{terms_full[term]}$ in $\it{journals_abbrev[journal]}$ per decade')
        plt.savefig(raw + '/' + journal + '_' + terms_save[term] +
                    '_mentions_articles_decades.png')
        plt.clf()
    
print('Time elapsed: ', datetime.now() - now)