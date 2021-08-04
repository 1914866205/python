#coding=utf-8
# import mysql.connector
import pymysql
db = pymysql.connect("localhost", "root", "root", "wzry")

#
# # # 打开数据库连接
# db=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="root",
#     database='wzry',
# )

#获取操作游标
cursor=db.cursor()
#执行sql语句
cursor.execute("select VERSION()")
#获取一条数据
data=cursor.fetchone()
print("mysql版本：%s" % data)

# #插入新球员
# sql="INSERT INTO player (team_id,player_name,height) VALUES (%s,%s,%s)"
# val=(1003,"涛涛",2)
# cursor.execute(sql,val)
# db.commit()
# print(cursor.rowcount,"记录插入成功")
#查询身高大于等于2.08的球员
sql="select * from heros where hp_max>=6000"
cursor.execute(sql)
data=cursor.fetchall()
for each_player in data:
    print(each_player)

#关闭游标，数据库连接
cursor.close()
db.close()