import requests


def getRobotTXT(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def analyseTXT(url, text):
    s = text.split('User-agent:')
    for i in range(1, len(s)):
        sub = s[i].split('\r\n')
    string = '对于爬虫代理: {} ,以下网址不能访问：'.format(sub[0])
    print(string)

    for j in range(1, len(sub)):
        if sub[j][:9] == 'Disallow:':
            string = url + sub[j][10:]
    print(string)
url = 'https://www.baidu.com'
robots = '/robots.txt'
text = getRobotTXT(url + robots)
analyseTXT(url, text)

