import requests
import json


class King:
    def __init__(self, word) -> None:
        # url
        # 对这个地址发送 post 请求
        self.url = 'http://localhost:3000'
        # 伪装
        self.headers = {
            # 伪造请求头
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
        }
        # data 字典
        self.data = {
            "name": word,  
        }

    # 发送请求获取响应
    def get_data(self):
        response = requests.post(
            self.url, json=self.data, headers=self.headers)
            
        return response.content.decode() 

    def parse_data(self, data):
        # loads 将 json 字符串转成 py 字典
        print(type(data))
        print(data)

    def run(self):
        # 数据解析
        response = self.get_data()

        self.parse_data(response)


if __name__ == '__main__':
    king = King("franck-lynn")
    king.run()
