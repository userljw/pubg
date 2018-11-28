# encoding=utf-8

from SockClient import SockClient
import logging
import random
from STATIC_DATA import ADDR, TEAM_NAME
from AI import algorithm
from Tools import get_treasure_map

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
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
    poison_turn=0
    while True:
        recv_dic = client.recv(10240)
        if recv_dic["type"] == "posion":
            poison_turn = recv_dic["turn"]
            logging.debug("-------------------毒圈轮数：%s-------------------" % str(poison_turn))
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
            remain_step = int(poison_turn) - int(turn)
            logging.info("第【%s】轮, 刷毒回合数【%s】,剩余步数【%s】" % (turn, poison_turn, remain_step))
            logging.debug("接收信息：%s" % recv_dic)
            real_data = recv_dic
            #防止触发bug掉线
            try:
                move_str = algorithm(treasures_map=treasures_map, poison=poison_data, info=real_data,remain_step=remain_step)
            except Exception as es:
                logging.error("---触发算法bug，随机游走--- Exception[%s]" % es)
                move_str = str({"move": [{"id": TEAM_NAME + "01", "movement": str(random.randint(1, 9))},
                                         {"id": TEAM_NAME + "02", "movement": str(random.randint(1, 9))},
                                         {"id": TEAM_NAME + "03", "movement": str(random.randint(1, 9))}]})
            turn = turn + 1
            logging.info("发送信息：%s" % move_str)
            client.send(move_str)


if __name__ == '__main__':

    from testAIPlayer import test_main
    test_main(6)

    client = login()
    mainloop(client)
