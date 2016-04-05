#想在一个固定长度记录或者数据块的集合上迭代，而不是一行一行的在文件中迭代，可以使用iter和functools.partial()函数
# from functools import partial
# RECODR_SIZE = 32
# with open('somefile.data','rb') as f:
#     records = iter(partial(f.read,RECODR_SIZE),b'')
#     for r in records:
#         pass
#这个例子中的records 对象是一个可迭代对象，它会不断的产生固定大小的数据块，直到文件末尾。要注意的是如果总记录大小不是块大小的整数倍的话，最后一个返回元素的字节数会比期望值少

# iter() 函数有一个鲜为人知的特性就是，如果你给它传递一个可调用对象和一个标记值，它会创建一个迭代器。这个迭代器会一直调用传入的可调用对象直到它返回标记值为止，这时候迭代终止。
# 在例子中， functools.partial 用来创建一个每次被调用时从文件中读取固定数目字节的可调用对象。标记值b'' 就是当到达文件结尾时的返回值。
# 最后再提一点，上面的例子中的文件时以二进制模式打开的。如果是读取固定大小的记录，这通常是最普遍的情况。而对于文本文件，一行一行的读取(默认的迭代行为) 更普遍点。
print('\n')
#读取二进制数据到可变缓冲区,为了读取数据到一个可变数组中，使用文件对象的readinto()方法
import os.path
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename,'rb') as f:
        f.readinto(buf)
    return buf 
with open('sample.bin','wb') as f:
    f.write(b'HELLO world')
buf = read_into_buffer('sample.bin')
print(buf)
buf[0:5] = b'Hallo'
print(buf)
m1 = memoryview(buf)
m2 = m1[-5:]
print(m2)
m2[:] = b'WORLD'
print(buf)
print('\n')
#内存映射一个二进制文件到一个可变字节数组中，为了随机访问它的内容或者是原地做些修改。使用mmap模块来做内存映射这个文件
import os
import mmap
def memory_map(filename,access = mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename,os.O_RDWR)
    return mmap.mmap(fd,size,access=access)
#为了使用这个函数，你需要有一个已创建并且内容不为空的文件
size = 1000000
with open('data','wb') as f:
    f.seek(size-1)
    f.write(b'\x00')
m = memory_map('data')
print(len(m))
print(m[1:10])
print(m[1:100])
print(m[0])
m[0:12] = b'Hello,Ownnow'
m.close()
with open('data','rb') as f:
    print(f.read(12))
with memory_map('data') as m:
    print(len(m))
    print(m[0:10])
    print(m.close())
ms = memory_map('data')
v = memoryview(ms).cast('I')
v[0] =7
print(ms[0:4])
ms[0:4] = b'\x07\x01\x00\x00'
print(v[0])