num1 = int(input("请输入一个数字"))
num2 = int(input("请再输入一个数字"))
greatest_common_divisor = 0

if num1 > num2:
    greatest_common_divisor = num2
else:
    greatest_common_divisor = num1
while (not (num2 % greatest_common_divisor == 0 and num1 % greatest_common_divisor == 0)):
    greatest_common_divisor = greatest_common_divisor - 1
print("{}和{}的最大公约数是：{}".format(num1, num2, greatest_common_divisor))

least_common_multiple = 0
if num1 > num2:
    least_common_multiple = num2
else:
    least_common_multiple = num1
while (not (least_common_multiple % num1 == 0 and least_common_multiple % num2 == 0)):
    least_common_multiple = least_common_multiple + 1
print("{}和{}的最小公倍数是：{}".format(num1, num2, least_common_multiple))
