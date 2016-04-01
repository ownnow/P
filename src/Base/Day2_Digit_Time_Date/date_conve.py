#coding:utf-8
from datetime import timedelta, datetime,date
a = timedelta(days=2,hours=6)
b = timedelta(hours=4.5)
print(a+b)
c = a+b
print(c.days)
print(c.seconds)
a1 = datetime(2012,9,23)
print(a1+timedelta(days=10))
b1 = datetime(2012,12,21)
print(b1-a1)
now = datetime.today()
print(now)
print(now+timedelta(minutes=10))
print('***'*10)
# 查找星期中某一天最后出现的日期，比如星期五
weekdays = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
def get_previous_byday(dayname,start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target=weekdays.index(dayname)
    day_ago = (7+day_num - day_num_target)%7
    if day_ago == 0:
        day_ago = 7
    target_date = start_date - timedelta(days=day_ago)
    return target_date
print(datetime.today())
print(get_previous_byday('Mon'))
print(get_previous_byday('Fri'))
print('----'*20)
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
#执行大量的日期计算的话，你最好安装第三方包python-dateutil来代替
print(datetime.now())
print(datetime.now()+relativedelta(weekday=MO))#NEXT MO
print(datetime.now()+relativedelta(weekday=FR(-1)))#last fri
print('@@'*20)
#在当前月份中循环每一天在这样的日期上循环并需要事先构造一个包含所有日期的列表。你可以先计算出开始日期和结束日期，然后在你步进的时候使用datetime.timedelta 对象递增这个日期变量即可。下面是一个接受任意datetime 对象并返回一个由当前月份开始日和下个月开始日组成的元组对象
import calendar
def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _,days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date+timedelta(days=days_in_month)
    return(start_date,end_date)
a_day = timedelta(days=1)
first_day,last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day
#上面的代码先计算出一个对应月份第一天的日期。一个快速的方法就是使用date或datetime 对象的replace() 方法简单的将days 属性设置成1 即可。replace()方法一个好处就是它会创建和你开始传入对象类型相同的对象。所以，如果输入参数是一个date 实例，那么结果也是一个date 实例。同样的，如果输入是一个datetime实例，那么你得到的就是一个datetime 实例。然后，使用calendar.monthrange() 函数来找出该月的总天数。任何时候只要你想获得日历信息，那么calendar 模块就非常有用了。monthrange() 函数会返回包含星期和该月天数的元组.一旦该月的天数已知了，那么结束日期就可以通过在开始日期上面加上这个天数获得。有个需要注意的是结束日期并不包含在这个日期范围内(事实上它是下个月的开始日期)。这个和Python 的slice 与range 操作行为保持一致，同样也不包含结尾。为了在日期范围上循环，要使用到标准的数学和比较操作。比如，可以利用timedelta 实例来递增日期，小于号< 用来检查一个日期是否在结束日期之前。
print('---'*20)
#为日期迭代创建一个同内置的range()函数，可以使用一个生成器实现这个目标
def date_range(start,stop,step):
    while start<stop:
        yield start
        start += step
for d in date_range(datetime(2016,4,1), datetime(2016,5,1), timedelta(hours=6)):
    print(d)
    
print('----'*15)
#字符串转换为日期,使用datetime模块可以很容易解决
#datetime.strptime() 方法支持很多的格式化代码，比如%Y 代表4 位数年份， %m代表两位数月份。还有一点值得注意的是这些格式化占位符也可以反过来使用，将日期输出为指定的格式字符串形式。
text = '2016-03-11'
y = datetime.strptime(text,'%Y-%m-%d')
z = datetime.now()
print(y,'\n',z)
diff = z - y
print(diff)
print(datetime.strftime(z,'%A %B %d,%Y'))
#日期格式是YYYY-MM-DD ，你可以像下面这样实现一个解析函数,strptime()的性能要差很多
def parse_ymd(s):
    year_s,mon_s,day_s = s.split('/')
    return datetime(int(year_s),int(mon_s),int(day_s))
from pytz import timezone
loc_d = datetime.now()
print(loc_d)






