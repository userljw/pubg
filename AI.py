#encoding=utf-8
"""


"""
from STATIC_DATA import OBSTACLE_POSITION_ARRAY,TEAM_NAME,MOVE_MAP
import random
import logging
import A_start

# 方向说明    5代表原地不动
# 7 8 9
# 4 5 6
# 1 2 3
def algorithm(treasures_map=None,poison=None,info=None,turn=0):
    poison_turn=poison["turn"]
    remain_step = int(poison_turn) - int(turn) - 1
    logging.info("第【%s】轮, 刷毒回合数【%s】,剩余步数【%s】" % (turn,poison_turn,remain_step))
    players_info=info["players"]
    #队员行动路径
    players_shortest_path=A_start.format_data_and_get_path(pubg_map=treasures_map,start_point_map=players_info,end_point_map=poison)
    move_list=fornmat_move(players_shortest_path)
    move_str=str({"move":move_list})
    return move_str


def fornmat_move(players_shortest_path):
    player_move_list=[]
    for one_player in players_shortest_path:
        if one_player["status"]==0:
            one_player_move={"id":one_player["id"],"movement":str(5)}
        else:
            path=one_player["path"]
            if len(path)==1:
                one_player_move = {"id": one_player["id"], "movement": str(5)}
            else:
                now_point=path[0]
                step_next=path[1]
                direction_tuple=(step_next[0]-now_point[0],step_next[1]-now_point[1])
                direction_str=MOVE_MAP[direction_tuple]
                one_player_move = {"id": one_player["id"], "movement": direction_str}
        player_move_list.append(one_player_move)
    return player_move_list


