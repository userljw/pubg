#encoding=utf-8
"""
A * 计算最近距离
"""
import numpy as np
from heapq import heappush, heappop


def heuristic_cost_estimate(neighbor, goal):
    x = neighbor[0] - goal[0]
    y = neighbor[1] - goal[1]
    return abs(x) + abs(y)


def dist_between(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path


# astar function returns a list of points (shortest path)
def astar(array, start, goal):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # 8个方向

    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic_cost_estimate(start, goal)}

    openSet = []
    heappush(openSet, (fscore[start], start))  # 往堆中插入一条新的值

    # while openSet is not empty
    while openSet:
        # current := the node in openSet having the lowest fScore value
        current = heappop(openSet)[1]  # 从堆中弹出fscore最小的节点

        if current == goal:
            return reconstruct_path(came_from, current)

        close_set.add(current)

        for i, j in directions:  # 对当前节点的 8 个相邻节点一一进行检查
            neighbor = current[0] + i, current[1] + j

            ## 判断节点是否在地图范围内，并判断是否为障碍物
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 1:  # 1为障碍物
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            # Ignore the neighbor which is already evaluated.
            if neighbor in close_set:
                continue

            # The distance from start to a neighbor via current
            tentative_gScore = gscore[current] + dist_between(current, neighbor)

            if neighbor not in [i[1] for i in openSet]:  # Discover a new node
                heappush(openSet, (fscore.get(neighbor, np.inf), neighbor))
            elif tentative_gScore >= gscore.get(neighbor, np.inf):  # This is not a better path.
                continue

                # This path is the best until now. Record it!
            came_from[neighbor] = current
            gscore[neighbor] = tentative_gScore
            fscore[neighbor] = tentative_gScore + heuristic_cost_estimate(neighbor, goal)

    return False


def format_data_and_get_path(pubg_map,start_point_map,end_point_map):
    #计算毒圈中心位置
    leftuppoint_srt=end_point_map["leftuppoint"]
    left_point=list(map(int,leftuppoint_srt.strip("]").strip("[").split(",")))
    radius=int(end_point_map["radius"])
    center_point=[int(left_point[0]+(radius-1)/2),int(left_point[1]+(radius-1)/2)]
    center_point_blank=get_blank_point(center_point,pubg_map)
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
            print("---------------------------------------------")
            print("start_point",start_point)
            print("center_point_blank",center_point_blank)
            print(path)
        else:
            one_player["path"] = None
        reslut_list.append(one_player)
    return reslut_list



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


if __name__ == "__main__":
    nmap = np.loadtxt("map.csv", delimiter=",")
    start_ponit=(17, 29)
    end_point=(17,24)


    end_point_ok=get_blank_point(end_point,nmap)
    path = astar(nmap,start_ponit ,end_point_ok )
    print (path[::-1])
    for i in range(len(path)):
        nmap[path[i]] = 100

    np.savetxt('path.csv', nmap, delimiter=',')