from PySide2.QtCore import QFile
from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QTableWidgetItem

import requests
from requests.sessions import Request


class HttpClient:
    def __init__(self) -> None:
        # 从文件中加载UI定义
        qfile = QFile('./httpclient.ui')
        qfile.open(QFile.ReadOnly)
        qfile.close()
        # 从ui定义中动态创建一个相应的窗口对象
        self.ui = QUiLoader().load(qfile)
        # 给 boxMethod 添加选型 GET, POST, PUT, DELETE
        self.ui.comboBox.addItems(['GET', 'POST', 'PUT', 'DETELE'])
        # 信号处理
        self.ui.buttonSend.clicked.connect(self.sendRequest)
        # 设置文本框的内容 QLineEdit 控件
        self.ui.editUrl.setText('http://localhost:3000')
        # self.ui.editUrl.setText('https://api.github.com/users/defunkt') # 设置文本框的内容 QLineEdit 控件

        row = self.ui.headersTable.rowCount()
        self.ui.headersTable.insertRow(row)
        newItem = QTableWidgetItem("Accept")
        self.ui.headersTable.setItem(row, 0, newItem)
        newItem = QTableWidgetItem("application/json")
        self.ui.headersTable.setItem(row, 1, newItem)

        self.ui.buttonAddHeader.clicked.connect(self.addOneHeader)
        self.ui.buttonDelHeader.clicked.connect(self.delOneHeader)

    def addOneHeader(self):
        addRowNumber = self.ui.headersTable.currentRow() + 1
        self.ui.headersTable.insertRow(addRowNumber)

    def delOneHeader(self):
        self.ui.headersTable.removeRow(self.ui.headersTable.currentRow())

    def sendRequest(self):
        method = self.ui.comboBox.currentText()  # 下拉列表 QComboBox 控件

        url = self.ui.editUrl.text()  # 返回文本框的内容 QLineEdit 控件

        # 获取消息头
        headers = {}
        ht = self.ui.headersTable
        for row in range(ht.rowCount()):
            k = ht.item(row, 0).text()
            v = ht.item(row, 1).text()
            if k.strip() == '':
                continue
            headers[k] = v
        
        # ! post 请求时设置请求体
        payload = self.ui.editBody.toPlainText()  # 消息体中的内容 QListView 控件
        
        r = requests.get(url, headers=headers)
        # print(r.content.decode())
        # ! 组装请求(请求体和消息体), 如何组装请求?
        # req = Request(method, url, headers, payload)
        # prepared = req.prepare()
        
        # ! 将请求按照格式打印出来
        # self.pretty_print_request(r)
        # s = requests.Session()
        # r = s.send(prepared)
        
        # ! 把响应按照格式打印出来
        self.pretty_print_response(r.content.decode())

    def pretty_print_request(self, req):
        if(req.body == None):
            msgBody = ''
        else:
            msgBody = req.body
        self.ui.outputWindow.append(
            '{}\n{}\n{}\n\n{}'.format(
                '\n\n----------------发送请求-----------------------',
                req.method + ' ' + req.url,
                '\n'.join('{}: {}'.format(k, v)
                          for k, v in req.headers.items()),
                msgBody
            )
        )

    def pretty_print_response(self, res):
        self.ui.outputWindow.insertPlainText(
            res
            # '{}\nHTTP/1.1 {}\n{}\n\n{}'.format(
            #     '\n\n----------------得到响应-----------------------',
            #     res.status.code,
            #     '\n'.join('\n{}: {}'.format(k, v)
            #               for k, v in res.headers.items()),
            #     res.text
            # )
        )


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('favicon.ico'))
    httpClient = HttpClient()
    httpClient.ui.show()
    app.exec_()
