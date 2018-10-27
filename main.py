from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import re
import urllib.request

from URLGet import *
prefixlink = "https://www.eecs.yorku.ca/course_archive/2011-12/W/4313/slides/"
downloadlink = []
raw_html = simple_get('https://www.eecs.yorku.ca/course_archive/2011-12/W/4313/slides/')
html = BeautifulSoup(raw_html, 'html.parser')
filenames = []
match = re.compile('\.(pdf)')
for i in html.find_all('a', href=True):
    try:
        href = i['href']
        if re.search(match, href):
            filenames.append(i['href'])
            downloadlink.append( prefixlink + i['href'])
    except log_error():
        pass

for x in range(len(downloadlink)):
    print(downloadlink[x])


for x in range(len(downloadlink)):
    urllib.request.urlretrieve(downloadlink[x], filenames[x] )