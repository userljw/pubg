#encoding=utf-8
"""


"""
from STATIC_DATA import OBSTACLE_POSITION_ARRAY,TEAM_NAME
import random
import logging


# 方向说明    5代表原地不动
# 7 8 9
# 4 5 6
# 1 2 3
def algorithm(treasures_map=None,poison=None,info=None,turn=0):
    poison_turn=poison["turn"]
    logging.info("第【%s】轮, 刷毒回合数【%s】" % (turn,poison_turn))




    import time
    time.sleep(0.1)
    move_str = str({"move": [{"id": TEAM_NAME+"01", "movement": str(random.randint(1, 9))}, {"id": TEAM_NAME+"02", "movement": str(random.randint(1, 9))},
                             {"id": TEAM_NAME+"03", "movement":str(random.randint(1, 9))}]})
    return move_str
