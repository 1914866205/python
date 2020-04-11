"""
爬取知乎一个专栏的所有粉丝数据并存入数据库
"""
import requests
import json
import pymysql
import time


def crawl():
    followers_data = []
    for offset in range(2500, 3000, 20):
        time.sleep(1)
        url = "https://www.zhihu.com/api/v4/columns/powertrain/followers?include=data%5B*%5D.follower_count%2Cgender%2Cis_followed%2Cis_following&offset=" + \
            str(offset)+"&limit=20"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64;x64)"
            "AppleWebKit/537.36 (KHTML,like Gecko) Chrome/79.0.3945.130 Stfari/537.36"
        }
        response = requests.get(url, headers=headers)
        followers_data += response.json().get("data")
    return followers_data


def data_insert(followers_data):
    # 打开数据库连接
    db = pymysql.connect("localhost", "ntt", ".15252205596xin", "db_python")
    # 使用cursor()方块创建一个游标对象 cursor
    cursor = db.cursor()
    val = []
    for dic in followers_data:
        item = (dic['id'], dic['name'], dic['url'], dic['gender'],
                dic['avatar_url'], dic['follower_count'])
        val.append(item)
    sql = "INSERT INTO t_follower (id,name,url,gender,avatar_url,follower_count) VALUES(%s,%s,%s,%s,%s,%s)"
    try:
        # 执行sql语句，批量插入
        cursor.executemany(sql, val)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()


if __name__ == '__main__':
    list = crawl()
    print(list)
    data_insert(list)
