#使用路径名来获取文件名，目录名，绝对路径等等。使用os.path模块中的函数来操作路径名
#coding:utf-8
import os
import sys
from _io import TextIOWrapper
path = r'G:\testwork\lock.txt'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.join('tmp','data',os.path.basename(path)))
#测试文件是否存在
print(os.path.exists(r'G:\testwork'))#文件目录是否存在
print(os.path.isfile(r'G:\testwork\login.py'))#是否是一个正规的文件
print(os.path.isdir(r'G:\testwork'))#是否是一个目录
print(os.path.islink(r'c:\python34\bin'))#是否是一个符号链接
print(os.path.realpath(r'c:\python34\lib'))#获得相关文件
#获取元数据(文件大小,修改日期)，也可以用os.path模块
print(os.path.getsize(r'G:\testwork\account.txt'))
print(os.path.getmtime(r'G:\testwork\account.txt'))
import time
print(time.ctime(os.path.getmtime(r'G:\testwork\lock.txt')))
print(os.path.getsize(r'G:\testwork\login.py'))
names = [name for name in os.listdir(r'G:\testwork') if os.path.isfile(os.path.join(r'G:\testwork',name))]
print(names)
dirnames = [name for name in os.listdir(r'C:\python34\lib') if os.path.isdir(os.path.join(r'C:\python34\lib',name))]
print(dirnames)
pyfiles = [name for name in os.listdir(r'G:\testwork') if name.endswith('.py')]
print(pyfiles)
print('\n')
import glob
pyfiles1 = glob.glob(r'G:\testwork\*.py')
name_sz_date = [(name,os.path.getsize(name),os.path.getmtime(name)) for name in pyfiles1]
for name,size,mtime in name_sz_date:
    print(name,size,mtime)
file_metadata = [(name,os.stat(name)) for name in pyfiles1]
for name,meta in file_metadata:
    print(name,meta.st_size,meta.st_mtime)
print('\n')
#print(pyfiles1)
from fnmatch import fnmatch
pyfiles3 = [name for name in os.listdir(r'C:\python34\lib') if fnmatch(name, '*.py')]
print(pyfiles3)
print('\n')
#忽略文件名编码，
print(sys.getfilesystemencoding())
with open('jalape\xf1o.txt','w') as f:
    f.write('Spicy!')
    f.close()
print(os.listdir('.'))
print(os.listdir(b'.'))
print('--'*20)
#打印不合法的文件名。你的程序获取了一个目录中的文件名列表，但是当它试着去打印文件名的时候程序崩溃，出现了UnicodeEncodeError 异常和一条奇怪的消息—— surrogates not allowed
#当打印未知的文件名时，使用下面的方法可以避免这样的错误
# def bad_filename(filename):
#     return repr(filename)[1:-1]
# try:
#     print(filename)
# except UnicodeEncodeError:
#     print(bad_filename(filename))
# def bad_filename1(filename):
#     temp = filename.encode(sys.getfilesystemencoding(),errors = 'surrogateescape')
#     return temp.decode('latin-1')
print('--'*20)
#增加或改变已打开文件的编码
#给一个以二进制模式打开的文件添加Unicode 编码/解码方式，可以使用io.TextIOWrapper() 对象包装它
import urllib.request
import io
u = urllib.request.urlopen('http://www.python.org')
f = TextIOWrapper(u,encoding='utf-8')
text = f.read()
#print(text)
print('***'*15)
#如果你想修改一个已经打开的文本模式的文件的编码方式，可以先使用detach()方法移除掉已存在的文本编码层，并使用新的编码方式代替
print(sys.stdout.encoding)
sys.stdout = TextIOWrapper(sys.stdout.detach(),encoding='latin-1')
print(sys.stdout.encoding)
#detach() 方法会断开文件的最顶层并返回第二层，之后最顶层就没什么用了
f1 = open('sample1.txt','w')
print(f1)
print(f1.buffer)
print(f1.buffer.raw)
b = f.detach()
print(b)