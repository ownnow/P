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
print(a + 6)