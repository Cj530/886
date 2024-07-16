import requests
import pandas as pd
from bs4 import BeautifulSoup
import jinja2

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

url = 'https://trade.500.com/jczq/?playid=271&g=2&date=2024-05-30'
response = requests.get(url, headers=headers)
content = BeautifulSoup(response.text, 'html.parser')
directory = content.find('div', class_='bet-main')

# 编号
time = [th.text.strip() for th in directory.find_all('td', 'td-no')]

# 赛事
events = [th.text.strip() for th in directory.find_all('td', 'td-evt')]

# 开赛时间
startTime = [th.text.strip() for th in directory.find_all('td', 'td-endtime')]

# 主队
homeTeam = [th.text.strip() for th in directory.find_all('a', 'team-l')]

# vs
vss = [th.text.strip() for th in directory.find_all('i', 'team-bf')]

# 客队
visitors = [th.text.strip() for th in directory.find_all('a', 'team-r')]

# 让球
handicapTheBall = [th.text.strip() for th in directory.find_all('p', 'itm-rangA1',)]

# 提取 betbtn-row itm-rangB1 中的胜平负数据
def extract_data(divs, data_value):
    result = []
    for div in divs:
        p_tag = div.find('p', {'data-value': data_value})
        if p_tag:
            result.append(p_tag.text.strip())
        else:
            result.append(None)
    return result

divs = directory.find_all('div', class_='betbtn-row itm-rangB1')

# 胜
victory = extract_data(divs, '3')
 

# 平
flat = extract_data(divs, '1')
 
# 负
negative = extract_data(divs, '0')


# 确保所有列具有相同的长度
max_length = max(len(time), len(events), len(startTime), len(homeTeam), len(vss), len(visitors), len(handicapTheBall),len(victory),len(flat),len(negative))

def pad_list(lst, length):
    return lst + [None] * (length - len(lst))

time = pad_list(time, max_length)
events = pad_list(events, max_length)
startTime = pad_list(startTime, max_length)
homeTeam = pad_list(homeTeam, max_length)
vss = pad_list(vss, max_length)
visitors = pad_list(visitors, max_length)
handicapTheBall = pad_list(handicapTheBall, max_length)
victory = pad_list(victory, max_length)
flat = pad_list(flat, max_length)
negative = pad_list(negative, max_length)

# 创建DataFrame
df = pd.DataFrame({
    '编号': time,
    '赛事': events,
    '开赛时间': startTime,
    '主队': homeTeam,
    'vs': vss,
    '客队': visitors,
    '让球':handicapTheBall,
    '胜':victory,
    '平':flat,
    '负':negative
})



# 保存带有样式的 DataFrame 到 Excel 文件
df.to_excel('06-12.xlsx', engine='openpyxl', index=False)

print("已生成.")