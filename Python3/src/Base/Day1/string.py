#coding:utf-8
# re.split()方法因为它允许你为分隔符指定多个正则模式。比如，
# 在上面的例子中，分隔符可以是逗号，分号或者是空格，并且后面紧跟着任意个的空格。
# 只要这个模式被找到，那么匹配的分隔符两边的实体都会被当成是结果中的元素返回
import re 
line = 'asdf fjdk; afed, fjek,asdf, foo'
sp = re.split(r'[;,\s]', line)
print(sp)

# 使用re.split() 函数时候，需要特别注意的是正则表达式中是否包含一个括
# 号捕获分组。如果使用了捕获分组，那么被匹配的文本也将出现在结果列表中。
fields = line
fields = re.split(r'(;|,|\s)\s*', fields)
print(fields)

values = fields[::2]
delimiters = fields[1::2] + ['']
print(values,'\n',delimiters)
# Reform the line using the same delimiters
print(''.join(v+d for v,d in zip(values,delimiters)))
print(re.split(r'(?:,|;|\s)\*s', line))
print('****'*20)
filename = 'spam.txt'
print(filename.endswith('.txt'),'\n',filename.startswith('file:'))
url = 'http://www.baidu.com'
print(url.startswith('http:'))
import os
print(os.chdir(r'd:/test/file/'))
print(os.getcwd())
filenames = os.listdir()
print(filenames)
print('@@@@@@@@@@@'*5)
print([name for name in filenames if name.endswith(('.c','.h','.txt'))])
#如果iterable的任何元素不为0、''、False,all(iterable)返回True。
#如果iterable为空，返回False
print(any(name.endswith('.py') for name in filenames))
print('---------'*5)
choices = ['http:','ftp:']
url = 'http://www.python.org'
# 这个方法中必须要输入一个元组作为参数。如果你恰巧有一个list 或
# 者set 类型的选择项，要确保传递参数前先调用tuple() 将其转换为元组类型
print(url.startswith(tuple(choices)))
stext ='spam.txt'
print(stext[-4:] == '.txt')
print(url[:5] == 'http:' or url[:6]=='https:' or url[:4] == 'ftp:')
print('@@@@@@@'*10)
import re
res = re.match('http:|https:|ftp:', url)
print(res)









