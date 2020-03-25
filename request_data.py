import requests
import brotli


url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&gp=2&page={0}&s=61&click=0"

payload = {}

headers = {
    'Host': 'search.jd.com',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Sec-Fetch-Dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Referer': 'https://global.jd.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': '__jdu=1582511349895283952680; shshshfpa=2275344e-9b3e-d611-ff7d-d938c13455f1-1582511352; shshshfpb=bsaekshi7R0sDfQJr78w94g%3D%3D; xtest=870.cf6b6759; qrsc=3; __jdv=76161171|direct|-|none|-|1584445256825; areaId=12; ipLoc-djd=12-933-3407-0; PCSYCityID=CN_320000_321300_321302; __jdc=122270672; rkv=V0700; 3AB9D23F7A4B3C9B=KKMMNIZ7CIYWN6WEIINIOWRIJBK5AWDSJ7PATYYPHDIHHFZWQ3NFR7UM7GUHEX5VCYGGGXXVLUOV3QPKG6UHACBGSY; _fbp=fb.1.1584788221632.1960364063; shshshfp=4958f712d02fdabba08effcda8d5881a; __jda=122270672.1582511349895283952680.1582511350.1584800769.1584864374.8; __jdb=122270672.1.1582511349895283952680|8.1584864374'
}


def get_data(page=0) -> str:
    realURL = url.format(page)
    response = requests.get(realURL, headers=headers, data=payload)
    return brotli.decompress(response.content).decode('utf-8')


if __name__ == "__main__":
    body = get_data()
    print(body)