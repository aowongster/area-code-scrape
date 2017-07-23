from __future__ import print_function

from bs4 import BeautifulSoup

with open('html_string.txt') as f:
    html_string = f.read()

soup = BeautifulSoup(html_string, 'html.parser') # dont have lib xml..

data = []
table = soup.find('table')

# table_body = table.find('tbody')
# TODO fix parser to fit html

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for elel in cols if ele])

print(data)
