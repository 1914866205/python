"""
字符串高频操作
"""
# re 为正则表达式库
import re
# strip 用于去除字符串前后的空格
print(' I love what \t\n '.strip())
# replece 用于字符串的替换
print(' I love what \t\n '.replace(' ', '_'))
# join 用于合并字符串
print('_'.join(['book', 'store', 'count']))
# title 用于单词的首字母大写
print(' I love what \t\n '.title())
# find 用于返回匹配字符串的起始位置索引
print(' I love what \t\n '.find('python'))
