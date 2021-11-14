import requests

url = 'https://www.baidu.com'
# my_header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
# }


# response = requests.get(url, my_header)
response = requests.get(url)
# print("自动推测的编码格式---> ", response.encoding)
# # 手动设置编码格式
# response.encoding = 'utf8'
# print("按照utf-8编码进行解码: ", response.text)
# # 自动推测的编码格式
# print(response.content.decode())

# !常用响应对象
# print("响应的 url: ",response.url)
# print("响应的 状态码: ",response.status_code)
# print("响应 对应的 请求头: ",response.request.headers)
print("响应 对应的 响应头: ",response.headers)

print("响应cookie对象: ", response.cookies)