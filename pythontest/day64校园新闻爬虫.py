"""
校园新闻爬虫
"""
# 连接数据库出现RuntimeError:crytography is required for sha256_passw
# 解决方法：按照cryptography即可
# pip install cryptography
import requests
from bs4 import BeautifulSoup
import pymysql


def crawl():
    info_list = []
    for num in range(1, 3):
        url = 'http://news.niit.edu.cn/4000/list'+str(num)+'.htm'
        html = requests.get(url).content
        html_doc = str(html, 'utf-8')
        soup = BeautifulSoup(html_doc, 'html.parser')
        content_div = soup.find(
            'div', {'class': 'wp_articlecontent'})
        temp_dict['content'] = content_div.get_text()
        img_list = content_div.find_all('img')
        if len(img_list) >= 1:
            img_url = img_list[0]['src']
            temp_dict['cover'] = 'http://news.niit.edu.cn/'+img_url
        else:
            # 新闻没有图片，使用默认
            temp_dict['cover'] = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
        info_list.append(temp_dict)
    return info_list


def data_insert(info_list):
    db = pymysql.connect("localhost", "root", "root", "db_python")
    cursor = db.cursor()
    val = []
    for dic in info_list:
        item = (dic['cover'], dic['created'], dic['updated'], dic['is_deleted'],
                dic['is_top'], dic['content'], dic['title'])
        val.append(item)
    sql = "INSERT INFO info_manage(cover,created,updated,is_deleted,is_top,content,title)"
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
    print(len(list))
    data_insert(list)
