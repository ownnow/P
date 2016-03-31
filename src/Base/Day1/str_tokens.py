#coding:utf-8
#字符串令牌解析
import re 
from collections import namedtuple
tokens = [('NAME','foo'),('EQ','='),('NUM','23'),('PLUS','+'),('NUM','42'),('TIMES','*'),('NUM','10')]
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
#?P<TOKENNAME> 用于给一个模式命名，供后面使用
master_pat = re.compile('|'.join([NAME,NUM,PLUS,TIMES,EQ,WS]))
#为了令牌化，使用模式对象很少被人知道的scanner()方法。这个方法会创建一个scanner对象，在这个对象上不断的调用match()方法会一步步的扫描目标文本，每步一个匹配
scanner = master_pat.scanner('foo = 42')
print(scanner.match())
def generate_tokens(pat,text):
    Token = namedtuple('Token',['type','value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match,None):
        yield Token(m.lastgroup,m.group())
for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)
print('#'*15)
tokens1 = (tok for tok in generate_tokens(master_pat,'foo = 42') if tok.type != 'WS')
for tok in tokens1:
    print(tok)
#通常来讲令牌化是很多高级文本解析与处理的第一步。为了使用上面的扫描方法，你需要记住这里一些重要的几点。第一点就是你必须确认你使用正则表达式指定了所有输入中可能出现的文本序列。如果有任何不可匹配的文本出现了，扫描就会直接停止。这也是为什么上面例子中必须指定空白字符令牌的原因。令牌的顺序也是有影响的。re 模块会按照指定好的顺序去做匹配。因此，如果一个模式恰好是另一个更长模式的子字符串，那么你需要确定长模式写在前面。