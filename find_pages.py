import requests as r
from bs4 import BeautifulSoup

URL = "http://kingkiller.wiki/w/"

base = BeautifulSoup(r.get(URL + "Special:AllPages").text, "html5lib")
all_pages = [i["href"][1:] for i in base.find("div", {"class": "mw-allpages-body"}).find_all("a")]

for href in all_pages:
    page = BeautifulSoup(r.get(URL + href).text, "html5lib")
    all_linked_pages = [i["href"][1:] for i in page.find("div", {"class": "mw-body-content"}).find_all("a")]
    all_pages = list(set(all_pages).union(set(all_linked_pages)))
