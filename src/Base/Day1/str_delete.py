#coding:utf-8
#strip()方法能用于删除开始或结尾的字符。lstrip()和rstrip()分别从左和
#从右执行删除操作。默认情况下，这些方法会去除空白字符，但是你也可以指定其他字符
s = ' hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())
t = '-----hello======'
print(t.strip('-='))
s1 = 'ownnow          @hotmail.com'
print(s1.replace(' ', ''))
import re 
print(re.sub('\s+', '', s1))
#能想消除整个区间上的字符或者去除变音符。
#可以使用str.translate()方法
trans = 'pýtĥöñ\fis\tawesome\r\n'
print(trans)
remap = {
         ord('\t'):' ',
         ord('\f'):' ',
         ord('\r'):None
         }
a = trans.translate(remap)
print(a)
import unicodedata
import sys
# 通过使用dict.fromkeys() 方法构造一个字典，每个Unicode 和音符作为键，对于的值全部为None 。然后使用unicodedata.normalize() 将原始输入标准化为分解形式字符。然后再调用translate 函数删除所有重音符。同样的技术也可以被用来删除其他类型的字符(比如控制字符等)。
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', trans)
b1 = b.translate(cmb_chrs)
print('---'*5)
print(b1)
#这里构造一个将所有Unicode数字字符映射到对应的ASCII字符上的表格
digitmap = {c: ord('o') + unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == 'Nd' }
print(len(digitmap))
print('----'*5)
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))
#另一种清理文本的技术涉及到I/O 解码与编码函数。这里的思路是先对文本做一些初步的清理，然后再结合encode()或者decode()操作来清除或修改它。
a1 = 'pýtĥöñ is awesome\n'
b = unicodedata.normalize('NFD', a1)
print(b)
#这里的标准化操作将原来的文本分解为单独的和音符。接下来的ASCII 编码/解码只是简单的一下子丢弃掉那些字符。当然，这种方法仅仅只在最后的目标就是获取到文本对应ACSII表示的时候生效
c = b.encode('ascii','ignore').decode('ascii')
print(c)
print('@'*20)
#字符串对齐操作，ljust(),rjust(),center()
text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
print(text.ljust(20,'='))
print(text.rjust(20,'-'))
print(text.center(20,'$'))
print('&&&'*10)
#format()函数也可以对齐字符串，但是要使用>,<,^.它可以用来格式化任何值，不仅仅适用于字符串
print(format(text,'>20'))
print(format(text,'<20'))
print(format(text,'^20'))
print(format(text,'=>20s'))
print(format(text,'*^20s'))
print(format(text,'=<20s'))
print('{:>10s} {:>10s}'.format('Hello','World'))
x = 1.2345
print(format(x,'>10'))
print(format(x,'^10.2f'))
print('%-20s' % text)#左对齐20个空字符
print('%20s' % text)#右对齐20个空字符
print('@@@'*10)
#合并拼接字符串
#要合并的字符串是在一个序列或者iterable中,那么最快的方式就是使用join()方法
parts = ['IS','Chicago','Not','Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))
a = 'Is Chicago'
b = 'Not Chicago?'
print(a+' '+b)
print('{} {}'.format(a,b))
print(a,b,sep=':')

data = ['ACME',50,91.1]
print(','.join(str(d) for d in data))
print(':'.join(str(data)))







