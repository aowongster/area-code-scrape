from __future__ import print_function

import sys
from bs4 import BeautifulSoup

with open('html_string.txt') as f:
    html_string = f.read()

soup = BeautifulSoup(html_string, 'html.parser') # dont have lib xml..

data = []
table = soup.find('table')

# table_body = table.find('tbody')
table_body = table

# header
rows = table_body.find('tr') # grab first tr for header
data.append([ row.text for row in rows ]) # setup fieleds

# data body
rows = table.find_all('tr')[1:] # skip one tr
for row in rows:
    cols = row.find_all('td') # not sure why i have to do this inner looping
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

# returns nested lists
print(data)

# TODO output to csv tsv textfile whatever..
