a = complex(2,4)
b = 3 - 5j
import cmath
print(cmath.sin(a))#正玄
print(cmath.cos(a))#反玄
print(cmath.tan(a))#正切
print(cmath.exp(a))#平方根
print('--'*10)
#使用numpy ，可以很容易的构造一个复数数组并在这个数组上执行各种操作：
import numpy as np
a1 = np.array([2+3j,4+5j,6-7j,8+9j])
print(a1)
print(a1+2)
print(np.sin(a1))
print(cmath.sqrt(-1))
#fractions 模块可以被用来执行包含分数的数学运算
from fractions import Fraction
frac = Fraction(5,4)
frac1 = Fraction(7,16)
print(frac + frac1)
print(frac * frac1)
print(float(frac*frac1))
import numpy as np
ax = np.array([1,2,3,4])
print (ax*2)
ay = np.array([5,6,7,8])
print (ay*2)
print (ax + 10)
print (ax + ay)
print (ax * ay)
def f(x):
    return 3*x**2 - 2*x +7
print (f(ax))

import random
values= [1,2,3,4,5,6]
print (random.choice(values))#随机提取一个
print (random.sample(values,3))#随机提取3个
random.shuffle(values)
print (values)
print (random.randint(0,10))#生成随机数
print (random.random())#生成0到1之间均匀分布的浮点数
print (random.getrandbits(20))#获取N位随机（二进制）的整数