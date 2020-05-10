"""
时间处理
"""
from datetime import date, datetime, time, timedelta
import re


def date_time_demo():
    today = date.today()
    print(today)
    str_date = date.strftime(today, '%Y-%m-%d')
    print(str_date)
    str_to_date = datetime.strptime('2020-05-10', '%Y-%m-%d')
    print(str_to_date)
    now = datetime.now()
    str_time = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    print(str_time)
    str_to_time = datetime.strptime('2020-02-22 15:12:33', '%Y-%m-%d %H:%M:%S')
    print(str_to_time)


# 生日还有多久
def get_days_friend(birthday):
    # 正则分割生日字符串
    splits = re.split(r'[-.\s+/]', birthday)
    # 去掉空格字符
    splits = [s for s in splits if s]
    if len(splits) < 3:
        raise ValueError('输入格式不正确，至少包括年月日')
    # 切片 截取年月日
    splits = splits[:3]
    # 得到birthday的完整信息如： 2020-08-10 00:00:00
    birthday = datetime.strptime('-'.join(splits), '%Y-%m-%d')
    today = date.today()
    # 计算差值
    delta = birthday.date()-today
    return delta.days


if __name__ == '__main__':
    date_time_demo()
    print('我的生日还有', get_days_friend('2020-05-27'), '天')
