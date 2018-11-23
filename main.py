# encoding=utf-8

from SockClient import SockClient
import logging
from STATIC_DATA import ADDR, TEAM_NAME
from AI import algorithm
from Tools import get_treasure_map

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')


def login():
    client = SockClient()
    client.connect(ADDR)
    send_str = str({'name': TEAM_NAME})
    client.send(send_str)
    recv_data = client.recv()
    if 'login' == recv_data["type"]:
        logging.info("登陆成功")
    else:
        logging.error("无法登陆服务器")
    return client


def mainloop(client):
    is_first_flag = True
    turn=1
    while True:
        recv_dic = client.recv(10240)
        if recv_dic["type"] == "posion":
            logging.debug("-------------------毒圈轮数：%s-------------------" % str(recv_dic["turn"]))
            logging.debug("毒圈信息：%s" % recv_dic)
            if is_first_flag:
                treasures = recv_dic["treasures"]
                treasures_map = get_treasure_map(treasures)
                # import numpy as np
                # np.savetxt('map.csv', treasures_map, delimiter=',')
                poison_data = recv_dic
                is_first_flag = False
            else:
                poison_data = recv_dic
                turn = 1
        # 需要在5s内响应
        if recv_dic["type"] == "info":
            logging.debug("队员信息：%s" % recv_dic)
            real_data = recv_dic
            move_str = algorithm(treasures_map=treasures_map, poison=poison_data, info=real_data,turn=turn)
            turn = turn + 1
            logging.info("发送信息：%s" % move_str)
            client.send(move_str)


if __name__ == '__main__':
    from testAIPlayer import test_main

    test_main(5)

    client = login()
    mainloop(client)
