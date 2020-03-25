from bs4 import BeautifulSoup
from goods import Goods

def parse_data(body, goods):
    # 通过bs来解析body获取一个soup的对象
    soup = BeautifulSoup(body)

    # 查找所有的商品
    items = soup.find_all('li', class_="gl-item")

    # 遍历所有商品列表
    for item in items:
        try:
            # 查找到price_tag
            price_tag = item.find_all('div', class_='p-price')[0]

            price = price_tag.strong.i.get_text()
            title = price_tag.next_sibling.next_sibling.a.em.get_text()
            page = price_tag.next_sibling.next_sibling.a['href']
            # 添加获取到的商品
            goods.append(Goods(price, title, page))
        except Exception as e:
            pass