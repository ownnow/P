#coding:utf-8
#在文本模式打开的文件中写入原始的字节数据,将字节数据直接写入文件的缓冲区即可
import sys
print(sys.stdout.buffer.write(b'Hello'))
#I/O 系统以层级结构的形式构建而成。文本文件是通过在一个拥有缓冲的二进制模式文件上增加一个Unicode 编码/解码层来创建。buffer 属性指向对应的底层文件。如果你直接访问它的话就会绕过文本编码/解码层。本小节例子展示的sys.stdout 可能看起来有点特殊。默认情况下，sys.stdout 总是以文本模式打开的。但是如果你在写一个需要打印二进制数据到标准输出的脚本的话，你可以使用上面演示的技术来绕过文本编码层
print('\n')
#有一个对应于操作系统上一个已打开的I/O 通道(比如文件、管道、套接字等)的整型文件描述符，你想将它包装成一个更高层的Python文件对象
#一个文件描述符和一个打开的普通文件是不一样的。文件描述符仅仅是一个由操作系统指定的整数，用来指代某个系统的I/O 通道。如果你碰巧有这么一个文件描述符，你可以通过使用open() 函数来将其包装为一个Python 的文件对象。你仅仅只需要使用这个整数值的文件描述符作为第一个参数来代替文件名即可
import os
fd = os.open(r'G:\testwork\account.txt',os.O_WRONLY | os.O_CREAT)
f = open(fd,'wt')
f.write('hello world\n')
f.close()
#当高层的文件对象被关闭或者破坏的时候，底层的文件描述符也会被关闭。如果这个并不是你想要的结果，你可以给open() 函数传递一个可选的colsefd=False 。比如：f = open(fd, 'wt', closefd=False)
#创建临时文件和文件夹，在程序执行时创建一个临时文件或目录，并在使用完之后可以自动销毁
#tempfile模块中有很多的函数可以完成这任务，创建一个匿名的临时文件，可以使用tempfile.TemporaryFile
from tempfile import TemporaryFile
import tempfile
with TemporaryFile('w+t',encoding='utf-8') as f:
    f.write('Hello,Ownnow\n')
    f.write('Testing\n')
    f.seek(0)
    data = f.read()
print(tempfile.mkstemp())
print(tempfile.mkdtemp())
print(tempfile.gettempdir())
#将一个Python 对象序列化为一个字节流，以便将它保存到一个文件、存储到数据库或者通过网络传输它.对于序列化最普遍的做法就是使用pickle 模块。为了将一个对象保存到一个文件中
#pickle 是一种Python 特有的自描述的数据编码。通过自描述，被序列化后的数据包含每个对象开始和结束以及它的类型信息。因此，你无需担心对象记录的定义，它总是能工作。举个例子，如果要处理多个对象，你可以这样做
import pickle
f = open('testing','wb')
pickle.dump([1,2,3,4],f)
pickle.dump('hello',f)
pickle.dump({'Apple','Pear','Banana'},f)
f.close()
f = open('testing','rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))
#还能序列化函数，类，还有接口，但是结果数据仅仅将它们的名称编码成对应的代码对象。例如：
import math
print(pickle.dumps(math.cos))
print('\n')
#有些类型的对象是不能被序列化的。这些通常是那些依赖外部系统状态的对象，比如打开的文件，网络连接，线程，进程，栈帧等等。用户自定义类可以通过提供getstate () 和setstate () 方法来绕过这些限制。如果定义了这两个方法，pickle.dump() 就会调用getstate () 获取序列化的对象。类似的， setstate ()在反序列化时被调用。为了演示这个工作原理，下面是一个在内部定义了一个线程但仍然可以序列化和反序列化的类：
import time
import threading
class Countdown:
    def __init__(self,n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()
    def run(self):
        while self.n > 0:
            print('T-minus',self.n)
            self.n -= 1
            time.sleep(5)
    def __getstate__(self):
        return self.n
    def __setstate__(self):
        return self.n
    def __setstate__(self,n):
        self.__init__(n)
c = Countdown(30)
print(c)



