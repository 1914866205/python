"""
excel格式化写操作
"""

from datetime import datetime
import xlsxwriter


def set_format():
    workbook = xlsxwriter.Workbook('res/Excel格式化.xlsx')
    worksheet = workbook.add_worksheet()
    # 基础格式
    fmt = workbook.add_format(
        {'font_name': u'微软雅黑', 'font_size': 10}
    )
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
    # 金额格式
    money_format = workbook.add_format({'num_format': '$#,##0'})
    # 日期格式
    date_format = workbook.add_format({'num_format': 'yyyy-mm-dd'})
    # 设置行高,从第0行开始，行高为20，格式为fmt
    worksheet.set_row(0, 20, fmt)
    # 设置列宽，从A列到C列，宽为20，格式为fmt
    worksheet.set_column('A:C', 20, fmt)
    # 用指定背景格式写入表头
    worksheet.write('A1', 'Item', bg_format)
    worksheet.write('B1', 'Date', bg_format)
    worksheet.write('C1', 'COST', bg_format)

    expenses = (
        ['Rent', '2020-01-13', 1000],
        ['Gas', '2020-01-14', 100],
        ['Food', '2020-01-15', 300],
        ['Gym', '2020-01-16', 50]
    )

    row = 1
    col = 0
    # 遍历数据，用不同的格式写入
    for item, date_str, cost in (expenses):
        date = datetime.strptime(date_str, "%Y-%m-%d")
        worksheet.write_string(row, col, item)
        worksheet.write_datetime(row, col + 1, date, date_format)
        worksheet.write_number(row, col+2, cost, money_format)
        row += 1

    worksheet.write(row, 1, 'Total')
    worksheet.write(row, 2, '=SUM(C2:C5)', money_format)
    workbook.close()


if __name__ == '__main__':
    set_format()
