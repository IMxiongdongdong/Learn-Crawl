import time
import multiprocessing as mp
import re
from urllib.request import urlopen,urljoin
from bs4 import BeautifulSoup

base_url='https://morvanzhou.github.io/'

def crawl(url):
    return urlopen(url).read().decode('utf-8')

def parse(html):
    soup=BeautifulSoup(html,features='lxml')
    urls=soup.find_all('a',{'href':re.compile('^/.+?/$')})
    title=soup.find('h1').get_text().strip()
    page_urls=set([urljoin(base_url,url['href']) for url in urls])
    url=soup.find('meta',{'property':'og:url'})['content']
    return title,page_urls,url

unseen=set([base_url,])
seen=set()

if __name__=='__main__':
    pool = mp.Pool(4)
    count, t1 = 1, time.time()

    while len(unseen) != 0:
        if len(seen) > 20:
            break

        print('\nDistributed crawling...')
        crawl_jobs = [pool.apply_async(crawl, args=(url,)) for url in unseen]
        htmls = [j.get() for j in crawl_jobs]

        print('\nDistributed parsing...')
        parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
        results = [j.get() for j in parse_jobs]

        print('Analysing...')
        seen.update(unseen)
        unseen.clear()

        for title, page_urls, url in results:
            print(count, title, url)
            count += 1
            unseen.update(page_urls - seen)
    print('Total time:%.1fs' % (time.time() - t1,))