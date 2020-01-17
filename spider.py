import re
from typing import List

from lxml import etree

from article import Article
from get_html_text import get_html_text

url = 'http://bjwb.seiee.sjtu.edu.cn'


def get_date(a) -> str:
    ret = ''
    try:
        raw = str(etree.HTML(get_html_text(url + a.xpath('@href')[0]))
                  .xpath('//*[@id="layout11"]/div/div[1]/div[2]/text()')[0])
        ret = re.search(r'\d{4}-\d{2}-\d{2}', raw)[0]
    except:
        print("Error getting date of", a.xpath('@href')[0])
    finally:
        return ret


def get_articles() -> List[Article]:
    articles = []
    try:
        tree = etree.HTML(get_html_text(url))

        top_a = tree.xpath('//*[@id="layout231"]/div/div[2]/div[2]/h4/a')[0]
        articles.append(Article(str(top_a.xpath('.//text()')[0]),
                                url + top_a.xpath('@href')[0],
                                get_date(top_a)
                                ))

        others = tree.xpath('//*[@id="layout231"]/div/div[2]/ul//li/a')
        articles += list(map(lambda a: Article(str(a.xpath('.//text()')[1]),
                                               url + a.xpath('@href')[0],
                                               get_date(a)),
                             others))
    except:
        print('Failed to get articles')

    return articles
