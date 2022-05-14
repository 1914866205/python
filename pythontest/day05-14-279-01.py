import requests
from bs4 import BeautifulSoup

allUniv = []


# 获取指定网页的全部内容
def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""


def fillUnivList(soup):
    # 所有学校列表
    data = soup.find_all('tr')
    # 每个学校信息
    for tr in data:
        # 每个学校的属性列表
        ltd = tr.find_all('td')
        if len(ltd) == 0:
            continue
        singleUniv = []
        for td in ltd:
            # 清华大学 Tsinghua University 双一流 / 985 / 211
            # e = np.char.split('hello python, I love you', sep=',')  # 以逗号为分隔符
            # print(td.text.strip().replace('\n','').replace('\r',''))
            singleUniv.append(td.text.strip().replace('\n', '').replace('\r', ''))
        allUniv.append(singleUniv)


def printUnivList(num):
    print("{:^4}{:^100}{:^5}{:^8}{:^10}".format("排名", "学校名称", "省市", "总分", "办学层次"))
    result=sorted(allUniv, key=lambda item: item[2])
    for i in range(num):
        u = result[i]
        print("{:^4}{:^100}{:^5}{:^8}{:^10}\n".format(u[0], u[1], u[2], u[4], u[5]))


def main(num):
    url = 'https://www.shanghairanking.cn/rankings/bcur/2022'
    html = getHtmlText(url)
    soup = BeautifulSoup(html, "html.parser")
    fillUnivList(soup)
    printUnivList(num)
    print("==================")

main(30)
