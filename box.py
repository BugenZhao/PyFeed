from datetime import datetime
import logging

from dateutil.tz import gettz
from feedgen.entry import FeedEntry
from feedgen.feed import FeedGenerator

from article import Article

url = 'http://bjwb.seiee.sjtu.edu.cn'


class Box:
    def __init__(self):
        self.fg = FeedGenerator()
        self.fg.title('交大电院本科生教务办 RSS by Bugen')
        self.fg.description('github.com/BugenZhao/PyFeed')
        self.fg.author({'name': 'Bugen Zhao', 'email': 'bugenzhao@sjtu.edu.cn'})
        self.fg.link(href=url)
        self.fg.language('zh-CN')

        self.dict = {}

    def add_article(self, article: Article):
        fe = self.fg.add_entry()
        fe.id(article.link)
        fe.link(href=article.link)
        fe.title(article.title)
        fe.description(article.description)
        fe.pubDate(datetime.fromisoformat(article.date).replace(tzinfo=gettz("Asia/Shanghai")))

        self.fg.updated()

    def update_article(self, article: Article):
        fe = FeedEntry()
        fe.id(article.link)
        fe.link(href=article.link)
        fe.title(article.title)
        fe.description(article.description)
        fe.pubDate(datetime.fromisoformat(article.date).replace(tzinfo=gettz("Asia/Shanghai")))
        self.fg.entry(fe, replace=True)

        self.fg.updated()

    def article(self, article: Article):
        if article.link not in self.dict:
            print('New article:', article.title)
            self.add_article(article)
            self.dict[article.link] = article
        elif article != self.dict[article.link]:
            print('Update article:', article.title)
            self.update_article(article)
            self.dict[article.link] = article
        else:
            print('Article already existed:', article.title)

    def rss_file(self, filename):
        self.fg.rss_file(filename, pretty=True)

    def size(self):
        return len(self.dict)
