#将一个多层嵌套的序列展开成一个单层列表
#写一个包含yield from语句的递归生成器来解决
from collections import Iterable
def flatten(items,ignore_types = (str,bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x
items = [1,2,[3,4,[5,6],7],8]
for x in flatten(items):
    print(x)
items1 = ['Dave','Paula',['Thomas','Lewis'],'Ownnow']
for x in flatten(items1):
    print(x)
#isinstance(x,Iterable)检查某个元素是否是可迭代的。如果是的话，yield from 就会返回所有子例程的值。最终返回结果就是一个没有嵌套的简单序列了。
#额外的参数ignore_types 和检测语句isinstance(x,ignore_types) 用来将字符串和字节排除在可迭代对象外，防止将它们再展开成单个的字符。这样的话字符串数组就能最终返回我们所期望的结果了
print('--'*15)
#顺序迭代合并后的排序迭代对象.
#有一些列排序序列，想将他们合并后得到一个排序序列并在上面迭代遍历，可以使用heapq.merge()函数
import heapq
a = [1,4,7,10]
b = [2,5,6,11]
for c in heapq.merge(a,b):
    print(c)
#heapq.merge可迭代特性意味着它不会立马去读所有序列。这就意味着你可以在非常长的序列中使用它，而不会有太大的开销。下面一个例子演示如何合并两个排序文件：
# with open('sorted_file_1','rt') as file1,open('sorted_file_2','rt') as file2,open('merged_file','wt') as outf:
#     for line in heapq.merge(file1,file2):
#         outf.write(line)
#要强调的是heapq.merge()需要所有输入序列必须是排过序的。特别的，它不会预先读取所有数据到堆栈中或者预先排序，也不会对输入做任何排序检测。它仅仅是检查所有序列的开始部分并返回最小的那个，这个过程一直会持续到所有输入序列中的元素都被遍历完
print('---'*8)
#迭代器代替while无限循环。
import sys 
f = open('passwd.txt')
for chunk in iter(lambda:f.read(10),''):
    n = sys.stdout.write(chunk)
    print(n)