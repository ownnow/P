#coding:UTF-8
# 使用Unix Shell中常用的通配符(比如*.py,Dat[0-9]*.csv等)去匹配文本字符串
# fnmatch模块提供了两个函数—fnmatch()和fnmatchcase()用来实现匹配
from fnmatch import fnmatch,fnmatchcase
import re
print(fnmatch('foo.txt', '*.TXT'))
print(fnmatchcase('word.doc', '*.doc'))
print(fnmatch('Dat1.csv', 'Dat[0-9]*'))
names = ['Dat1.csv','Dat2.csv','config.ini','foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])
print('****'*10)
# 这两个函数通常会被忽略的一个特性是在处理非文件名的字符串时候它们也是很有用的
addresses = [
'5412 N CLARK ST',
'1060 W ADDISON ST',
'1039 W GRANVILLE AVE',
'2122 N CLARK ST',
'4802 N BROADWAY',
]
print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])

text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah',text.startswith('yeah'),text.endswith('no'),text.find('no'))

text1 = '11/27/2012'
text2 = 'Nov 27,2012'
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
if re.match('\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')
    
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')
if datepat.match(text2):
    print('yes')
else:
    print('no')
    
# match() 总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位
# 置，使用findall() 方法去代替
text3 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text3))
print('----'*10)
# 在定义正则式的时候，通常会利用括号去捕获分组
# 捕获分组可以使得后面的处理更加简单，因为可以分别将每个组的内容提取出来
datepats = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepats.match('11/27/2012')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
month,day,year = m.groups()
print(month,day,year)
print("@@@@@@"*10)
print(datepats.findall(text3))
for month,day,year in datepats.findall(text3):
    print('{}-{}-{}'.format(year,month,day),end = '   ')
# findall() 方法会搜索文本并以列表形式返回所有的匹配。如果你想以迭代方式
print('***'*10)
# 返回匹配，可以使用finditer()方法来代替
for m in datepats.finditer(text3):
    print(m.groups())
    
m = datepats.match('11/27/2012abcdef')
print(m)
print(m.group())

datepat1 = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat1.match('11/27/2012abcdef'))
print(datepat1.match('11/27/2012'))
print(re.findall(r'(\d+)/(\d+)/(\d+)', text3))
    
    
