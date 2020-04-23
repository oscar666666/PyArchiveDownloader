from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import os.path
import re
import urllib.request

from URLGet import *
prefixlink = "https://www.cs.cmu.edu/~16385/s19/lectures/"
downloadlink = []
raw_html = simple_get('https://www.cs.cmu.edu/~16385/s19/lectures/')
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


    if os.path.isfile(filenames[x]):#only download new files
        print("File exist")
    else:
        print("File not exist")
        urllib.request.urlretrieve(downloadlink[x], filenames[x] )