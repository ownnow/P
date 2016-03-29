#coding=utf:8
import re
#简单的使用str.replace()进行替换
text = 'yeah,but no,but yeah,but no,but yeah'
t = text.replace('yeah', 'OWN')
print(t)
#复杂的模式使用re模块中的sub()函数,反斜杠数字比如\3 指向前面模式的捕获组号
text1 = 'Today is 11/26/2012. PyCon starts 3/13/2003.'
t1 = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text1)
print(t1)
#对于更复杂的替换，可以传递一个替换回调函数来代替
from calendar import month_abbr
datepats = re.compile(r'(\d)+/(\d+)/(\d+)')
def change_date(m):
    mon_name = month_abbr(int(text1.group(1)))
    return '{} {} {}'.format(text1.group(2),mon_name,text1.group(3))
f = datepats.sub(change_date,text1)
print(f)