import json
import logging
import pickle
import signal
from threading import Timer

import spider
from box import Box

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

box = None
config: dict = {}


def init():
    global config
    with open('config.json', 'r') as c:
        config = json.load(c)

    global box
    try:
        with open(config['box_path'], 'rb') as f:
            box = pickle.load(f)
        logging.info('Loaded {} articles from file.'.format(box.size()))
        if box.version != config['version']:
            logging.warning('Box version is {} while feed version is {}'.format(box.version, config['version']))
    except:
        box = Box(config)
        logging.info('New box built.')

    box.rss_file(config['rss_path'])


def save():
    logging.info('Saving...')
    with open(config['box_path'], 'wb') as f:
        pickle.dump(box, f)
    logging.info('Saved.')


def my_exit(signum, frame):
    save()
    exit()


def worker():
    for article in spider.get_articles(config):
        box.article(article)
    box.rss_file(config['rss_path'])


if __name__ == '__main__':
    signal.signal(signal.SIGINT, my_exit)
    signal.signal(signal.SIGTERM, my_exit)

    init()

    i = 0
    while True:
        i += 1
        logging.info('[ {} ] will start in {} seconds'.format(i, config['time_interval'] if i != 1 else 0.0))
        time_interval = float(config['time_interval']) if i != 1 else 0.0
        timer = Timer(time_interval, worker)
        timer.start()
        timer.join()
        logging.info('[ {} ] Done.'.format(i))
