#encoding=utf-8
"""
地图静态信息生成
"""
from STATIC_DATA import PUBG_MAP
import copy

"""
获取带奖励信息的地图
"""
def get_treasure_map(treasures):
    treasure_map = copy.deepcopy(PUBG_MAP)
    for (k, v) in treasures.items():
        k_x = k.split(",")[0]
        k_y = k.split(",")[1]
        treasure_map[int(k_x)][int(k_y)]=int(v)
    return treasure_map


"""
目标点障碍物碰撞检测
"""
def get_blank_point(x_y,pubg_map):
    x=x_y[0]
    y=x_y[1]
    if pubg_map[x,y] != 1 :
        return x_y
    else:
        x_y_candidate=[(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x-2,y-2),(x-2,y)]
        for xy in x_y_candidate:
            if pubg_map[xy[0], xy[1]] != 1:
                return xy

"""
获取毒圈内圈坐标列表
[(x,y)(x,y)]
"""


