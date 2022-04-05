str = input("请输入一串字符")
num = 0
word = 0
char = 0
for item in str:
    i = ord(item)  # ASCII 字符转数字
    if ord('9') >= i >= ord('0'):
        num = num + 1
    elif (ord('a') <= i <= ord('z')) | (ord('A') <= i <= ord('Z')):
        word = word + 1
    else:
        char = char + 1

print("数字有{}个".format(num))
print("单词有{}个".format(word))
print("字符有{}个".format(char))
