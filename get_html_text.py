import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) \
    AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15'
}


def get_html_text(url, timeout=3, times=5):
    i = 0
    while i < times:
        try:
            request = requests.get(url, timeout=timeout)
            text = request.text
            request.close()
            return text
        except requests.exceptions.RequestException:
            i += 1

    return None
