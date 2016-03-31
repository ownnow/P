#coding:utf-8
#format()和format_map()相比较那些方案而已更加先进，因此应该被优先选择。使用format()方法还有一个好处就是你可以获得对字符串格式化的所有支持(对齐，填充，数字格式化等待)，而这些特性是使用像模板字符串之类的方案不可能获得的。
s = '{name} has {n} messages.'
print(s.format(name='Guido',n=37))
name = 'Guido'
n =37
#如果要被替换的变量能在变量域中找到，那么你可以结合使用format map()和vars().vars()还有一个特性就是也适用于对象实例
print(s.format_map(vars()))
class Info:
    def __init__(self,name,n):
        self.name = name
        self.n = n
a = Info('Ownnow',26)
print(s.format_map(vars(a)))
#format,format_map并不能很好的处理变量缺失的情况，这是一个缺陷
# s.format(name='ownnow')  tips:KeyError:'n'。为了弥补这个缺陷，另外定义含有__missing__()方法的字典对象
class safesub(dict):
    '''防止 key 找不到'''
    def __missing__(self,key):
        return '{' + key + '}'
#可以利用这个类包装输入后传递给format_map()
del n 
print(s.format_map(safesub(vars())))
#如果你发现自己在代码中频繁的执行这些步骤，你可以将变量替换步骤用一个工具函数封装起来
import sys 
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))
names = 'OWNNOW'
n1 = 24
print(sub('HELLO {names}'))
print(sub('YOU HAVE {n1} MESSAGES.'))
print(sub('Your favorite color is {color}'))
#导入string模块，使用Template()   
import string
s = string.Template('$name has $n1 messages.')
print(s.substitute(vars()))
print('****'*5) 
#指定列宽来格式化长字符串,使用textwrap模块来格式化字符串输出
#你可以使用os.get_terminal_size() 方法来获取终端的大小尺寸.可以使用os.get_terminal_size().columns
s1 = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
import textwrap
print(textwrap.fill(s1, 70))
print(textwrap.fill(s1, 40))
print(textwrap.fill(s1, 40,initial_indent='        '))
print(textwrap.fill(s1, 40,subsequent_indent='          '))
#在字符串中处理html和xml，例如替换文本字符串中的‘<’,'>'使用html.escape()函数可以很容易的完成
#在生成HTML或者XML文本的时候，如果正确的转换特殊标记字符是一个很容易被忽视的细节。特别是当你使用print() 函数或者其他字符串格式化来产生输出的时候。使用像html.escape() 的工具函数可以很容易的解决这类问题。如果你想以其他方式处理文本， 还有一些其他的工具函数比如xml.sax.saxutils.unescapge() 可以帮助你。然而，你应该先调研清楚怎样使用一个合适的解析器。比如，如果你在处理HTML 或XML 文本，使用某个解析模块比如html.parse 或xml.etree.ElementTree 已经帮你自动处理了相关的替换细节
text = 'Elements are written as "<tag>text</tag>".'
import html
print(text)
print(html.escape(text))
print(html.escape(text, quote=False))
s2 = 'Spicy Jalapeño'
print(s2.encode(encoding='ascii', errors='xmlcharrefreplace'))
s3 = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
print(p.unescape(s3))
t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))
print('@'*30)























