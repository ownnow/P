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
