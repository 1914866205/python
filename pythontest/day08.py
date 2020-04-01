"""
列表元素的添加和删除
"""

list1 = [1, 3, 5, 7, 100]
list1.append(200)
list1.insert(1, 400)
print(list1)  # [1,400,3,5,7,100,200]

# 合并两个列表
list1.extend([1000, 2000])
print(list1)  # [1,400,3,5,7,100,200,1000,2000]
list1 += [100, 200]
print(list1)  # [1, 400, 3, 5, 7, 100, 200, 1000, 2000, 100, 200]
print(len(list1))  # 11
# 先通过成员运算符哦按段元素是否在列表中，如果存在就删除元素
if 100 in list1:
    list1.remove(100)
if 1234 in list1:
    list1.remove(1234)
print(list1)  # [1,400,3,5,7,200,1000,2000,100,200]
# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1)-1)
print(list1)  # [400,3,5,7,200,1000,2000,100]
# 清空列表元素
list1.clear()
print(list1)  # []

"""
列表的定义和遍历
"""
list1 = [1, 3, 5, 7, 100]
print(list1)  # [1,3,5,7,100]
list2 = ['hello']*3
print(list2)  # ['hello','hello','hello']
print(len(list1))  # 5
print(list1[0])  # 1
print(list1[4])  # 100
print(list1[-1])  # 100
print(list1[-3])  # 3     正着数，从0开始，倒着数，从-1开始
list1[2] = 300
print(list1)  # [1,3,300,7,100]
# 通过循环下标遍历
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历
for elem in list1:
    print(elem)
# 通过enumerate函数处理列表之后再遍历可以同时获得元素的索引和值
for index, elem in enumerate(list1):
    print(index, elem)
