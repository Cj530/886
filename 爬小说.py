import requests
from bs4 import BeautifulSoup


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

url = 'http://www.cxbz958.cc/jianlai/'
response = requests.get(url,headers=headers)
content = BeautifulSoup(response.content,'html.parser')
web_cont = content.find('div',class_='listmain')

for web_list in web_cont:
    list_text = web_list.text
    list_link = web_list['href']
    print(f'列表名称:{list_text},\n 列表链接:{list_link} ' )
  

