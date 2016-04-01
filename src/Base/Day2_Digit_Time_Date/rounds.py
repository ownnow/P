#coding:utf-8
print(round(1.231,1))
print(round(-5.683,1))
#传给round() 函数的ndigits 参数可以是负数，这种情况下，舍入运算会作用在十位、百位、千位等上面
a = 1627731
print(round(a,-1))
print(round(a,-2))
print(round(a,-3))
print(4.1+2.3)
from decimal import Decimal, localcontext
a = Decimal('4.1')
b = Decimal('2.3')
print(a+b)
print(a / b)
with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)
with localcontext() as ctx:
    ctx.prec = 50
    print(a/b)
print('-'*20)
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
#为了将bytes 解析为整数，使用int.from_bytes() 方法
print(len(data))
print(int.from_bytes(data,'little'))
print(int.from_bytes(data,'big'))
#为了将一个大整数转换为一个字节字符串，使用int.to_bytes()方法
x = 94522842520747284487117727783387188
#字节顺序规则(little 或big) 仅仅指定了构建整数时的字节的低位高位排列方式
print(x.to_bytes(16,'big'))
print(x.to_bytes(16,'little'))
print('*'*10)
#如果你试着将一个整数打包为字节字符串，那么它就不合适了，你会得到一个错误。如果需要的话，你可以使用int.bit length() 方法来决定需要多少字节位来存储这个值
y = 523 ** 239
print(y)
#print(y.to_bytes(16,'little'))
print(y.bit_length())
nbytes,rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1
print(x.to_bytes(nbytes,'little'))