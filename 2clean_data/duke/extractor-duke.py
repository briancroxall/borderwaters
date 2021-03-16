#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:06:24 2019

@author: briancroxall

Script to manage the pdftotext process within Bash.

IMPORTANT: This needs to be run from the command line and not within Spyder
because Spyder doesn't have access to pdftotext.
"""

import subprocess  # allows me to run command line commands
from shlex import split  # helps me pass commands to the command line as lists
from glob import glob
import os
import shutil
from datetime import datetime

startTime = datetime.now()


def get_name(file):
    #  function to get file name w/o extension. It accounts for the shift to DOIs late in the run.
    name = file.split('/')[-1]
    no_ext_list = name.split('.')
    if len(no_ext_list) == 2:
        new_name = no_ext_list[0]
    else:
        new_name = '.'.join(no_ext_list[0:2])
    return new_name


# Directories
home = os.path.expanduser('~')
parent = home + '/Documents/github/amerlite/'

if not os.path.isdir(parent + 'extracted-text'):
    os.mkdir(parent + 'extracted-text')

dest = parent + 'extracted-text/'

# Corpora
single = ['amerlite_2000_72_1_1-30_00720001.pdf']
corpus = sorted(glob('*.pdf'))

# Counters
counter = 0
counter2 = 0

# For-loop
for file in corpus:
    name = get_name(file)
    first = name + '-first.txt'
    rest = name + '-rest.txt'
    if name.startswith('amerlite_2000_72'):  # this should capture page proof files (vol 72)
        subprocess.run(split(f'pdftotext -f 1 -l 1 -x 134 -y 236 -W 330 -H 409 {file} {first}'))
        subprocess.run(split(f'pdftotext -f 2 -x 146 -y 124 -W 322 -H 515 {file} {rest}'))
        counter += 1
    elif name.startswith('amerlite_2001_73_2'):  # other set of page proofs (73.2)
        if name.endswith('br'):  # book reviews have longer first pages
            subprocess.run(split(f'pdftotext -f 1 -l 1 -x 117 -y 231 -W 353 -H 400 {file} {first}'))
            subprocess.run(split(f'pdftotext -f 2 -x 116 -y 123 -W 357 -H 521 {file} {rest}'))
            counter += 1
        else:
            subprocess.run(split(f'pdftotext -f 1 -l 1 -x 117 -y 231 -W 353 -H 374 {file} {first}'))
            subprocess.run(split(f'pdftotext -f 2 -x 116 -y 123 -W 357 -H 521 {file} {rest}'))
            counter += 1
    elif name.startswith('amerlite_2001_73_1') or name.startswith('amerlite_2001_73_3') or name.startswith('amerlite_2001_73_4') or name.startswith('amerlite_2002_74') or name.startswith('amerlite_2003_75'):
        if name.endswith('br'):  # book reviews have longer first pages
            subprocess.run(split(f'pdftotext -f 1 -l 1 -x 45 -y 200 -W 460 -H 425 {file} {first}'))
            subprocess.run(split(f'pdftotext -f 2 -x 45 -y 125 -W 450 -H 530 {file} {rest}'))
            counter2 += 1
        else:
            subprocess.run(split(f'pdftotext -f 1 -l 1 -x 45 -y 200 -W 450 -H 400 {file} {first}'))
            subprocess.run(split(f'pdftotext -f 2 -x 45 -y 125 -W 450 -H 530 {file} {rest}'))
            counter2 += 1
    elif name.startswith('amerlite_2004_76') or name.startswith('amerlite_2005_77') or name.startswith('amerlite_2006_78_1') or name.startswith('amerlite_2006_78_2'):
        if name.endswith('br'):
            subprocess.run(split(f'pdftotext -f 1 -l 1 -x 52 -y 157 -W 330 -H 405 {file} {first}'))
            subprocess.run(split(f'pdftotext -f 2 -x 52 -y 51 -W 330 -H 540 {file} {rest}'))
            counter2 += 1
        else:
            subprocess.run(split(f'pdftotext -f 1 -l 1 -x 52 -y 157 -W 330 -H 388 {file} {first}'))
            subprocess.run(split(f'pdftotext -f 2 -x 52 -y 51 -W 330 -H 540 {file} {rest}'))
            counter2 += 1
    else:
        subprocess.run(split(f'pdftotext -f 1 -l 1 -x 52 -y 157 -W 330 -H 388 {file} {first}'))
        subprocess.run(split(f'pdftotext -f 2 -x 52 -y 51 -W 330 -H 540 {file} {rest}'))
        counter2 += 1
    subprocess.run(f'cat {first} {rest} > {name}.txt', shell=True)  # because we are piping in the command (using >), we can't run it as a split. the shell=True fixes this
    shutil.move(f'{name}.txt', dest)
    os.remove(first)
    try:
        os.remove(rest)
    except FileNotFoundError:
        continue
print('Number of page proof files: ', counter)
print('Number of normal files: ', counter2)
print('Time elapsed: ', datetime.now() - startTime)
