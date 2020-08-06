from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

url = 'http://www.dili360.com/gallery/'
html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')

all_ul = soup.find_all('ul', {'class' : 'gallery-block-middle'})
print(len(all_ul))

for ul in all_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        ulr = img['src']
        r = requests.get(url, stream=True)
        img_name = url.split('/')[-1]
        with open('./img/%s' % img_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('save %s' % img_name)