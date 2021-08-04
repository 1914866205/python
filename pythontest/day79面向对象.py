# 使用class语句创建一个新类,class之后为类的名称并以冒号结尾
class Employee:
    '所有员工的基类'
    empCount = 0
   # 左右两条下划线
    def __init__(self,name,salary):  #构造方法
        self.name=name                #self代表类的实例，在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数
        self.salary=salary
        Employee.empCount += 1

    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print ("Name :",self.name,",Salary:",self.salary)

emp=Employee("涛涛",2000)
emp.displayCount()
emp.displayEmployee()

# SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hello,world!")
# Python3中取消了以前Python 2中的语法，两者在打印输出的语法上有所差别，
# 所以在Python 3下面使用之前的语法格式就会报错，错误信息已经提示你需要加上括号，字符串可以用单引号或双引号括起来。