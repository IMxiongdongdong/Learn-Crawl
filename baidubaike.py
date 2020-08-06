from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

base_url = 'https://baike.baidu.com'
his = ['/item/%E8%9C%98%E8%9B%9B/8135707']
for i in range(10):
    url = base_url + his[-1]
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    print(soup.find('h1').get_text(), 'url:', base_url + his[-1])#找h1的tag
    sub_urls = soup.find_all('a', {'target':'_blank', 'href':re.compile('/item/(%.{2})+$')})
    #find_all找到所有的a，a里的target是这样，href是这样。右键检查源代码找出规律
    #规律是/item/后面是%加两个字符，$结束
    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        his.pop()