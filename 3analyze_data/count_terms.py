#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2018-07-10

@author: briancroxall

A script to count the appearance of particular words in the JSTOR and
Project Muse corpora


ocean (including words like oceanic and oceania)
island (and islands and islandic etc)
isle (and isles)
continent
sea (can you search for this word without picking up thinks like "season"?)
water
"""

from glob import glob
import re
from datetime import datetime
# from pprint import pprint
# from collections import Counter
from nltk import word_tokenize
from string import punctuation

punct = set(punctuation)
punct.add('')  # add an empty string to the set

# Start Timer for script
startTime = datetime.now()


def get_id(file):
    # function to get file name w/o extension or journal name. It accounts for the shift to DOIs late in the run of amerlite.
    name = file.split('/')[-1]
    no_ext_list = name.split('.')
    if len(no_ext_list) == 2:
        new_name = no_ext_list[0]
    else:
        new_name = '.'.join(no_ext_list[0:2])
    underscore = new_name.split('_')
    drop_jname = '_'.join(underscore[1:])
    return drop_jname


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

"""
def get_vol(file):
    # Function to get article volume
    short = file.split('/')[-1]
    vol = short.split('_')[2]
    return vol


def get_iss(file):
    # Function to get article issue
    short = file.split('/')[-1]
    iss = short.split('_')[3]
    return iss
"""


def count_yn(count):
    # Function to determine if a count is 1 or higher or not
    if count >= 1:
        return 1
    else:
        return 0


def get_word_count(text):
    # Function to count the number of words in an individual article
    tokens = word_tokenize(text)
    no_punct = [t for t in tokens if t not in punct]
    return len(no_punct)

# test corpus
test = list(sorted(glob('test/*.txt')))

# actual corpus
articles = list(sorted(glob('articles/*.txt')))

# create TSVs
filenames = ['amerquar.tsv', 'amerlite.tsv', 'amerlitehist.tsv',
             'jamericanhistory.tsv', 'jamerstud.tsv']
headers = ['Article ID', 'Year', 'Word Count',
           'Archi Count', 'Archi Y/N', 'Archi Words',
           'Ocean Count', 'Ocean Y/N', 'Ocean Words',
           'Island Count', 'Island Y/N', 'Island Words',
           'Continent Count', 'Continent Y/N', 'Continent Words',
           'Water Count', 'Water Y/N',
           'Sea Count', 'Sea Y/N',
           'Mainland Count', 'Mainland Y/N', 'Mainland Words',
           'Insular Count', 'Insular Y/N', 'Insular Words',
           'Transnational Count', 'Transnational Y/N', 'Transnational Words',
           'Pacific Count', 'Pacific Y/N', 'Pacific Words',
           'Atlantic Count', 'Atlantic Y/N', 'Atlantic Words']

for filename in filenames:
    with open(filename, 'w') as tsv:
        print(*headers, sep='\t', file=tsv)

# regex
re_archi = r'((?:\b\w+\b-)?\b\w*arch[i1l]pel\w*\b(?:\'s)?)'  # https://regex101.com/r/c0ngTb/2
re_ocean = r'((?:\b\w+\b-)?\b\w*[o0]cean.*?\b(?:\'s|-\w*)?)'  # https://regex101.com/r/ROlMVU/1
re_island = r'Carlisle|Bisland|aisle|sideaisle|((?:\w+(?:-)?)?isl(?:e|and)(?:(?:s|ic|\'s)?)(?:-\w+)?)\b'  # https://regex101.com/r/1zNJK3/3
re_water = r'water-|(\bwater)\b'  # https://regex101.com/r/nCtp0I/3
re_sea = r'sea-|seas-|(\bsea(?:s)?\b)'  # https://regex101.com/r/nCtp0I/4 should capture only "sea" and "seas" and no hyphenates
re_continent = r'incontinent|\b([\w-]*(?:continent\w*?))\b'  # https://regex101.com/r/af9YGC/3
re_mainland = r'\b((?:\w)*?-?ma[il1]n[1li]and(?:\w)*?(?:-)?(?:\w)*)\b'  # https://regex101.com/r/YhWBVA/1
re_insular = r'(?:\w)*?peninsular|\b((?:\w)*?(?:-)?[1li]nsu[1li]ar(?:\w)*?)\b'  # https://regex101.com/r/G12Lf1/2
re_transnational = r'\b(\w*?trans(?:-)?national.*?)\b'  # https://regex101.com/r/hO8Es3/3/
re_pacific = r'\b(\w*?(?:-)?Pac[i1|l]f[i1|l]c)\b'  # https://regex101.com/r/kMjgAH/3
re_atlantic = r'\b(\w*?(?:-)?At[l1|]antic)\b'  # https://regex101.com/r/y4THPO/2

"""
Original regexes for finding larger sets of words
re_sea = r'\b(sea[\w-]*)\b'  # https://regex101.com/r/Lnn8Oh/1  # https://regex101.com/r/mc57LC/1
re_water = r'\b(water[\w-]*)\b'  # https://regex101.com/r/577Xgo/1
"""


# counters
article_count = 0
amerlite_count = 0
amerlitehist_count = 0
amerquar_count = 0
jamericanhistory_count = 0
jamerstud_count = 0
archi_word_count = []
ocean_word_count = []
island_word_count = []
water_word_count = []
sea_word_count = []
continent_word_count = []
mainland_word_count = []
insular_word_count = []
transnational_word_count = []
pacific_word_count = []
atlantic_word_count = []

# sets
#sea_set = set()
#water_set = set()
#mainland_set = set()
#insular_set = set()
transnational_set = set()
pacific_set = set()
atlantic_set = set()

pacific_list = []
atlantic_list = []
transnational_list = []

# for-loop
for counter, article in enumerate(articles):
    if counter % 100 == 0:
        print('.', end='', flush=True)  # print 1 dot per every 100 articles
    article_count += 1
    """
    This next section was added to produce counts of how many articles are in
    each journal.
    """
    journal = get_journal(article)
    if journal == 'amerlite':
        amerlite_count += 1
    elif journal == 'amerlitehist':
        amerlitehist_count += 1
    elif journal == 'amerquar':
        amerquar_count += 1
    elif journal == 'jamericanhistory':
        jamericanhistory_count += 1
    elif journal == 'jamerstud':
        jamerstud_count += 1
    with open(article) as file:
        text = file.read()
    word_count = get_word_count(text)
    archi_words = re.findall(re_archi, text, flags=re.I)
    archi_count = len(archi_words)
    ocean_words = re.findall(re_ocean, text, flags=re.I)
    ocean_count = len(ocean_words)
    island_words = re.findall(re_island, text, flags=re.I)
    island_words2 = [i for i in island_words if i != '']
    """
    The list comprehension above solves the problem of getting empty results
    of '' returned in the output, which was throwing off the counts. These
    empty results are due to the best regex hack ever technique of using
    uncaptured groups to add a NOT to your search.
    """
    island_count = len(island_words2)
    water_words = re.findall(re_water, text, flags=re.I)
    water_words2 = [i for i in water_words if i != '']
    water_count = len(water_words2)
    sea_words = re.findall(re_sea, text, flags=re.I)
    sea_words2 = [i for i in sea_words if i != '']
    sea_count = len(sea_words2)
    continent_words = re.findall(re_continent, text, flags=re.I)
    continent_words2 = [i for i in continent_words if i != '']
    continent_count = len(continent_words2)
    mainland_words = re.findall(re_mainland, text, flags=re.I)
    mainland_count = len(mainland_words)
    insular_words = re.findall(re_insular, text, flags=re.I)
    insular_words2 = [i for i in insular_words if i != '']
    insular_count = len(insular_words2)
    transnational_words = re.findall(re_transnational, text, flags=re.I)
    transnational_count = len(transnational_words)
    [transnational_set.add(i) for i in transnational_words]
    # transnational_list.extend(transnational_words)
    pacific_words = re.findall(re_pacific, text, flags=re.I)
    pacific_count = len(pacific_words)
    [pacific_set.add(i) for i in pacific_words]
    # pacific_list.extend(pacific_words)
    atlantic_words = re.findall(re_atlantic, text, flags=re.I)
    atlantic_count = len(atlantic_words)
    [atlantic_set.add(i) for i in atlantic_words]
    # atlantic_list.extend(atlantic_words)
#    [mainland_set.add(i) for i in mainland_words]
#    [insular_set.add(i) for i in insular_words]
#    sea_words = re.findall(re_sea, text, re.I)
#    [sea_set.add(i) for i in sea_words]  # pick this line or the next two
#    sea_set_tmp = set(sea_words)
#    sea_set = sea_set | sea_set_tmp
#    water_words = re.findall(re_water, text, re.I)
#    [water_set.add(i) for i in water_words]
#    water_set_tmp = set(water_words)
#    water_set = water_set | water_set_tmp
    with open(get_journal(article) + '.tsv', 'a') as tsv:
        print(get_id(article), get_year(article), word_count,
              archi_count, count_yn(archi_count), archi_words,
              ocean_count, count_yn(ocean_count), ocean_words,
              island_count, count_yn(island_count), island_words2,
              continent_count, count_yn(continent_count), continent_words2,
              water_count, count_yn(water_count),
              sea_count, count_yn(sea_count),
              mainland_count, count_yn(mainland_count), mainland_words,
              insular_count, count_yn(insular_count), insular_words,
              transnational_count, count_yn(transnational_count), transnational_words,
              pacific_count, count_yn(pacific_count), pacific_words,
              atlantic_count, count_yn(atlantic_count), atlantic_words,
              sep='\t', file=tsv)
    archi_word_count.append(archi_count)
    ocean_word_count.append(ocean_count)
    island_word_count.append(island_count)
    water_word_count.append(water_count)
    sea_word_count.append(sea_count)
    continent_word_count.append(continent_count)
    mainland_word_count.append(mainland_count)
    insular_word_count.append(insular_count)
    transnational_word_count.append(transnational_count)
    pacific_word_count.append(pacific_count)
    atlantic_word_count.append(atlantic_count)
print('\nTotal number of articles scanned: ', article_count)
print('Total number of archi words in corpus: ', sum(archi_word_count))
print('Total number of ocean words in corpus: ', sum(ocean_word_count))
print('Total number of island words in corpus: ', sum(island_word_count))
print('Total number of water words in corpus: ', sum(water_word_count))
print('Total number of sea words in corpus: ', sum(sea_word_count))
print('Total number of continent words in corpus: ', sum(continent_word_count))
print('Total number of mainland words in corpus: ', sum(mainland_word_count))
print('Total number of insular words in corpus: ', sum(insular_word_count))
print('Total number of transnantional words in corpus: ', sum(transnational_word_count))
print('Total number of pacific words in corpus: ', sum(pacific_word_count))
print('Total number of atlantic words in corpus: ', sum(atlantic_word_count))
#with open('sea-words2.txt', 'w') as file:
#    print(sorted(sea_set), file=file)
#with open('water-words2.txt', 'w') as file:
#    print(sorted(water_set), file=file)
#with open('mainland-words.txt', 'w') as file:
#    print(sorted(mainland_set), file=file)
#with open('insular-words.txt', 'w') as file:
#    print(sorted(insular_set), file=file)
# with open('transnational-words.txt', 'w') as file:
#     pprint(sorted(transnational_set), stream=file)
# freqs = Counter(transnational_list)
# with open('transnational-freqs.txt', 'w') as freq_file:
#     pprint(freqs, stream=freq_file)

# with open('pacific-words.txt', 'w') as file:
#     pprint(sorted(pacific_set), stream=file)
# freqs_pac = Counter(pacific_list)
# with open('pacific-freqs.txt', 'w') as freq_file:
#     pprint(freqs_pac, stream=freq_file)
# with open('atlantic-words.txt', 'w') as file:
#     pprint(sorted(atlantic_set), stream=file)
# freqs_atl = Counter(atlantic_list)
# with open('atlantic-freqs.txt', 'w') as freq_file:
#     pprint(freqs_atl, stream=freq_file)

with open('article-counts.txt', 'w') as count_file:
    print('Total number of amerlite articles: ', amerlite_count,
          '\nTotal number of amerlitehist articles: ', amerlitehist_count,
          '\nTotal number of amerquar articles: ', amerquar_count,
          '\nTotal number of jamericanhistory articles: ', jamericanhistory_count,
          '\nTotal number of jamerstud articles: ', jamerstud_count,
          file=count_file)
print()
print('Time elapsed: ', datetime.now() - startTime)
