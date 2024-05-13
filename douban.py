import requests
from bs4 import BeautifulSoup
import pprint
import json

page_indexs = range(0,250,25)
list(page_indexs)


def download_all_htmls():
    htmls =[]
    for idx in page_indexs:
        url = f'https://movie.douban.com/top250?start={idx}&fileter='
        print("craw html:",url)
        r = requests.get(url)
        if r.status_code !=200:
            raise Exception("error")
        htmls.append(r.text)
    return htmls
    
htmls = download_all_htmls()
