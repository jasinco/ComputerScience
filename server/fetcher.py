import requests
from urllib.parse import unquote

cached_news = []
cached_news_content = {}
headers = {
    'referer': 'https://w3.tcivs.tc.edu.tw/',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}

def fetcher():
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

def content_fetcher(nid: str):
    if cached_news_content.get(nid) is not None:
        return
    r = requests.get("https://w3.tcivs.tc.edu.tw/ischool/widget/site_news/news_query_json_content.php", params={"nid": nid, "uid":"WID_20_2_afc1af1dcbfd4511204ea2694c796b494d477f47" }, headers=headers)
    temp = r.json()[0]
    temp["content"] = unquote(temp["content"])
    temp["content"] = temp["content"].replace("https://w3.tcivs.tc.edu.tw/ischool/resources/WID_20_2_afc1af1dcbfd4511204ea2694c796b494d477f47", "/api/outer_res")
    cached_news_content[nid] = temp

def content_static_files_fetcher(path:str) -> tuple:
    pth =  f"https://w3.tcivs.tc.edu.tw/ischool/resources/WID_20_2_afc1af1dcbfd4511204ea2694c796b494d477f47/{path}"
    r = requests.get(pth, headers={
        'referer': 'https://w3.tcivs.tc.edu.tw/',
    }, stream=True)
    return (r.headers.get("Content-Type"), r.raw)



if __name__ == "__main__":
    import json
    fetcher()
    for i in cached_news:
        print(json.dumps(i, indent=4))
    content_fetcher(cached_news[0]["newsId"])
    print(cached_news_content)
    # print(content_static_files_fetcher("NEWS_20_2_08e97d817b67be6dedc7b39c3a264c026668b464/c5dc6189424665eb110a082012361b33.jpg"))
