#encoding=utf-8
"""


"""
from STATIC_DATA import OBSTACLE_POSITION_ARRAY,TEAM_NAME,MOVE_MAP
import logging
import A_start
import Tools

# 方向说明    5代表原地不动
# 7 8 9
# 4 5 6
# 1 2 3
def algorithm(treasures_map=None,poison=None,info=None,remain_step=0):
    poison_turn=poison["turn"]  #毒圈轮数
    # logging.info("第【%s】轮, 刷毒回合数【%s】,剩余步数【%s】" % (turn,poison_turn,remain_step))
    players_info=info["players"]
    sight_info=info["sight"]
    #下一个安全区中心位置
    leftuppoint_srt = poison["leftuppoint"]
    left_point = list(map(int, leftuppoint_srt.strip("]").strip("[").split(",")))
    radius = int(poison["radius"])
    center_point_unchecked= [int(left_point[0] + (radius - 1) / 2), int(left_point[1] + (radius - 1) / 2)]
    center_point = Tools.get_blank_point(center_point_unchecked, treasures_map)
    #下一个安全区域边缘
    edge_point_list=Tools.get_safe_edge_blank(treasures_map,left_point,radius)
    #获得到下一个安全区最短路径 如果在安全里面 one_player["path"]=[]
    players_info_has_shortest = []
    for one_player in players_info:
        point_str = one_player["pos"]
        start_point = list(map(int, point_str.strip("]").strip("[").split(",")))
        if one_player['status'] == 1:
            if center_point_unchecked[0]- (radius - 1) / 2 < start_point[0] <  center_point_unchecked[0]+(radius - 1) / 2 and center_point_unchecked[0]- (radius - 1) / 2 < start_point[1] <  center_point_unchecked[0]+(radius - 1) / 2:
                one_player["path"] = []
            else:
                for end_point in edge_point_list:
                    path_tmp = A_start.get_shortest_path(treasures_map, start_point, end_point)
                    if "path" not in one_player:
                        one_player["path"]=path_tmp
                    elif len(one_player["path"])>= len(path_tmp):
                        one_player["path"]=path_tmp
        else:
            one_player["path"] =False
        players_info_has_shortest.append(one_player)
    logging.debug("players_info_has_shortest %s" %players_info_has_shortest) #每个队员信息增加最短路径
    
    #队员行动路径规则
    #1.毒圈轮数判断
    #前2圈，先吃buff，不进攻。













    #1.计算到目标位置的路径
    players_shortest_path=A_start.format_data_and_get_path(pubg_map=treasures_map,start_point_map=players_info,end_point_map=poison)
    #2.视野分析 + 碰撞检测
    players_move=anlyse_sight(pubg_map=treasures_map,players_shortest_path=players_shortest_path,sight_info=sight_info)

    #3.最后攻击

    move_list=fornmat_move(players_shortest_path)
    move_str=str({"move":move_list})
    return move_str




def anlyse_sight(pubg_map,players_shortest_path,sight_info):
    # 判断视野内
    pass



#返回命令格式化
def fornmat_move(players_shortest_path):
    player_move_list=[]
    for one_player in players_shortest_path:
        if one_player["status"]==0:
            one_player_move={"id":one_player["id"],"movement":str(5)}
        else:
            path=one_player["path"]
            if len(path)==0:
                one_player_move = {"id": one_player["id"], "movement": str(5)}
            else:
                now_point_str=one_player["pos"]
                now_point=list(map(int, now_point_str.strip("]").strip("[").split(",")))
                step_next=path[0]
                direction_tuple=(step_next[0]-now_point[0],step_next[1]-now_point[1])
                direction_str=MOVE_MAP[direction_tuple]
                one_player_move = {"id": one_player["id"], "movement": direction_str}
        player_move_list.append(one_player_move)
    return player_move_list


