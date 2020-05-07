"""
数学内置函数
""", 10
# 长度
dic = {'a': 1, 'b': 3}
print(len(dic))
a = [{'name': 'xiaoming', 'age': 18, 'gender': 'male'},
     {'name': 'xiaohong', 'age': 19, 'gender': 'female'}]
# 最大值
print(max(a, key=lambda x: x['age']))
# pow(x,y,z=Nome,/) x为底的y次幂,如果有z，取余
print(pow(3, 2, 4))
# 四舍五入,第二个参数代表小数点后保留几位
print(round(3.1415926535897962), 3)
a = [1, 5, 4, 3, 5]
# 求和
print(sum(a))
# 指定求和的初值为10
print(sum(a, 10))
# 求绝对值或负数的模
print(abs(-6))
# 分别取商和余数
print(divmod(10, 3))
# 定义复数
print(complex(1, 2))
