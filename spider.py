import logging
import re
import traceback
from datetime import datetime
from typing import List

from lxml import etree

from article import Article
from get_html_text import get_html_text


def get_date(config: dict, a) -> datetime:
    url = config['url']
    ret = datetime.now()
    if config['auto_datetime']:
        return ret

    try:
        raw = str(etree.HTML(get_html_text(url + a.xpath('@href')[0]))
                  .xpath('//*[@id="layout11"]/div/div[1]/div[2]/text()')[0])
        ret = re.search(r'\d{4}-\d{2}-\d{2}', raw)[0]
    except:
        logging.error("Error getting date of", a.xpath('@href')[0])
    finally:
        return ret


def get_articles(config: dict) -> List[Article]:
    url = config['url']
    articles = []
    try:
        tree = etree.HTML(get_html_text(url))

        nodes = tree.xpath(config['xpath']['a'])
        todo = nodes if config['max_count'] == 0 else nodes[:config['max_count']]
        articles += list(map(lambda a: Article(str(a.xpath(config['xpath']['title'])[config['xpath']['title_index']]),
                                               config['base_url'] + a.xpath(config['xpath']['href'])[
                                                   config['xpath']['href_index']],
                                               get_date(config, a),
                                               config['content']),
                             todo))
    except:
        traceback.print_exc()
        logging.error('Failed to get articles')

    return articles
