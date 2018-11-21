#encoding=utf-8
"""
PUBG Client
1. Socket 连接
2. send 封装
3. recv 分装
4.Socket 释放
"""
import json
from socket import socket, AF_INET, SOCK_STREAM

class SockClient(socket):
    def __init__(self):
        super(SockClient, self).__init__(AF_INET,SOCK_STREAM)

    def send(self, data):
        head = "0000" + str(bytes(data, encoding="utf-8").__len__());
        head_format = head[head.__len__() - 4:head.__len__()]
        super().send(bytes(head_format,encoding="utf-8"))
        super().send(bytes(data,encoding="utf-8"))

    def recv(self, buffersize=10240):
        raw_data = super().recv(buffersize)
        if raw_data:
            try:
                re_str = str(raw_data, encoding="utf-8")[4:]
            except:
                re_str = str(raw_data, encoding="gbk")[4:]
            dictinfo = json.loads(re_str)
            return dictinfo



# if __name__ == '__main__':
#     ADDR = ('127.0.0.1', 8888)
#     teamName = "背锅侠4"
#     sc = SockClient()
#     sc.connect(ADDR)
#     sendStr = "{'name':'" + teamName + "'}"
#     sc.send(sendStr)
#     data1 = sc.recv()
#     print(data1["type"])
#     while True:
#         recvString = sc.recv()
#         print(recvString)
