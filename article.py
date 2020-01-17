from goose3 import Goose
from goose3.text import StopWordsChinese

goose = Goose({'stopwords_class': StopWordsChinese})


class Article:
    def __init__(self, title: str = '', link: str = '', date: str = ''):
        self.title: str = title
        self.link: str = link
        self.date: str = date
        self.description: str = goose.extract(url=link).cleaned_text if len(link) > 1 else ''

    def __eq__(self, other):
        return self.title == other.title and \
               self.link == other.link and \
               self.date == other.date and \
               self.description == other.description
