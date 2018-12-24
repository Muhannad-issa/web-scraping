from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = bs(html, "lxml")
for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
