#coding:utf-8
s = '{name} has {n} messages.'
print(s.format(name='Guido',n=37))
name = 'Guido'
n =37
#如果要被替换的变量能在变量域中找到，那么你可以结合使用format map()和vars().vars()还有一个特性就是也适用于对象实例
print(s.format_map(vars()))
class Info:
    def __init__(self,name,n):
        self.name = name
        self.n = n
a = Info('Ownnow',26)
print(s.format_map(vars(a)))
#format,format_map并不能很好的处理变量缺失的情况，这是一个缺陷
# s.format(name='ownnow')  tips:KeyError:'n'。为了弥补这个缺陷，另外定义含有__missing__()方法的字典对象
class safesub(dict):
    '''防止 key 找不到'''
    def __missing__(self,key):
        return '{' + key + '}'
#可以利用这个类包装输入后传递给format_map()
del n 
print(s.format_map(safesub(vars())))
#如果你发现自己在代码中频繁的执行这些步骤，你可以将变量替换步骤用一个工具函数封装起来
import sys 
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))
names = 'OWNNOW'
n1 = 24
print(sub('HELLO {names}'))
print(sub('YOU HAVE {n1} MESSAGES.'))
print(sub('Your favorite color is {color}'))
print('****'*5)    


