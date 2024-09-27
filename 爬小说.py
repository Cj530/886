import requests
from bs4 import BeautifulSoup


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

url = 'http://www.cxbz958.cc/jianlai/'
response = requests.get(url,headers=headers)
content = BeautifulSoup(response.content,'html.parser')
web_cont = content.find('div',class_='listmain')
web_dd = web_cont.find_all('a')

for list in web_dd:
    list_name = list.get_text()
    list_url = list.get('href')
    print(f'章节名:{list_name}\n章节链接:{list_url}')
     

