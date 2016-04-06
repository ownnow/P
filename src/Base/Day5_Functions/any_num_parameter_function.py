#coding:utf-8
#构造可接受任意数量参数的函数
#让一个函数接受任意数量的位置参数，可以使用一个*参数
def avg(first,*rest):
    return (first+sum(rest))/(1+len(rest))
print(avg(1,2))
print(avg(1,2,3,4))
#让一个函数接受任意的关键字参数，可以使用一个以**开头的参数
import html
def make_element(name,value,**attrs):
    keyvals = ['%s = "%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(name = name,attrs = attr_str,value=html.escape(value))
    return element
print(make_element('item', 'Albatross',size='large',quantity=6))
def mininum(*values,clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m 
    return m 
print(mininum(1,5,2,-5,10))
print(mininum(1,5,2,-5,10,clip = 0))