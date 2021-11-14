from utils.MyUtils import MyUtils

# print(str(dir(MyUtils)))


class BaiduData(MyUtils):
    def __init__(self, url, webname, username, password) -> None:
        super().__init__(url, webname)
        self.username = username
        self.password = password
        
        
baiduData = BaiduData("url", "webname", "username", "password")

baiduData.login()
