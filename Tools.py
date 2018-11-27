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
def get_safe_edge_blank(treasures_map,left_point,radius):
    left_point_x=left_point[0]
    left_point_y=left_point[1]
    edge_list=[]
    for i in range(1,radius-1):
        point_top=(left_point_x+1,left_point_y+i)
        point_buttom=(left_point_x+radius-3,left_point_y+i)
        point_left=(left_point_x+i,left_point_y+1)
        point_right=(left_point_x+i,left_point_y+radius-3)
        if 0<=point_top[0]<=49 and 0<=point_top[1]<=49 and treasures_map[point_top[0],point_top[1]] != 1:
            edge_list.append(point_top)
        if 0<=point_buttom[0]<=49 and 0<=point_buttom[1]<=49 and treasures_map[point_buttom[0], point_buttom[1]] != 1:
            edge_list.append(point_buttom)
        if 0<=point_left[0]<=49 and 0<=point_left[1]<=49 and treasures_map[point_left[0], point_left[1]] != 1:
            edge_list.append(point_left)
        if 0<=point_right[0]<=49 and 0<=point_right[1]<=49 and treasures_map[point_right[0], point_right[1]] != 1:
            edge_list.append(point_right)
    return list(set(edge_list))