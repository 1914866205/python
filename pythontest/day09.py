"""
列表排序
"""
list1 = ['orange', 'apple', 'zoo', 'bluebetty', 'banana', 'pear']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定的字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)


"""
列表切片
"""
fruits = ['apple', 'grape', 'peach', 'strawberry', 'pear']
fruits += ['pitaya', 'mango', 'waxberry']
# 列表切片
fruits2 = fruits[1:4]
# ['grape','peach','strawberry']
print(fruits2)
# 课堂通过完整切片操作直接复制过来
# ['opple','grape','peach','strowberry','pear','pitaya','mango','waxberry']
fruits3 = fruits[:]
print(fruits3)
# ['pitoya','mango']
fruits4 = fruits[-3:-1]
print(fruits4)
# 反向切换操作获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5)
