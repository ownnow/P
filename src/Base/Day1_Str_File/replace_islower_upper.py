import re 
from _ast import Num
# 为了在文本操作时忽略大小写搜索与替换文本字符串，
# 在使用re 模块的时候给这些操作提供re.IGNORECASE标志参数,sub()可以接受一个回调函数
text = 'UPPER PYTHON,lower python,Mixed Python'
print(text)
f= re.findall('python', text, flags=re.IGNORECASE)
print(f)
f1=re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(f1)
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
f3 = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(f3)
print('*****'*10)
# 用正则表达式匹配某个文本模式，但是它找到的是模式的最长可能匹
# 配。而你想修改它变成查找最短的可能匹配
# 一般出现在需要匹配一对分隔符之间的文本的时候(比如引号包含的字符串)
str_pat = re.compile(r'\"(.*)\"')#匹配被""包含的内容,*是贪婪操作
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
#匹配被""包含的内容,*是贪婪操作,在其后面加上?，表示非贪婪
print(re.compile(r'\"(.*?)\"').findall(text2))
print('####'*10)
#匹配多行操作
text3 = '''/* this is a 
    multiline coomment */
    '''
# (?:.|\n) 指定了一个非捕获组,也就是它定义了一个仅仅用来做
# 匹配，而不能通过单独捕获或者编号的组
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text3))

#re.compile()函数接受一个标志参数叫re.DOTALL在这里非常有用
#它可以让正则表达式中的点(.)匹配包括换行符在内的任意字符
comm = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comm.findall(text3))

#在Unicode中某些字符能够用多个合法的编码表示
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1,'\n',s2)
print(s1 == s2)
print(len(s1),len(s2))
#unicodedata模块将文本标准化
import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1,t2)
print(t1 == t2,'\n',ascii(t1),ascii(t2))
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
print(ascii(t3),'\n',ascii(t4))

# normalize()第一个参数指定字符串标准化的方式。
#NFC表示字符应该是整体组成(比如可能的话就使用单一编码)
#而NFD表示字符应该分解为多个组合字符表示。
#Python同样支持扩展的标准化形式NFKC和NFKD，
#它们在处理某些字符的时候,增加了额外的兼容特性
print('@@@@@'*5)
s = '\ufb01'#单个字符串
print(s)
print(unicodedata.normalize('NFKC', s))
print(unicodedata.normalize('NFKD', s))
# 标准化对于任何需要以一致的方式处理Unicode文本的程序都是非常重要的
# 当处理来自用户输入的字符串而你很难去控制编码的时候尤其如此。
# 在清理和过滤文本的时候字符的标准化也是很重要的。
# 假设你想清除掉一些文本上面的变音符的时候(可能是为了搜索和匹配)
u1 = unicodedata.normalize('NFD', s1)
#combining()函数可以测试一个字符是否为和音字符。在这个模块中还有
#其他函数用于查找字符类别，测试是否为数字字符等等。
u2 = ''.join(c for c in u1 if not unicodedata.combining(c))
print(u2)
print('在正则式中使用Unicode')
num = re.compile('\d+')
print(num.match('123'))
print(num.match('\u0661\u0662\u0663'))

















