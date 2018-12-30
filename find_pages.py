import requests as r
from bs4 import BeautifulSoup

def find_a_under_div(url, **kwargs):
    page = BeautifulSoup(r.get(url).text, "lxml")
    return [i["href"][3:] for i in page.find("div", **kwargs).find_all("a")]

URL = "http://kingkiller.wiki/w/"

all_pages = find_a_under_div(URL + "Special:AllPages", class_="mw-allpages-body")
unknown_pages = []
for href in all_pages:
    all_linked_pages = find_a_under_div(URL + href, id="mw-content-text")
    for l in all_linked_pages:
        if l.startswith("te_note-"): pass # reference
        elif l.startswith("Project") or l.startswith("Special"): pass # project and special
        elif "redlink" in l:
            k = l.split("=")[1].split("&")[0]
            if k not in unknown_pages:
                unknown_pages.append(k)
                print(unknown_pages[-1])
        # elif l not in all_pages:
        #     all_pages.append(l)
    # all_pages = list(set(all_pages).union(set(all_linked_pages)))
    # print(all_linked_pages)
# print("\n".join(unknown_pages))
