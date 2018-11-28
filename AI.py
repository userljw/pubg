#encoding=utf-8
"""


"""

import logging
import A_start
import Tools
import copy
import random
from STATIC_DATA import TEAM_NAME,MOVE_MAP,MOVE_LIST

# 方向说明    5代表原地不动
# 7 8 9
# 4 5 6
# 1 2 3
def algorithm(treasures_map=None,poison=None,info=None,remain_step=0):
    #----------------------------------基础信息准备-start---------------------------------------------
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
    #获得到下一个安全区最短路径 如果在安全里面 one_player["path"]=[]  如果死亡 one_player["path"]=Flase
    players_info_has_shortest = []
    for one_player in players_info:
        point_str = one_player["pos"]
        start_point = list(map(int, point_str.strip("]").strip("[").split(",")))
        if one_player['status'] == 1:
            if left_point[0] < start_point[0] < left_point[0]+ radius-1 and left_point[1] < start_point[1] < left_point[1]+ radius-1:
                one_player["path"] = []
            #  最后一圈 边界判断失效 直接去中心点
            elif int(poison_turn)>5:
                for end_point in edge_point_list:
                    path_tmp = A_start.get_shortest_path(treasures_map, start_point, end_point)
                    if path_tmp!= False:
                        if "path" not in one_player:
                            one_player["path"]=path_tmp
                        elif len(one_player["path"])>= len(path_tmp):
                            one_player["path"]=path_tmp
            else:
                path_tmp = A_start.get_shortest_path(treasures_map, start_point, center_point)
                one_player["path"] = path_tmp
        #队员已经死了
        else:
            one_player["path"] =False
        players_info_has_shortest.append(one_player)
    logging.debug("players_info_has_shortest %s" %players_info_has_shortest) #每个队员信息增加最短路径
    # ----------------------------------基础信息准备-end---------------------------------------------
    #队员行动路径规则
    players_move_list = []
    for one_player in players_info_has_shortest:
        one_player_id = one_player['id']
        point_str = one_player["pos"]
        start_point = list(map(int, point_str.strip("]").strip("[").split(",")))
        if one_player['status'] == 1:
            one_sight_info = get_one_player_sight(id=one_player_id, sight_info_all=sight_info)
            # 如果剩余步数>= 移动到安全区的最小步数
            if remain_step >= len(one_player["path"]):
                # 吃视野内的buff
                buff_point = get_buff_in_sight(one_sight_info)
                if buff_point != None:
                    move_action = A_start.get_shortest_path(treasures_map, start_point, buff_point)
                    one_player["path"] = move_action  # 吃buff
                # 攻击对手
                enemy_point=find_enemy_in_sight(one_sight_info,start_point)
                #一步范围内有人
                if enemy_point !=None:
                    if "teammate" in enemy_point:
                        teammates_map=copy.deepcopy(treasures_map)
                        teammates_map[enemy_point["teammate"][0],enemy_point["teammate"][1]]=1
                        avoid_teammates=A_start.get_shortest_path(teammates_map,start_point,center_point)
                        one_player["path"] = avoid_teammates  # 避让
                    if "enemy" in enemy_point:
                        attac_action=A_start.get_shortest_path(treasures_map, start_point, enemy_point["enemy"])
                        one_player["path"] = attac_action # 进攻
        players_move_list.append(one_player)
    logging.debug("players_move_list %s" % players_move_list)


    players_move_list_optimizationed=[]
    #todo
    if int(poison_turn) >=30 and remain_step >= 4:
        for one_player in players_move_list:
            if one_player['status'] == 1 and len(one_player["path"])==0:
                #去吃地图上最近的一个宝物点：
                point_str = one_player["pos"]
                start_point = list(map(int, point_str.strip("]").strip("[").split(",")))
                sight=one_player["sight"]
                nearest_buff=find_nearest_buff_in_map(start_point,treasures_map,sight)
                if nearest_buff != None:
                    treasures_journey=A_start.get_shortest_path(treasures_map,start_point,nearest_buff)
                    one_player["path"] = treasures_journey # 获取宝物  而不是原地不动
                #附近没有buff 随机走一下
                if len(one_player["path"])==0:
                    one_player["path"] = [MOVE_LIST[random.randint(0,8)]]
            players_move_list_optimizationed.append(one_player)
        # 返回路径格式化
        logging.debug("players_move_list_optimizationed %s" % players_move_list_optimizationed)
        move_list = fornmat_move(players_move_list_optimizationed)
        move_str = str({"move": move_list})
        return move_str

    move_list = fornmat_move(players_move_list)
    move_str = str({"move": move_list})
    return move_str




"""
获取地图内最近的宝物点
4步数内
"""
def find_nearest_buff_in_map(start_point,treasures_map,sight):
    x=start_point[0]
    y=start_point[1]
    try:
        if sight==1:
            x_y_candidate = [(x - 2, y - 2), (x - 1, y - 2), (x, y - 2), (x + 1, y - 2), (x + 2, y - 2),
                             (x - 2, y - 1), (x + 2, y - 1),
                             (x - 2, y), (x + 2, y),
                             (x - 2, y + 1), (x + 2, y + 1),
                             (x - 2, y + 2), (x - 1, y + 2), (x, y + 2), (x + 1, y + 2), (x + 2, y + 2),
                             (x - 3, y - 3), (x - 2, y - 3), (x - 1, y - 3), (x, y - 3), (x + 1, y - 3), (x + 2, y - 3),
                             (x + 3, y + 3),
                             (x - 3, y - 2), (x + 3, y - 2),
                             (x - 3, y - 1), (x + 3, y - 1),
                             (x - 3, y), (x + 3, y),
                             (x - 3, y + 1), (x + 3, y + 1),
                             (x - 3, y + 2), (x + 3, y + 2),
                             (x - 3, y + 3), (x - 2, y + 3), (x - 1, y + 3), (x, y + 3), (x + 1, y + 3), (x + 2, y + 3),
                             (x + 3, y + 3)]
            for xy in x_y_candidate:
                if treasures_map[xy[0],xy[1]] == 2 or treasures_map[xy[0],xy[1]] == 3 or treasures_map[xy[0],xy[1]] == 4:
                    return xy
        if 1<sight<=2:
            x_y_candidate = [(x - 3, y - 3), (x - 2, y - 3), (x - 1, y - 3), (x, y - 3), (x + 1, y - 3), (x + 2, y - 3),
                             (x + 3, y + 3),
                             (x - 3, y - 2), (x + 3, y - 2),
                             (x - 3, y - 1), (x + 3, y - 1),
                             (x - 3, y), (x + 3, y),
                             (x - 3, y + 1), (x + 3, y + 1),
                             (x - 3, y + 2), (x + 3, y + 2),
                             (x - 3, y + 3), (x - 2, y + 3), (x - 1, y + 3), (x, y + 3), (x + 1, y + 3), (x + 2, y + 3),
                             (x + 3, y + 3)]
            for xy in x_y_candidate:
                if treasures_map[xy[0],xy[1]] == 2 or treasures_map[xy[0],xy[1]] == 3 or treasures_map[xy[0],xy[1]] == 4:
                    return xy
        if sight>2:
            return None
    except:
        return None






"""
获取单个视野
"""
def get_one_player_sight(id,sight_info_all):
    for one_sight_dic in sight_info_all:
        if id in one_sight_dic:
            return one_sight_dic[id]
    return []



"""
获取视野内的buff
2、	＋10攻击 player att+10
3、	＋10血量 player hp+10
4、	＋1视野 （player最大3格视野）

input 
[{'pos': '[39,26]', 'type': '1'}, 
{'pos': '[39,27]', 'type': '0'}, 
{'pos': '[39,28]', 'type': '0'},]
"""
def get_buff_in_sight(one_sight_info):
    for point_dic in one_sight_info:
        end_point_str = point_dic["pos"]
        end_point = list(map(int, end_point_str.strip("]").strip("[").split(",")))
        if point_dic["type"] == "2" or point_dic["type"] == "3" or point_dic["type"] == "4":
            return end_point
    return None

"""
获取一步范围内敌人 和 队友的信息
"""
def find_enemy_in_sight(one_sight_info,start_point):
    for point_dic in one_sight_info:
        sight_point_str = point_dic["pos"]
        sight_point = list(map(int, sight_point_str.strip("]").strip("[").split(",")))
        setp_between=Tools.dist_between(sight_point,start_point)
        #一步范围内
        if point_dic["type"] == "6" and setp_between<3:
            enemy_info_dic=point_dic["player"]
            enemy_teamName=enemy_info_dic["teamName"]
            if TEAM_NAME!=enemy_teamName:
                return {"enemy":sight_point}
            else:
                return {"teammate":sight_point}
    return None




"""
返回命令格式化
"""
def fornmat_move(players_shortest_path):
    player_move_list=[]
    for one_player in players_shortest_path:
        if one_player["status"]==0:
            one_player_move={"id":one_player["id"],"movement":str(5)}
        else:
            try:
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
            except:
                one_player_move = {"id": one_player["id"], "movement": str(random.randint(1, 9))}
        player_move_list.append(one_player_move)
    return player_move_list


