import requests

url = 'https://movie.douban.com/j/search_subjects'
query_data = {
    "type": "movie",
    "tag": "热门",
    "page_limit": 50,
    "page_start": 0
}
# r = requests.get(url, params=query_data)
# # 反爬虫机制起作用了
# print(r.status_code)
# # {'User-Agent': 'python-requests/2.26.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
# print(r.request.headers)
my_header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

r = requests.get(url, params=query_data, headers=my_header)
# print(r.status_code)
print(r.json())