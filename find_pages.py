import requests as r
from bs4 import BeautifulSoup

def find_a_under_div(url, div_class):
    page = BeautifulSoup(r.get(url).text, "html5lib")
    return [i["href"][1:] for i in page.find("div", {"class": div_class}).find_all("a")]

URL = "http://kingkiller.wiki/w/"

all_pages = find_a_under_div(URL + "Special:AllPages", "mw-allpages-body")

for href in all_pages:
    all_linked_pages = find_a_under_div(URL + href, "mw-body-content")
    all_pages = list(set(all_pages).union(set(all_linked_pages)))
