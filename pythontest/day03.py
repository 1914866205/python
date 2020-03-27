"""
输入一个正整数判断是不是素数
    提示：素数指的是只能被1和自身整除的大于1的整数
"""
from math import sqrt

num = int(input('请输入一个正整数：'))
end = int(sqrt(num))
is_prime = True
for x in range(2, end+1):
    if num % x == 0:
        is_prime = False
        break
    if is_prime and num != 1:
        print('%d是素数' % num)
    else:
        print('%不是素数' % num)

"""
输入两个正整数，计算它们的最大公约数和最小公倍数
"""
x = int(input('x='))
y = int(input('y='))
# 如果x大于y就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给 x，将x的值赋给y
    x, y = y, x
# 从两个数中较小的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x*y/factor))
        break

  # 打印三角形
row = int(input('请输入行数:'))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row-i-1):
        print(' ', end='')
    for _ in range(2*i+1):
        print('*', end='')
    print()
