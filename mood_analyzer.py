#!/usr/bin/python

# Coding project for Mevoked
# Kaylee Moser
# Python version 2.7.10

import sys
from openpyxl import load_workbook

# read in a sentence (tweet)
tweet = sys.stdin.readline().split()

# read in spreadsheet with values for pos/neg/neut
wb = load_workbook('test.xlsx')
ws = wb.active

# for each word in tweet, search spreadsheet for matching word
# NEEDS CHANGING; for now prints matching word
for word in tweet:
    for row in ws.iter_rows('A2:A20'):
        for cell in row:
            if (word == cell.value):
                print word



