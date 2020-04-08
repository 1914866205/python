"""
类和对象
"""


from pyecharts import charts


class Student(object):
    # __init__是一个特殊方法，用于在创建对象是进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学呢%s.' % (self.name, course_name))

    # PEP 要求标识符的名字全用小写，多个单词用下划线连续
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看18岁以下才能看的电影.' % self.name)
        else:
            print('%s可以观看18岁以上可以看的电影.' % self.name)


def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('李华', 18)
    # 给对象发study消息
    stu1.study('今年高考英语又该我上场表演了')
    # 给对象发出watch_av消息
    stu1.watch_movie()
    stu2 = Student('小明', 12)
    stu2.study('今年又考不上初中了')
    stu2.watch_movie()


if __name__ == '__main__':
    main()


"""
使用oycharts绘制仪表盘
"""

# 仪表盘
gauge = charts.Gauge()
gauge.add('Python小例子', [('Python机器学习', 30),
                        ('Python基础', 70), ('Python正则', 90)])
gauge.render(path="./res/仪表盘.html")
print('ok')
