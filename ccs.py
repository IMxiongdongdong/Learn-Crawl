from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import urllib
import http.cookiejar

url = 'http://www.ccs.org.cn/ccswz/font/fontProductAction!productList.do?productType=272'
# html = urlopen(url).read().decode('utf-8')

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # "Accept-Encoding": "gzip, deflate",
    "Accept-Encoding": "gb2313,utf-8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Connection": "keep-alive",
    "referer": "http://www.ccs.org.cn/ccswz/font/fontProductAction!productList.do?productType=272"
}

cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
headall = []

for key, value in headers.items():
    item = (key, value)
    headall.append(item)
opener.addheaders = headall

urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, features='lxml')
all_tr = soup.find_all('tbody')
print(len(all_tr))

for tr in all_tr:
    tds = tr.find_all('td', {'align' : 'center'})
    for td in tds:
        td_str = td['align']
        td_name = td_str.split('&')[-2]
        with open('./test.txt', 'w') as f:
            f.write(td_name)
