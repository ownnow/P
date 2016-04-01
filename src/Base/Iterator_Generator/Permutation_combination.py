#coding:utf-8
#迭代遍历一个集合中元素的所有可能的排列或组合.itertools 模块提供了三个函数来解决这类问题。其中一个是itertools.permutations(),它接受一个集合并产生一个元组序列，每个元组由集合中所有元素的一个可能排列组成
from itertools import permutations,combinations, combinations_with_replacement
from _collections import defaultdict
items = ['a','b','c']
for p in permutations(items):
    print(p)
#想得到指定长度的所有排列，你可以传递一个可选的长度参数
for p in permutations(items,2):
    print(p)
print('---'*10)
#使用itertools.combinations()可得到输入集合中元素的所有的组合
for c in combinations(items,3):
    print(c)
for c in combinations(items,2):
    print(c)
for c in combinations(items,1):
    print(c)
    
#在计算组合的时候， 一旦元素被选取就会从候选中剔除掉(比如如果元素’a’ 已经被选取了， 那么接下来就不会再考虑它了)。而函数itertools.combinations with replacement() 允许同一个元素被选择多次，
for c in combinations_with_replacement(items,3):
    print(c)
print('---'*10)
#在迭代一个序列的同时跟踪正在被处理的元素索引,内置的enumerate() 函数可以很好的解决这个问题
my_list = ['a','b','c']
for idx,val in enumerate(my_list):
    print(idx,val)
for i,v in enumerate(my_list,1):#行号从1开始
    print(i,v)
    
#遍历文件时想在错误消息中使用行号定位
def parse_data(filename):
    with open(filename,'rt') as f:
        for lineno,line in enumerate(f,1):
            fields = line.split()
            try:
                count = int(fields[1])
                ...
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno,e))
#enumerate()对于跟踪某些值在列表中出现的位置是很有用的。所以，如果你想将一个文件中出现的单词映射到它出现的行号上去，可以很容易的利用enumerate()来完成
word_summary = defaultdict(list)
with open('passwd.txt','r') as f:
    lines = f.readlines()
for idx,line in enumerate(lines):
    #在当前行创建一个单词列表
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)
#如果你处理完文件后打印word summary ，会发现它是一个字典(准确来讲是一个defaultdict )，对于每个单词有一个key ，每个key 对应的值是一个由这个单词出现的行号组成的列表。如果某个单词在一行中出现过两次，那么这个行号也会出现两次，同时也可以作为文本的一个简单统
data = [(1,2),(3,4),(5,6),(7,8)]
for n,(x,y) in enumerate(data):
    print(n,(x,y))
#同时迭代多个序列，每次分别从一个序列中提取一个元素。使用zip()函数迭代长度跟参数中最短序列长度一致
xpts = [1,5,4,2,10,7]
ypts = [101,78,37,15,62,99]
zpts = [20,35,29]
for x,y in zip(xpts,ypts):
    print(x,y)
print('--'*5)
for x,z in zip(xpts,zpts):
    print(x,z)
from itertools import zip_longest
for i in zip_longest(xpts,zpts):
    print(i)
for i in zip_longest(xpts,zpts,fillvalue = 0):
    print(i)
print('---'*10)
headers = ['name','shares','price']
values = ['ACME',100,490.1]
s = dict(zip(headers,values))
print(s)
for name,val in zip(headers,values):
    print(name,'=',val)
print(list(zip(xpts,ypts,zpts)))
print(list(zip(xpts,ypts)))
#不同集合上元素的迭代，在多个对象执行相同的操作，但是这些对象在不同的容器中，在代码不失可读性的情况下避免写重复循环。itertools.chain()方法可以用来简化这个任务。它接受一个可迭代对象列表作为输入，并返回一个迭代器，有效的屏蔽掉在多个容器中的细节，代码如下
from itertools import chain
a = [1,2,3,4]
b = ['x','y','z']
for x in chain(a,b):
    print(x)
#使用chain()的一个常见场景是当你相对不同对象的集合中所有元素执行








