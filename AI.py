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
    # 前面两轮 吃buffer 集合
    players_move_list = []
    if int(poison_turn) == 50 or int(poison_turn) == 30:
        players_move_list_tmp=[]
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
                        one_player["path"] = move_action  # 更新原来的行动路径
            players_move_list_tmp.append(one_player)
        logging.debug("players_move_list %s" % players_move_list_tmp)  # 视野内buff获取



        move_list = fornmat_move(players_move_list)
        move_str = str({"move": move_list})
        return move_str


    #3.最后攻击

    #返回路径格式化
    move_list=fornmat_move(players_move_list)
    move_str=str({"move":move_list})
    return move_str


#获取单个视野
def get_one_player_sight(id,sight_info_all):
    for one_sight_dic in sight_info_all:
        if id in one_sight_dic:
            return one_sight_dic[id]
    return []

#获取视野的buff
"""
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








def collision_detection(move):
    pass






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


