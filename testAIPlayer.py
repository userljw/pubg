#encoding=utf-8
"""
陪练
"""

import threading
from SockClient import SockClient
from STATIC_DATA import ADDR
import random


def onePlay(team_name):
    client = SockClient()
    client.connect(ADDR)
    send_str = str({'name': team_name})
    client.send(send_str)
    
    while True:
        recv_dic = client.recv(10240)
        # import time
        # time.sleep(0.05)
        if recv_dic["type"] == "info":
            move_str = str({"move": [{"id": team_name + "01", "movement": str(random.randint(1, 9))},
                                     {"id": team_name + "02", "movement": str(random.randint(1, 9))},
                                     {"id": team_name + "03", "movement": str(random.randint(1, 9))}]})
            client.send(move_str)



def test_main(num):
    for i in range(num):
        team_name="陪练"+str(i)
        print(team_name)
        t = threading.Thread(target=onePlay, args=(team_name,))
        t.setDaemon(True) #设置后台
        t.start()

