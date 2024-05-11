import requests
from bs4 import BeautifulSoup
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

url = 'https://www.junke666.com/cate_list/'
url2 = ''
response = requests.get(url,headers=headers)
response.encoding = 'gbk'
content = BeautifulSoup(response.text,'html.parser')
web_page = content.find('div',class_='flex-1') 
web_page_name = web_page.find_all('a')[1:]
for page_cont in web_page_name:
    page_url = page_cont.get('href')
    page_name = page_cont.text
    caricature_urls = 'https://www.junke666.com' + page_url
    print('漫画名:',page_name)
    print('漫画链接:',caricature_urls)
    print('#'*30)
    response = requests.get(url = caricature_urls)
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text,'html.parser')
    cart_cont = soup.find_all('div',class_='mh-item')
    for cart_conts in cart_cont:
        cart_name = cart_conts.h2.get_text()
        print('漫画名:',cart_name)
            































class UrlManager():
    '''
    url 管理器
    '''
    def __init__(self):     #url初始化函数
        self.new_urls = set()   # 定义新的待爬取的url
        self.old_urls = set()   # 已经爬取的url

    def add_new_url(self, url):  # 新增URL
        if url is None or len(url) == 0:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        self.new_urls.add(url)

    def add_new_urls(self, urls): # 批量增加URL
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def get_url(self):    # 获取一个待爬取URL 方法
        if self.has_new_url():
            url = self.add_new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None
   
    def has_new_url(self):  # 判断一个待爬取的URL
        return len(self.new_urls) > 0
    

 
