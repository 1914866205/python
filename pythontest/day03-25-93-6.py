import time
scale=10
print("{0:-^14}".format("执行开始"))
for i in range(scale+1):
    a,b='**' * i , '..' * (scale-i)
    print("Start[{}->{}]Down!".format(a,b))
    time.sleep(0.1)
print("{0:-^14}".format("执行结束"))