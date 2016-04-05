#读写各种不同编码的文本数据，比如ASCII,UTF-8,UTF-16编码等。
#使用rt模式读取文本文件
with open('passwd.txt','rt') as f:
    data = f.read()
    print(data)
with open('passwd.txt','rt') as f:
    for line in f:
        pass
#使用wt模式写入一个文本文件，如果之前文件内容存在则清除并覆盖
with open('somefile.txt','wt') as f:
    f.write('hello,ownnow')
    f.write('xian')
    f.close()
    
#将print()函数的输出重定向到一个文件中
with open('g:/testwork/text.txt','wt') as f:
    print('hello,ownnow',file = f)
    
#使用print()函数输出数据，想改变默认的分隔符或者行尾符，使用sep,end关键字参数，得到你想要的方式输出
print('ACME',50,91.5)
print('ACME',50,91.5,sep = ',')
print('ACME',50,91.5,sep = ',',end='!!\n')
for i in range(5):
    print(i,end=' ')#end输出禁止换行
print('\n')
row = ('ACME',50,91.5)
print('@'.join(str(x) for x in row))
print('\n')
#在读取二进制数据的时候，字节字符串和文本字符串的语义差异可能会导致一个潜在的陷阱。特别需要注意的是，索引和迭代动作返回的是字节的值而不是字节字符串。比如：
t = 'Hello,World'
print(t[0])
for c in t:
    print(c,end=' ')
print('\n')
b = b'Hello,Ownnow'
print(b[0])
for c in b:
    print(c,end=' ')
#从二进制模式的文件读取或写入文本数据，必须确保要进行解码和编码操作
# with open('somefile.bin','rb') as f:
#     data = f.read(16)
#     text = data.decode('utf-8')
# with open('somefile.bin','wb') as f:
#     text = 'Hello,World'
#     f.write(text.encode('utf_8'))
#在写文件时通常会遇到的一个问题的完美解决方案(不小心覆盖一个已存在的文件)。一个替代方案是先测试这个文件是否存在，像下面这样：
print('\n')
with open('somefile.txt','wt') as f:
    f.write('My name is Ownnow!\nhello\n')
    f.close()
with open('somefile.txt','a') as f:
    f.write('Good Luck!')
    f.close()
import os
print(os.getcwd())
if not os.path.exists('somefile'):
    with open('somefile','wt') as f:
        f.write('Hello\n')
else:
    print('File already extists!')