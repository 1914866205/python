"""
爬取实验楼所有的课程信息
学习xpath和tree结合获取结点信息
可以按关键字统计一些数据，比如Java,C课程的数量
按照 pip3 install lxml
"""
import requests
from lxml import html


def crawl():
    course_list = []
    for num in range(1, 25):
        url = 'https://www.shiyanlou.com/courses/?page=' + str(num)
        content = requests.get(url)
        tree = html.fromstring(content.text)
        course_names = tree.xpath('//h6[@class="course-name"]/text()')
        course_descriptions = tree.xpath(
            '//div[@class="course-description"]/text()')
        course_covers = tree.xpath('//img[@class="cover-image"]/@src')
        for index in range(0, len(course_names)-1):
            temp_dict = {}
            temp_dict['name'] = course_names[index].strip()
            temp_dict['description'] = course_descriptions[index].strip()
            temp_dict['cover'] = course_covers[index]
            course_list.append(temp_dict)
    return course_list


if __name__ == '__main__':
    list = crawl()
    print(len(list))
