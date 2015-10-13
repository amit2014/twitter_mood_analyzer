#!/usr/bin/python

# Coding project for Mevoked
# Kaylee Moser
# Python version 2.7.10

from openpyxl import load_workbook

# read in spreadsheet with values for pos/neg/neut
wb = load_workbook('test.xlsx')
ws = wb.active
print ws['A4'].value

