#coding:UTF-8
# 使用Unix Shell中常用的通配符(比如*.py,Dat[0-9]*.csv等)去匹配文本字符串
# fnmatch模块提供了两个函数—fnmatch()和fnmatchcase()用来实现匹配
from fnmatch import fnmatch,fnmatchcase
print(fnmatch('foo.txt', '*.txt'))