#coding:utf-8
#构建了一个自定义容器对象，里面包含有列表、元组或其他可迭代对象。你想直接在你的这个新容器对象上执行迭代操作
#实际上你只需要定义一个iter () 方法，将迭代操作代理到容器内部的对象上去。
class Node:
    def __init__(self,value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self,node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)
print('----'*10)
def frange(start,stop,increment):
    x = start
    while x < stop:
        yield x
        x += increment
for n in range(0,4,2):
    print(n)
print(list(frange(0, 5, 0.5)))
#一个函数中需要有一个yield 语句即可将其转换为一个生成器。跟普通函数不同的是，生成器只能用于迭代操作
def countdown(n):
    print('Starting to count from',n)
    while n>0:
        yield n
        n -=1
    print('Done!')
    
c = countdown(3)
print(c)
print(next(c))
print(next(c))
print(next(c))
#print(next(c))
def count(n):
    while True:
        yield n
        n +=1
c = count(0)
print(c)
#itertools.islice()适用于在迭代器和生成器上做切片操作
import itertools
for x in itertools.islice(c,10,20):
    print(x)
#迭代器和生成器不能使用标准的切片操作，因为它们的长度事先我们并不知道(并且也没有实现索引)。函数islice() 返回一个可以生成指定元素的迭代器，它通过遍历并丢弃直到切片开始索引位置的所有元素。然后才开始一个个的返回元素，并直到切片结束索引位置。
#这里要着重强调的一点是islice() 会消耗掉传入的迭代器中的数据。必须考虑到迭代器是不可逆的这个事实。所以如果你需要之后再次访问这个迭代器的话，那你就得先将它里面的数据放入一个列表中
print('---'*10)
#已经明确知道了要跳过的元素的个数的话，那么可以使用itertools.islice()来代替
from itertools import islice
items = ['a','b','c',1,4,10,15]
for x in islice(items,3,None):
    print(x)
#islice() 函数最后那个None 参数指定了你要获取从第3 个到最后的所有元素，如果None 和3 的位置对调，意思就是仅仅获取前三个元素恰恰相反，(这个跟切片的相反操作[3:] 和[:3] 原理是一样的
for x in islice(items,None,3):
    print(x)
with open('passwd.txt') as f:
    for line in f:
        print(line,end='\n')
#itertools 模块中有一些函数可以完成这个任务。首先介绍的是itertools.dropwhile() 函数。使用时，你给它传递一个函数对象和一个可迭代对象。它会返回一个迭代器对象，丢弃原有序列中直到函数返回True 之前的所有元素，然后返回后面所有元素。
'''
##
# User Database
##
#Note that this file is consulted directly only when #the system is running
# in single-user mode. At other times, this #information is provided by
# Open Directory.
...
##
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0:System Administrator:/var/root:/bin/sh
        '''
print('----'*10)
#如果你想跳过开始部分的注释行的话，可以这样做：
from itertools import dropwhile
with open('passwd.txt') as f1:
    for line in dropwhile(lambda line:line.startswith("#"),f1):
        print(line,end='')