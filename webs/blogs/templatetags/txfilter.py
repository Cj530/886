from django import template
register = template.Library()  #注册变量的名称必须是register的库，库里的函数Library()

@register.filter
def FilterMinGan(value,arg1):
    filstr1= str(value)
    if filstr1.find("敏感词1")>=0:
        return filstr1.replace("敏感词1",arg1)
    else:
        return value