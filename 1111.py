import requests

url = 'https://www.sogou.com'


response = requests.get(url)
#状态码
print(response.status_code) 

print(response.reason)

print(response.apparent_encoding)

