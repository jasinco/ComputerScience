import json
import requests

cached_news = []


def fetcher():
    headers = {
        'referer': 'https://w3.tcivs.tc.edu.tw/',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    r= requests.post("https://w3.tcivs.tc.edu.tw/ischool/widget/site_news/news_query_json.php", headers=headers,data={
        "field": 'time',
        "order": 'DESC',
        "pageNum": '0',
        "maxRows": '15',
        "keyword": '',
        "uid": 'WID_20_2_afc1af1dcbfd4511204ea2694c796b494d477f47',
        "tf": '1',
        "auth_type": 'user',
        "use_cache": '1'
    })
    global cached_news
    parsing = r.json()
    cached_news = parsing[1:]


if __name__ == "__main__":
    fetcher()
    for i in cached_news:
        print(json.dumps(i, indent=4))
