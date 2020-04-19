"""
excel格式化写操作
"""

from datetime import datetime
import xlsxwriter
import wordcloud
import xlrd


def set_format():
    # 打开工作簿
    workbook_old = xlrd.open_workbook('res/班级卡片数据.xlsx')
    sheet1 = workbook_old.sheets()[0]

    # 获取第1列的内容
    list = [[], []]
    list[0] = sheet1.col_values(1)
    list[1] = sheet1.col_values(14)
    list[0].remove('姓名')
    list[1].remove('color')

    workbook = xlsxwriter.Workbook('res/班级卡片数据变色.xlsx')
    worksheet = workbook.add_worksheet()
    # 背景格式：定义字体，对齐方式，背景前景色等
    bg_format = workbook.add_format(
        {
            'bold': True,
            'font_name': u'微软雅黑',
            'bg_color': '#217346',
            'align': 'center',
            'valign': 'vcenter',
            'font_color': '#282c34',
            'font_size': 11,
            'border': 1
        }
    )
    # 基础格式
    fmt = workbook.add_format(
        {'font_name': u'微软雅黑', 'font_size': 10}
    )
    # 设置行高,从第0行开始，行高为20，格式为fmt
    worksheet.set_row(0, 20, fmt)
    # 设置列宽，从A列，宽为20，格式为fmt
    worksheet.set_column('A:A', 20, fmt)
    # 用指定背景格式写入表头
    worksheet.write('A1', '姓名', bg_format)

    row = 1
    col = 0
    # 遍历数据，用不同的格式写入
    for index in range(0, len(list[0])):
        worksheet.write_string(row, col, list[0][index], {
                               'bg_color': list[1][index]})
        row += 1

    workbook.close()


if __name__ == '__main__':
    set_format()
