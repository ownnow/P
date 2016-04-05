#使用StringIO()和BytesIO()类来创建文件对象操作字符串数据.
from io import StringIO,BytesIO
s = StringIO()
s1 = StringIO()
num = s.write('hello world\n')
print(num)
print('This is a test',file = s1)
print(s1.getvalue())
s3 = StringIO('Ownnow\nhello')
print(s3.read(4))
print(s3.read())
b = BytesIO()
print(b.write(b'binary data'))
print(b.getvalue())
print('\n')
#读一个gzip或bz2格式的压缩文件,以文本形式读取压缩文件
# import gzip
# with gzip.open('somefile.gz','rt') as f:
#     text = f.read()
# import bz2
# with bz2.open('somefile.bz2','rt') as f:
#     text = f.read()
# #写一个gzip或者bz2格式文件
# with gzip.open('somefile.gz','wt') as f:
#     f.write(text)
# with bz2.open('somefile.bz2','wt') as f:
#     f.write(text)
#当写入压缩数据时，可以使用compresslevel 这个可选的关键字参数来指定一个压缩级别默认的等级是9，也是最高的压缩等级。等级越低性能越好，但是数据压缩程度也越低
#gzip.open()和bz2.open()还有一个特性，它们可以作用在一个已存在并以二进制模式打开的文件上。
f = open('somefile.gz','rb')
with gzip.open(f,'rt') as g:
    text = g.read()