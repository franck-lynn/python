import requests
# 读取环境变量文件


url = 'https://gitee.com/'

my_header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    # "cookie": "user_locale=zh-CN; oschina_new_user=false; remote_way=http; tz=Asia%2FShanghai; Hm_lvt_24f17767262929947cc3631f99bfd274=1634479673,1634542513; gitee_user=true; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%228948434%22%2C%22first_id%22%3A%2217c8e9486bf18c-07610fa29fbeb2-b7a1438-2073600-17c8e9486c0ac7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217c8e9486bf18c-07610fa29fbeb2-b7a1438-2073600-17c8e9486c0ac7%22%7D; Hm_lpvt_24f17767262929947cc3631f99bfd274=1634542588; gitee-session-n=T0dRLzNOQ2dVZmpJSE5ISjdxbEFtcjJaQUNJdk81dnJja0l0M1c0UGFlQjhIME12NzVFVVhNMkNiSndCdExwWSsvMEhxNzljbjE4alJNTU5mQ0g0Z3l1NzFveW52bUdNRWJzdGlHVWxTOGFjeVlKY2I0TWdkaGVXYTRPaEFuWEpLR2twblk3eDgvQ3ZPRUhQei8xcHdSTVkwYnlEL0FNNG1Ia1JkeVRaM05kL09xcTdTS2FTdTQ3VXNWdUJIYkUyaGd2RzAzSnhkcEx5ekJNZk5oWEJuY0YxNU5kTE9yQS9FR0xXV1FEMTlSQnJicnZZM29ab25GMDJIMHhGUCtKenBqMnZtQkFBU0xDYzBtSG9Vemw5S2oyUFdDakVhZnZSQU1SaGdReDBmZkx0eTlHQkozSDBqY3dIWjEzUVcrazZjT2kvdXRIbG02bVo2Y1VkS3RvTGNIOVBpcVpkNWxpRVBkWDQ1VnNad05zPS0taTFuK0JUZ3h4bTZYdG9qODFuVE1iQT09--505428829491499b437653bcac2c077bd387460f"
}

r = requests.get(url,  headers=my_header)

# 验证是否登录成功
if my_header.has('cookie'):
    with open('github_with_cookies_.html', 'wb') as f:
        f.write(r.content)
else:
    with open('github_without_cookies_.html', 'wb') as f:
        f.write(r.content)





