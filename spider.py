import logging
import re
import traceback
from datetime import datetime
from typing import List

from lxml import etree

from article import Article
from get_html_text import get_html_text


def get_date(config: dict, link: str) -> datetime:
    ret = datetime.now()
    if config['auto_datetime']:
        return ret

    try:
        raw = str(etree.HTML(get_html_text(link))
                  .xpath(config['datetime']['xpath'])[config['datetime']['index']])
        date_str = re.search(config['datetime']['re'], raw)[0]
        ret = datetime.strptime(date_str, config['datetime']['fmt'])
    except:
        logging.error("Error getting date of {}".format(link))
    finally:
        return ret


def get_articles(config: dict) -> List[Article]:
    url = config['url']
    articles = []
    try:
        tree = etree.HTML(get_html_text(url))

        for xpath in config['xpath']:
            nodes = tree.xpath(xpath['a'])
            articles += list(
                map(lambda a: Article(str(a.xpath(xpath['title'])[xpath['title_index']]),
                                      config['base_url'] + a.xpath(xpath['href'])[xpath['href_index']],
                                      get_date(config,
                                               config['base_url'] + a.xpath(xpath['href'])[xpath['href_index']]),
                                      config['content']),
                    nodes))
    except:
        traceback.print_exc()
        logging.error('Failed to get articles')

    if config['max_count'] <= 0:
        return articles
    else:
        return articles[:config['max_count']]
