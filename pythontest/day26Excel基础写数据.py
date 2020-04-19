"""
excel基础写操作
"""

import xlsxwriter

# 1.创建一个excel文件并作为当前的工作簿
workbook = xlsxwriter.Workbook('res/excel_demo.xlsx')
# 2.添加一个工作表，默认名称是Sheet1,可以指定名称
# 默认名称 Sheet1
worksheet1 = workbook.add_worksheet()
# 指定名称 Data
worksheet2 = workbook.add_worksheet('Data')
# 3.写数据
# 向worksheet1 指定单元格写入内容
worksheet1.write('A1', 'Hello world')
# 向worksheet2写入一组数据并用公式求和
expenses = (
    ['Rent', 1000],
    ['Gas', 100],
    ['Food', 300],
    ['Gym', 50]
)
# 行和列的索引初值为0
row = 0
col = 0
# 遍历数据并逐行写入
for item, cost in (expenses):
    worksheet2.write(row, col, item)
    worksheet2.write(row, col+1, cost)
    row += 1

# 写一个公式，计算出总和
worksheet2.write(row, 0, 'Total')
worksheet2.write(row, 1, '=SUM(B1:B4)')

workbook.close()
