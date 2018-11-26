#encoding=utf-8
"""
A * 计算最近距离
"""
import numpy as np
from heapq import heappush, heappop
import logging
import Tools

def heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2


def astar(array, start, goal):
    if start == goal:
        return []
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))

    while oheap:

        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))
    return False



"""
start_point (x,y)
end_point (x,y)
"""
def get_shortest_path(pubg_map,start_point,end_point):
    try:
        reverse_path = astar(pubg_map, tuple(start_point), tuple(end_point))
        path = reverse_path[::-1]
        return path
    except:
        return False








def format_data_and_get_path(pubg_map,start_point_map,end_point_map):
    #计算毒圈中心位置
    leftuppoint_srt=end_point_map["leftuppoint"]
    left_point=list(map(int,leftuppoint_srt.strip("]").strip("[").split(",")))
    radius=int(end_point_map["radius"])
    center_point=[int(left_point[0]+(radius-1)/2),int(left_point[1]+(radius-1)/2)]
    center_point_blank=Tools.get_blank_point(center_point,pubg_map)
    reslut_list=[]
    for one_player in start_point_map:
        #如果存活
        if one_player['status'] == 1:
            point_str=one_player["pos"]
            start_point = list(map(int,point_str.strip("]").strip("[").split(",")))
            end_point=center_point_blank
            reverse_path = astar(pubg_map, tuple(start_point), tuple(end_point))
            path=reverse_path[::-1]
            one_player["path"]=path
            logging.debug("play_id:%s  start_point:%s --> end_point_blank:%s" % (str(one_player["id"]) ,str(start_point),str(center_point_blank)))
        else:
            one_player["path"] = None
        reslut_list.append(one_player)
    return reslut_list





if __name__ == "__main__":
    nmap = np.loadtxt("map.csv", delimiter=",")
    start_ponit=(17, 29)
    end_point=(17,24)
    end_point_ok=Tools.get_blank_point(end_point,nmap)
    path = astar(nmap,start_ponit ,end_point_ok )
    print (path[::-1])
    for i in range(len(path)):
        nmap[path[i]] = 100

    np.savetxt('path.csv', nmap, delimiter=',')