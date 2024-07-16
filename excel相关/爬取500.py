import requests
import pandas as pd
from bs4 import BeautifulSoup




headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

url = 'https://trade.500.com/jczq/?playid=270&g=2&date=2024-05-27'
response = requests.get(url,headers=headers)
content = BeautifulSoup(response.text,'html.parser')
directory = content.find('div',class_='bet-main')


#编号
time = [] 
for th in directory.find_all('td','td-no'):
        time.append(th.text.strip())

#赛事
events =[]
for th in directory.find_all('td','td-evt'):
        events.append(th.text.strip())

#开赛时间
startTime = []
for th in directory.find_all('td','td-endtime'):
        startTime.append(th.text.strip())

#主队
homeTeam = []
for th in directory.find_all('span','team-l'):
        homeTeam.append(th.text.strip())

#vs
vss = []
for th in directory.find_all('i','team-vs'):
        vss.append(th.text.strip())
#客队
visitors = []
for th in directory.find_all('span','team-r'):
        visitors.append(th.text.strip())

Balls = []
for th in directory.find_all('td','td-betbtn'):
        Balls.append(th.text.strip())
Bone =[]
for th in directory.find_all('p','td-betbtn'):
        Bone.append(th.text.strip())
Boneo = []
for th in directory.find_all('p','betbtn'): 
        Boneo.append(th.text.strip())

data =({time},{events},{startTime},{homeTeam})

# # 找到最长列的长度
# max_length = max(len(v) for v in data.values())

# # 对每列进行填充，使得所有列长度一致
# for key, value in data.items():
#     if len(value) < max_length:
#         th[key] += [None] * (max_length - len(value))

excels = pd.DataFrame({
        '编号': time,
        '赛事': events,
        '开赛时间': startTime,
        '主队': homeTeam,
        # 'VS': vss,
        # '客队':visitors,
        # '主队VS客队':contingent,
        # '0球 1球 2球 3球 4球 5球 6球 7+球':Balls
        # '0球':Boneo
  
})

print(excels)


# output_file ='table1.xlsx'
# excels.to_excel(output_file,index=False)

# print(f"数据已保存为excel文件:{output_file}")