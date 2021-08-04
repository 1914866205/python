import sys,io
import requests
from lxml import etree

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8') #改变标准输出的默认编码

response = requests.get("https://www.jd.com/").text
#print(response)
documnet = etree.HTML(response)
query_result = open("query_keywords.csv","w")
for i in range(1,19):
    keywords = documnet.xpath('//*[@id="J_cate"]/ul/li['+str(i)+']/a/text()')
    #print(keywords)
    for element in keywords:
        print(element)
        query_result.write(str(element)+'\n')

query_result.close()

