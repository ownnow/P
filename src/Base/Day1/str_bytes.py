#coding:utf-8
data = b'Hello world'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))
data1 = bytearray(b'Hello World')
print(data1[0:5])
data2 = b'FOO:BAR,SPAM'
import re 
print(re.split(b'[:,]', data2))
#大多数情况下，在文本字符串上的操作均可用于字节字符串。然而，这里也有一些需要注意的不同点。首先，字节字符串的索引操作返回整数而不是单独字符.这种语义上的区别会对于处理面向字节的字符数据有影响
a = 'Hello World'
print(a[0])
print(a[1])
b1 = b'Hello world'
print(b1[0])
print(b1[1])
#字节字符串不会提供一个美观的字符串表示，也不能很好的打印出来，除非它们先被解码为一个文本字符串.也不存在任何适用于字节字符串的格式化操作,如果你想格式化字节字符串，你得先使用标准的文本字符串，然后将其编码为字节字符串
s = b'HELLO WORLD'
print(s)
print(s.decode('ascii'))
print('{:5s} {:5d} {:5.2f}'.format('ACME',100,490.1).encode('ascii'))
#使用字节字符串可能会改变一些操作的语义，特别是那些跟文件系统有关的操作。比如，如果你使用一个编码为字节的文件名，而不是一个普通的文本字符串，会禁用文件名的编码/解码
with open('xf1o.txt','w') as f:
    f.write('spicy')
    f.close()
import os
print(os.listdir(b'.'))

'''
为了提升程序执行的速度会倾向于使用字节字符串而不
是文本字符串。尽管操作字节字符串确实会比文本更加高效(因为处理文本固有的
Unicode 相关开销)。这样做通常会导致非常杂乱的代码。你会经常发现字节字符串并
不能和Python 的其他部分工作的很好，并且你还得手动处理所有的编码/解码操作。
坦白讲，如果你在处理文本的话，就直接在程序中使用普通的文本字符串而不是字节
字符串。
'''

