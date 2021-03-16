#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:43:07 2019

@author: briancroxall

File to try to eliminate duplicate PDFs
"""

from filecmp import cmp
from glob import glob
import os
from datetime import datetime

startTime = datetime.now()

dupes = set()

files = glob('*.pdf')

for file1 in files:
    for file2 in files:
        if cmp(file1, file2):
            if file1 < file2:
                dupes.add(file2)

for file in dupes:
    os.remove(file)
    
print('Time elapsed: ', datetime.now() - startTime)
