# #encoding=utf-8
#
# import sys
#
#
# print(sys.__stdout__.encoding)
#
# b=b'1762{"teams":[{"teamName":"\xb1\xb3\xb9\xf8\xcf\xc04","score":"0"},{"teamName":"\xb1\xb3\xb9\xf8\xcf\xc04","score":"0"},{"teamName":"\xb1\xb3\xb9\xf8\xcf\xc04","score":"0"},{"teamName":"\xb1\xb3\xb9\xf8\xcf\xc04","score":"0"}],"players":[{"teamName":"\xb1\xb3\xb9\xf8\xcf\xc04","pos":"[23,34]","attack":10,"teamId":"7","damageRatio":1,"sight":1,"id":"\xb1\xb3\xb9\xf8\xcf\xc0401","life":100,"status":1},{"teamName":"\xb1\xb3\xb9\xf8\xcf\xc04","pos":"[27,42]","attack":10,"teamId":"7","damageRatio":1,"sight":1,"id":"\xb1\xb3\xb9\xf8\xcf\xc0402","life":100,"status":1},{"teamName":"\xb1\xb3\xb9\xf8\xcf\xc04","pos":"[27,42]","attack":10,"teamId":"7","damageRatio":1,"sight":1,"id":"\xb1\xb3\xb9\xf8\xcf\xc0402","life":100,"status":1}],"sight":[{"\xb1\xb3\xb9\xf8\xcf\xc0401":[{"pos":"[22,33]","type":"0"},{"pos":"[22,34]","type":"0"},{"pos":"[22,35]","type":"0"},{"pos":"[23,33]","type":"0"},{"pos":"[23,34]","type":"6","player":{"teamName":"\xb1\xb3\xb9\xf8\xcf\xc04","pos":"[23,34]","attack":10,"teamId":"7","damageRatio":1,"sight":1,"id":"\xb1\xb3\xb9\xf8\xcf\xc0401","life":100,"status":1}},{"pos":"[23,35]","type":"0"},{"pos":"[24,33]","type":"0"},{"pos":"[24,34]","type":"0"},{"pos":"[24,35]","type":"0"}]},{"\xb1\xb3\xb9\xf8\xcf\xc0402":[{"pos":"[26,41]","type":"0"},{"pos":"[26,42]","type":"0"},{"pos":"[26,43]","type":"0"},{"pos":"[27,41]","type":"0"},{"pos":"[27,42]","type":"6","player":{"teamName":"\xb1\xb3\xb9\xf8\xcf\xc04","pos":"[27,42]","attack":10,"teamId":"7","damageRatio":1,"sight":1,"id":"\xb1\xb3\xb9\xf8\xcf\xc0402","life":100,"status":1}},{"pos":"[27,43]","type":"0"},{"pos":"[28,41]","type":"0"},{"pos":"[28,42]","type":"0"},{"pos":"[28,43]","type":"0"}]},{"\xb1\xb3\xb9\xf8\xcf\xc0402":[{"pos":"[26,41]","type":"0"},{"pos":"[26,42]","type":"0"},{"pos":"[26,43]","type":"0"},{"pos":"[27,41]","type":"0"},{"pos":"[27,42]","type":"6","player":{"teamName":"\xb1\xb3\xb9\xf8\xcf\xc04","pos":"[27,42]","attack":10,"teamId":"7","damageRatio":1,"sight":1,"id":"\xb1\xb3\xb9\xf8\xcf\xc0402","life":100,"status":1}},{"pos":"[27,43]","type":"0"},{"pos":"[28,41]","type":"0"},{"pos":"[28,42]","type":"0"},{"pos":"[28,43]","type":"0"}]}],"type":"info"}'
#
#
# print(type(b))
# bs = str(b, encoding = "gbk")
#
# print(bs)
#
# aa=bs[4:]
# print(aa)
#
# import json
# dictinfo = json.loads(aa)
#
# print(type(dictinfo))
#
# treasures={'31,18': '3', '48,2': '3', '7,34': '3', '30,3': '2', '1,34': '3', '30,21': '4', '37,22': '4', '20,45': '3', '23,35': '3', '32,43': '3', '43,7': '4', '12,48': '4', '37,47': '2', '22,39': '3', '5,48': '3', '12,19': '3', '26,41': '4', '14,38': '3', '38,48': '3', '0,0': '2', '47,39': '2', '21,34': '3', '16,49': '4', '14,13': '4', '47,31': '2', '28,31': '4', '29,10': '3', '38,41': '3', '37,1': '4', '41,13': '2', '21,39': '3', '28,44': '4', '32,2': '2', '35,30': '3', '36,31': '3', '11,13': '3', '14,12': '3', '25,3': '3', '17,45': '3', '15,3': '2', '20,37': '3', '22,33': '3', '23,36': '3', '3,34': '4', '38,18': '2', '14,35': '4', '36,16': '3', '5,35': '4', '26,39': '4', '21,10': '3', '35,28': '3', '48,48': '2', '49,35': '4', '15,42': '4', '33,13': '4', '21,7': '4', '24,12': '3', '49,13': '4', '5,10': '3', '19,21': '3', '1,32': '3', '36,6': '3', '28,45': '3', '15,49': '4', '0,20': '3', '32,18': '3', '27,39': '4', '6,10': '4', '31,16': '3', '34,10': '2', '3,24': '2', '11,4': '3', '40,49': '4', '9,48': '4', '40,19': '3', '28,12': '3', '23,20': '2', '7,29': '3', '41,18': '3', '46,29': '4', '39,1': '2', '3,48': '3', '31,0': '2', '33,8': '4', '19,45': '4', '8,8': '4', '3,8': '2', '33,36': '3', '30,43': '3', '31,30': '3', '19,47': '3', '21,17': '4'}
#
#
# from Tools import get_treasure_map
#
#
# import numpy as np
# aaaaaaaaaa=get_treasure_map(treasures)
#
#
# np.savetxt('featvector.csv', aaaaaaaaaa, delimiter=',')
#
# import numpy as np
# leftuppoint_srt = "[1,34]"
# left_point = list(map(int, leftuppoint_srt.strip("]").strip("[").split(",")))
# print(left_point)
#
#
# aa=['15', '3']
# intt=list(map(int,aa))
# print(intt)
#
# start=[1,2]
# gscore = {start: 0}





# import numpy as np
# nmap = np.array([
#         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 0, 1 , 1, 1, 1, 1, 0, 1],
#         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#         [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 123, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
#
# print(nmap[1,2])


# def get_safe_edge_blank(treasures_map,left_point,radius):
#     left_point_x=left_point[0]
#     left_point_y=left_point[1]
#     edge_list=[]
#     for i in range(1,radius-1):
#         point_top=(left_point_x+1,left_point_y+i)
#         edge_list.append(point_top)
#         point_buttom=(left_point_x+radius-2,left_point_y+i)
#         point_left=(left_point_x+i,left_point_y+1)
#         point_right=(left_point_x+i,left_point_y+radius-2)
#         edge_list.append(point_buttom)
#         edge_list.append(point_left)
#         edge_list.append(point_right)
#     return list(set(edge_list))

print (int("50"))