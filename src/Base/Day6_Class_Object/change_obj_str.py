#coding:utf-8
#改变对象实例的打印或显示输出，更具有可读性。可以重新定义它的__str__()和__repr__()方法
class Pair:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
    #__repr__()方法返回一个实例的代码表示形式，通常用来重新构造这个实例。内置的repr()函数返回这个字符串，跟我们使用交互式解释器显示的值是一样的
        return 'Pair({0.x!r},{0.y!r})'.format(self)
    #return 'Pair(%r,%r)' % (self.x,self.y)
    # >>>p --->Pair(3,4)  __repr__() output
    def __str__(self):
    #__str__()方法将实例转化为一个字符串，使用str()或print()函数会输出这个字符串
        return '({0.x!s},{0.y!s})'.format(self)
    #格式化代码{0.x}对应的是第1个参数的x属性,在上面的函数中0实际上指的就是self本身
p = Pair(3,4)
print(p)#__str__()output
#!r 格式化代码指明输出使用repr__()__来代替默认的__str__()
p1 = Pair(1,2)
print('p1 is {0!r}'.format(p1))
print('p is {0}'.format(p))
print('\n')
#自定义字符串的格式化，通过format()函数和字符串方法使得一个对象能支持自定义的格式化，为了自定义字符串的格式化，需要在类上定义__format__()方法
_format = {
           'ymd':'{d.year}-{d.month}-{d.day}',
           'mdy':'{d.month}/{d.day}/{d.year}',
           'dmy':'{d.day}/{d.month}/{d.year}'
           }
class Date:
    def __init__(self,year,month,day):
        self.year = year 
        self.month = month 
        self.day = day 
        
    def __format__(self,code):
        if code == '':
            code = 'ymd'
        fmt = _format[code]
        return fmt.format(d=self)
    
d = Date(2016,4,6)
print(format(d))
print(format(d,'mdy'))
print('The date is {:ymd}'.format(d))
print('The date is {:mdy}'.format(d))

from datetime import date 
d1 = date(2016,4,1)
print(format(d1))
print(format(d1,'%A, %B, %d, %Y'))
print('The start is {:%A %B %d %Y}.WELCOME!'.format(d1))
print('The end is {:%d %b %Y}. GoodBye'.format(d1))
print('\n')
#让对象支持上下文管理协议(with语句)。让一个对象兼容with语句，得实现__enter__()和__exit__()方法
from socket import socket,AF_INET,SOCK_STREAM
class LazyConnection:
    def __init__(self,address,family=AF_INET,type=SOCK_STREAM):
        self.address = address 
        self.family = family
        self.type = type
        self.sock = None
        
    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected!')
        self.sock = socket(self.family,self.type)
        self.sock.connect(self.address)
        return self.sock
    def __exit__(self,exc_ty,exc_val,tb):
        self.sock.close()
        self.sock = None
from functools import partial
conn = LazyConnection(('www.python.org'),80)
with conn as s:
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv,8192),b''))
    
    
    











        

