import pickle
import signal
import spider
from threading import Timer

from box import Box

box: Box = Box()


def init():
    global box
    try:
        with open('box.p', 'rb') as f:
            box = pickle.load(f)
        print('Loaded {} articles from file.'.format(box.size()))
    except:
        box = Box()
        print('New box built.')


def save():
    print('Saving...')
    with open('box.p', 'wb') as f:
        pickle.dump(box, f)
    print('Saved.')


def my_exit(signum, frame):
    save()
    exit()


def worker():
    for article in spider.get_articles():
        box.article(article)
    box.rss_file('rss.xml')


if __name__ == '__main__':
    signal.signal(signal.SIGINT, my_exit)
    signal.signal(signal.SIGTERM, my_exit)

    init()

    i = 0
    while True:
        print(i)
        i += 1
        timer = Timer(3.0, worker)
        timer.start()
        timer.join()
