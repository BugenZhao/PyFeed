import logging

from dateutil.tz import gettz
from feedgen.entry import FeedEntry
from feedgen.feed import FeedGenerator

from article import Article


class Box:
    def __init__(self, config=None):
        if config is None:
            config = {}
        self.fg = FeedGenerator()
        self.fg.title(config['title'] if 'title' in config else 'PyFeed')
        self.fg.description(config['description'] if 'description' in config else 'github.com/BugenZhao/PyFeed')
        self.fg.author({'name': 'Bugen Zhao', 'email': 'bugenzhao@sjtu.edu.cn'})
        self.fg.link(href=config['url'] if 'url' in config else 'github.com/BugenZhao/PyFeed')
        self.fg.language('zh-CN')

        self.dict = {}
        self.version = 'v0.3'

    def add_article(self, article: Article):
        fe = self.fg.add_entry()
        fe.id(article.link)
        fe.link(href=article.link)
        fe.title(article.title)
        fe.description(article.description)
        fe.pubDate(article.date.replace(tzinfo=gettz("Asia/Shanghai")))

        self.fg.updated()

    def update_article(self, article: Article):
        fe = FeedEntry()
        fe.id(article.link)
        fe.link(href=article.link)
        fe.title(article.title)
        fe.description(article.description)
        fe.pubDate(article.date.replace(tzinfo=gettz("Asia/Shanghai")))
        self.fg.entry(fe, replace=True)

        self.fg.updated()

    def article(self, article: Article):
        if article.link not in self.dict:
            logging.info('New article: ' + article.title)
            self.add_article(article)
            self.dict[article.link] = article
        elif article != self.dict[article.link]:
            logging.info('Update article: ' + article.title)
            self.update_article(article)
            self.dict[article.link] = article
        else:
            logging.info('Article already existed: ' + article.title)

    def rss_file(self, filename):
        self.fg.rss_file(filename, pretty=True)

    def size(self):
        return len(self.dict)
