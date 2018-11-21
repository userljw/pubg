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






