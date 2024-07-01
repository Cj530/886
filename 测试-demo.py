money = 5000000
name = None
#要求客户输入姓名
name = input("输入姓名")

#定义查询函数
def query(show_money):
    if show_money:
        print("------------------查询余额------------")
    print(f"{name},您好，您的余额剩余：{money}元")

#定义存款函数
def saving(num):
    global money  #money 在函数内部定义全局变量
    money+=num
    print(f"{name},您好，您存款{num}元成功")

    query(False)

 def get_money(num):
    global money   #定义全局变量
    money -=num
    print("--------------取款---------------")
    print(f"{name},您好，您存款{num}元成功")

    query(False)

def main():
    print(f'----------------主菜单----------------')
    print(f'{name},h欢迎您来到什么什么')
    print(f"查询余额[输入]")
