# PyFeed
A simple RSS feed implemented in Python, for Office of undergraduate affairs, SEIEE, SJTU.

##Feed on bugenzhao.com

You can get a existing feed for **Office of undergraduate affairs, SEIEE, SJTU** at:

> https://bugenzhao.com/rss.xml
>

Subscribe it with [NetNewsWire](https://ranchero.com/netnewswire/), a fully free RSS reader for macOS and iOS.

![截屏2020-01-17下午6.28.23](img/screenshot.png)

## Self Hosting

If you want to host your own feed, follow the instructions below:

1. Clone the repository and install requirements.

   ```bash
   git clone https://github.com/BugenZhao/PyFeed
   cd PyFeed
   pip3 install -r requirements.txt
   ```

2. Configure `config.json` like this:

   ```json
   {
     "version": "v0.2",
     "time_interval": 900,  // Time interval for update
     "box_path": "./box.p",
     "rss_path": "/root/homepage/public/rss.xml" // Path of the feed to generate
   }
   ```

3. Go for it.
   ```bash
   python3 ./main.py
   ```


