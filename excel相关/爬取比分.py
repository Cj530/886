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

# 投注区
Balls = [th.text.strip() for th in directory.find_all('p', 'sbetbtn')]





# 确保所有列具有相同的长度
max_length = max(len(time), len(events), len(startTime), len(homeTeam), len(vss), len(visitors), len(Balls))

def pad_list(lst, length):
    return lst + [None] * (length - len(lst))

time = pad_list(time, max_length)
events = pad_list(events, max_length)
startTime = pad_list(startTime, max_length)
homeTeam = pad_list(homeTeam, max_length)
vss = pad_list(vss, max_length)
visitors = pad_list(visitors, max_length)
Balls = pad_list(Balls, max_length)
# Boneo = pad_list(Boneo, max_length)
# Bonea = pad_list(Bonea, max_length)
# Boneb = pad_list(Boneb, max_length)
# Bonec = pad_list(Bonec, max_length)
# Boned = pad_list(Boned, max_length)
# Bonee = pad_list(Bonee, max_length)
# Bonef = pad_list(Bonef, max_length)
# Boneg = pad_list(Boneg, max_length)
# 创建DataFrame
df = pd.DataFrame({
    '编号': time,
    '赛事': events,
    '开赛时间': startTime,
    '主队': homeTeam,
    'vs': vss,
    '客队': visitors,
    '投注区':Balls
    # '0球': Boneo,
    # '1球':Bonea,
    # '2球':Boneb,
    # '3球':Bonec,
    # '4球':Boned,
    # '5球':Bonee,
    # '6球':Bonef,
    # '7+球':Boneg,
})

# 定义一个样式函数用于 vss 列
def highlight_vss(val):
    return 'color: red' if val == 'VS' else ''

# # 定义一个样式函数用于 Boneo 列
# def highlight_boneo(val):
#     return 'color: red' if val == 'okok' else ''

# # 使用 Styler 对象的 apply 和 applymap 方法，将样式应用到 DataFrame 中的特定列
# styled_df = df.style.applymap(highlight_vss, subset=['vs'])
# styled_df = styled_df.applymap(highlight_boneo, subset=['0球'])

# 保存带有样式的 DataFrame 到 Excel 文件
df.to_excel('06-25.xlsx', engine='openpyxl', index=False)

print("Styled DataFrame has been saved to 'styled_data.xlsx'.")