import requests
from bs4 import BeautifulSoup

# 解析当前页面的文章名链接
# def cols_soup(soup):
#     essays = []
#     for article in articles:
#         title_tag = article.find('h2',class_='entry-title').find('a')  
#         if title_tag:
#             title = title_tag.get_text().strip()
#             link = title_tag['href']
#             essays.append(title)
#     return essays

# 查找下一页的 URL
def find_net_page_url(soup):
    next_page_url = soup.find('div',class_='infinite-scroll-button')
    if next_page_url:
        return next_page_url['href']
    else:
        return None
    

#目标网站
url ='http://www.bdsmms.com/bdsm'

#发送请求
response = requests.get(url) 

#检查请求是否成功
if response.status_code == 200:
    #解析HTML内容
    soup = BeautifulSoup(response.content, 'html.parser')

    #找到网站栏目的div
    articles = soup.find_all('a', class_='name')

    for column in articles:
        #提取栏目标题
        coltitle = column.text
        colink = column['href']
        print(f"栏目名:{coltitle},\n{colink}")

        #遍历栏目的链接
        col_response = requests.get(colink)
        col_soup = BeautifulSoup(col_response.content,'html.parser')
        print(f'爬取文章页面-文章名-文章链接')
        
        for title_tag in col_soup.find_all(attrs={"class":"entry-title"}):
            #爬取文章页面的文章名
            link_tag = title_tag.find('a')
            title = link_tag.get_text().strip()
            link = link_tag['href']
            print([title],link)     

        #如果有分页按钮，继续加载更多内容
        all_links = []
        page_num =1
        while True:
            article_links =  get_    
else:
    print(f'请求失败，状态码:{response.status_code}')



 
