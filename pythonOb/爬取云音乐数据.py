"""
爬取知乎一个专栏的所有粉丝数据并存入数据库
"""
import requests
import json
import pymysql
import time


def crawl(a):
    try:
        music_data = []
        url = "https://music.163.com/api/playlist/detail?id=" + str(a)
        print(url)
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64;x64)"
            "AppleWebKit/537.36 (KHTML,like Gecko) Chrome/80.0.3987.163 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        music_data += response.json().get("result").get("tracks")
    except:
        return ""
    return music_data


# def data_insert(music_data):
def data_insert():
    # 打开数据库连接
    db = pymysql.connect("localhost", "ntt", ".15252205596xin", "db_python")
    # for i in range(157009499, 13109499, -3):
    for i in range(156971702, 13109499, -3):
        # 使用cursor()方块创建一个游标对象 cursor

        cursor = db.cursor()
        val = []
        try:
            for dic in crawl(i):
                item = (dic['id'], dic['name'], dic['copyrightId'], dic['artists'][0].get(
                    'name'), dic['duration']/1000, dic['artists'][0].get('img1v1Url'))
        # print(dic['id'])
        # print(dic['name'])
        # print(dic['copyrightId'])
        # print(dic['artists'][0].get('name'))
        # print(dic['duration']/1000)
        # print(dic['artists'][0].get('img1v1Url'))
            # print(item)
                val.append(item)
                sql = "INSERT INTO song(song_id,song_name,sort_id,singer,duration,thumbnail) VALUES(%s,%s,%s,%s,%s,%s)"
                # 执行sql语句，批量插入
                cursor.executemany(sql, val)
                # 提交到数据库执行
                db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
        # finally:
    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    # list = crawl()
    data_insert()
