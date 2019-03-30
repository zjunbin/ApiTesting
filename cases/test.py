#  coding utf-8
# @time      :2019/3/2015:50
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :test.py

# a = None
# if a :
#     print('pass')
# else:
#     print('failed')
from decimal import Decimal

b = 1.5
c = 1.5
if Decimal(b) == Decimal(c):
    print('pass')
else:
    print('failed')

print(Decimal(b))
print(Decimal(c))