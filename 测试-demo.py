import re

pattern = re.compile(r'\d+') #查找数字
result1 = pattern.findall('blue 123 google 456',0,5)

print(result1)


it = re.finditer(r"\d+","123453435fdg3434")
for match in it:
    print(match.group())

    