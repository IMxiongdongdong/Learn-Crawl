from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

url = 'http://www.ngchina.com.cn/photography/photo_of_the_day/'
html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')
img_ul = soup.find_all('ul', {'class': 'cf showImg-list'})
print(len(img_ul))

for ul in img_ul:
    #有好几个ul存放图片
    imgs = ul.find_all('img')
    #找到所有的img tag
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        img_name = url.split('/')[-1]
        #取最后一个作为名字
        with open('./img/%s' % img_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('save %s' % img_name)