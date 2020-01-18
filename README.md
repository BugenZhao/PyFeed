# PyFeed
A simple RSS feed implemented in Python.

## Feed on bugenzhao.com

You can get a existing feed for **Office of Undergraduate Affairs, SEIEE, SJTU** at:

> https://bugenzhao.com/rss.xml

Subscribe it with [NetNewsWire](https://ranchero.com/netnewswire/), a fully free RSS reader for macOS and iOS.

![Screenshot](img/screenshot.png)

## Self Hosting

If you want to host your own feed, follow the instructions below:

1. Clone the repository and install requirements.

   ```bash
   git clone https://github.com/BugenZhao/PyFeed
   cd PyFeed
   pip3 install -r requirements.txt
   ```

2. Create a configuration file `config.json` like this:

   ```json
   {
     "version": "v0.3",
     "time_interval": 900,
     "box_path": "./box_bjwb.p",
     "rss_path": "/root/homepage/public/rss.xml",
     "url": "http://bjwb.seiee.sjtu.edu.cn",
     "base_url": "http://bjwb.seiee.sjtu.edu.cn",
     "title": "交大电院本科生教务办 RSS by Bugen",
     "description": "github.com/BugenZhao/PyFeed",
     "auto_datetime": false,
     "datetime": {
       "xpath": "//*[@id=\"layout11\"]/div/div[1]/div[2]/text()",
       "index": 0,
       "re": "\\d{4}-\\d{2}-\\d{2}",
       "fmt": "%Y-%m-%d"
     },
     "max_count": 0,
     "content": true,
     "xpath": [
       {
         "a": "//*[@id=\"layout231\"]/div/div[2]/div[2]/h4/a",
         "title": ".//text()",
         "title_index": 0,
         "href": "@href",
         "href_index": 0
       },
       {
         "a": "//*[@id=\"layout231\"]/div/div[2]/ul//li/a",
         "title": ".//text()",
         "title_index": 1,
         "href": "@href",
         "href_index": 0
       }
     ]
   }
   ```

   | Key            |                                      Description |
   | -------------- | -----------------------------------------------: |
   | time_interval  |                         Time interval for update |
   | box_path       |      Path for app to save and load current state |
   | rss_path       |                     Path of the feed to generate |
   | url            |                            Url of the index page |
   | base_url       |                          Url of the website root |
   | auto_datetime  | Whether to use current date time for new entries |
   | xpath          |                       XPath of specified element |
   | xpath -> a     |                               XPath of `<a></a>` |
   | xpath -> index |              Index of elements obtained by XPath |

3. Go for it!

   ```bash
   python3 ./main.py -c config.json
   ```


