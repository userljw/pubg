#encoding=utf-8


# GLOBLE_CONFIG
ADDR = ('127.0.0.1', 8888)
TEAM_NAME = "背锅侠"


#障碍物
OBSTACLE_POSITION_ARRAY = {"0,27", "0,28", "0,29", "0,30", "1,27", "1,28", "1,29", "1,30",
                           "2,17", "2,27", "2,28", "2,29", "2,30", "3,5", "3,6", "3,7", "3,18", "3,26", "3,27", "3,28",
                           "3,29", "3,40",
                           "3,41", "3,42", "3,43", "3,44", "4,4", "4,8", "4,19", "4,25", "4,26", "4,27", "4,28", "4,40",
                           "5,3", "5,9",
                           "5,19", "5,40", "5,46", "6,3", "6,19", "6,25", "6,26", "6,27", "6,28", "6,40", "6,46", "7,3",
                           "7,19",
                           "7,25", "7,26", "7,27", "7,28", "7,40", "7,46", "8,4", "8,19", "8,25", "8,26", "8,27",
                           "8,28", "8,33",
                           "8,34", "8,35", "8,36", "8,37", "8,45", "9,5", "9,7", "9,19", "9,25", "9,26", "9,27", "9,28",
                           "9,32",
                           "9,40", "9,41", "9,42", "9,43", "9,44", "10,8", "10,12", "10,13", "10,14", "10,15", "10,19",
                           "10,25",
                           "10,26", "10,27", "10,28", "10,31", "10,40", "11,9", "11,25", "11,26", "11,27", "11,28",
                           "11,30", "11,40",
                           "12,9", "12,40", "13,9", "13,25", "13,26", "13,28", "13,40", "14,3", "14,8", "14,26",
                           "14,28", "14,40",
                           "15,4", "15,5", "15,6", "15,7", "15,25", "15,28", "15,40", "16,25", "16,26", "16,27",
                           "16,28", "16,40",
                           "17,25", "17,26", "17,27", "17,28", "18,25", "18,26", "18,27", "18,28", "19,5", "19,6",
                           "19,26", "19,27",
                           "19,28", "19,35", "19,40", "20,4", "20,7", "20,16", "20,17", "20,18", "20,36", "20,40",
                           "21,8", "21,15",
                           "21,19", "21,25", "21,26", "21,27", "21,37", "21,40", "22,3", "22,14", "22,20", "22,25",
                           "22,26", "22,27",
                           "22,28", "22,38", "22,40", "23,4", "23,7", "23,8", "23,13", "23,25", "23,26", "23,27",
                           "23,28", "23,39",
                           "23,40", "24,5", "24,6", "24,8", "24,13", "24,14", "24,15", "24,16", "24,17", "24,21",
                           "24,25", "24,26",
                           "24,27", "24,28", "25,8", "25,21", "25,25", "25,26", "25,27", "25,28", "25,39", "25,40",
                           "26,12", "26,13",
                           "26,14", "26,15", "26,16", "26,18", "26,21", "26,28", "26,38", "26,40", "27,3", "27,8",
                           "27,12", "27,13",
                           "27,14", "27,15", "27,16", "27,18", "27,19", "27,20", "27,21", "27,25", "27,26", "27,28",
                           "27,37", "27,40",
                           "28,4", "28,7", "28,13", "28,14", "28,15", "28,16", "28,17", "28,18", "28,19", "28,20",
                           "28,21", "28,25",
                           "28,26", "28,28", "28,36", "28,40", "29,5", "29,6", "29,14", "29,15", "29,16", "29,17",
                           "29,19", "29,20",
                           "29,35", "29,40", "30,34", "30,40", "31,25", "31,26", "31,27", "31,28", "31,33", "31,40",
                           "32,25", "32,26",
                           "32,27", "32,28", "33,3", "33,4", "33,5", "33,6", "33,24", "33,25", "33,26", "33,27", "34,3",
                           "34,7",
                           "34,23", "34,24", "34,25", "34,26", "34,29", "34,40", "34,41", "34,42", "34,43", "35,3",
                           "35,8", "35,23",
                           "35,24", "35,25", "35,26", "35,40", "35,44", "36,3", "36,9", "36,23", "36,24", "36,25",
                           "36,26", "36,45",
                           "37,3", "37,40", "37,45", "38,3", "38,9", "38,23", "38,24", "38,25", "38,26", "38,40",
                           "38,44", "39,3",
                           "39,9", "39,23", "39,24", "39,25", "39,26", "39,40", "39,42", "39,43", "40,3", "40,9",
                           "40,23", "40,24",
                           "40,25", "40,26", "40,40", "40,44", "41,3", "41,9", "41,23", "41,24", "41,25", "41,26",
                           "41,40", "42,9",
                           "42,13", "42,14", "42,15", "42,17", "42,18", "42,19", "42,23", "42,24", "42,25", "42,26",
                           "42,40", "42,45",
                           "43,3", "43,9", "43,12", "43,16", "43,20", "43,45", "44,3", "44,40", "44,45", "45,3", "45,7",
                           "45,12",
                           "45,16", "45,20", "45,23", "45,24", "45,25", "45,26", "45,40", "45,44", "46,3", "46,4",
                           "46,5", "46,6",
                           "46,13", "46,14", "46,15", "46,17", "46,18", "46,19", "46,23", "46,24", "46,25", "46,26",
                           "46,40", "46,41",
                           "46,42", "46,43", "47,23", "47,24", "47,25", "47,26", "48,23", "48,24", "48,25", "48,26",
                           "49,23", "49,24",
                           "49,25", "49,26"};


import numpy as np
def get_original_map():
    pubg_map = np.zeros((50, 50))
    for obstacle in OBSTACLE_POSITION_ARRAY:
        obstacle_x=obstacle.split(",")[0]
        obstacle_y = obstacle.split(",")[1]
        pubg_map[int(obstacle_x)][int(obstacle_y)]=1
    return pubg_map

PUBG_MAP=get_original_map()