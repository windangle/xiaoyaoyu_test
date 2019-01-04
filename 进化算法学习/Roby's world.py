#-*-conding:utf-8-*-
''' 
《===罗比的世界进化算法===》
题目：
一个叫罗比的机器人，生活在一个10X10的方格的世界中，这个世界的外围是一圈墙，这个世界中随机分布着一些罐子(每个格子里最多只有一个罐子)，罗比的任务就是把这些罐子捡起来，任务规则如下：
1、每一次执行任务罗比从世界最左上角的位置出发。
2、罗比只能看到他所在格子及东南西北一个格子的情况。
3、罗比可以执行7种操作，分别是向东走一格、向南走一格、向西走一格、向北走一格、随机走一格、不动、捡罐子。
4、罗比成功捡到1个罐子得10分，在没有罐子的格子里捡罐子扣1分，撞墙扣5分并回到撞墙前得位置。
5、每一次执行任务只能执行200次操作。
请帮助他设计一套算法，让他能够得到尽量高的分。
使用进化算法，分数据初始化，捡罐子算法，基因遗传，数据持久化4大部分。
''' 
import random

# 《==数据初始化==》

# 《=初始化棋盘=》
def initialize_board():
    board = {}  # 用字典存储棋盘
    JAR_SUM = 50  # 棋盘中的罐子的数量
    EMPTY_GRID = -1  # 空格子的分数
    JAR_GRID = 10  # 放罐子的格子的分数
    # 用两个简单循环填充棋盘，-1代表没有罐子，10代表有罐子。初始化为-1，后面再放罐子。
    for x in range(0, 10):
        for y in range(0, 10):
            board[(x, y)] = EMPTY_GRID;
    # 随机往棋盘上放JAR_SUM个罐子
    x = 0
    while x < JAR_SUM:
        y = (random.randint(0,9), random.randint(0,9))
        if board[y] == EMPTY_GRID:
            board[y] = JAR_GRID
            x += 1
    return board

# 初始化基因组
def initialize_dna():
    # 用字典存储dna，用key代表具体的基因，用value表示基因的序列。
    # 基因由5个字母的字符串组成，每一位分别表示东南西北中的方位，而其中的字母e代表空，j代表罐子，w代表墙。
    # 基因有由1种组成、有2种基因组成、3种基因组成三种情况。1种基因的情况只有3种，因此定义时直接给出。
    COUNT = 5 # 表示基因的位数
    result = item = ["e", "j", "w"]  # 定义基因的组成元素
    temp = []
    for x in range(1, COUNT):
        for y in range(0, len(result)):
            for z in range(0, len(item)):
                temp.append(result[y] + item[z])
        result = temp
        temp = []
    return result

# 用1~7的随机数初始化dna，1、2、3、4、5、6、7分别代表东、南、西、北、不动、捡罐子、随机操作一下
def random_dna(dna):
    dna_obj = {}
    for item in dna:
        dna_obj[item] = random.randint(1, 7)
    return dna_obj

# 捡罐子
# pick_dna传入基因组，board传入棋盘，operation times传入一次捡罐子任务的操作次数。
def pick_jar(pick_dna, board, operation_times):
    roby = [0, 0]
    result_once = 0
    while operation_times > 0:
        action = pick_dna[look_around(board, roby)]  # 看周围的情况决定行动
        while action > 0:
            if action == 1:
                if roby[1] == 9:
                    result_once -= 5
                    action = 0
                else:
                    roby[1] += 1
                    action = 0
            elif action == 2:
                if roby[0] == 9:
                    result_once -= 5
                    action = 0
                else:
                    roby[0] += 1
                    action = 0
            elif action == 3:
                if roby[1] == 0:
                    result_once -= 5
                    action = 0
                else:
                    roby[1] -= 1
                    action = 0
            elif action == 4:
                if roby[0] == 0:
                    result_once -= 5
                    action = 0
                else:
                    roby[0] -= 1
                    action = 0
            elif action == 6:
                result_once += board[roby[0], roby[1]]
                action = 0
            else:
                action == random.randint(1, 6)

#看周围情况
def look_around(board, roby):
    around_list = []
    # 东
    if roby[1] == 9:
        around_list.append("w")
    elif board[roby[0], roby[1]+1] == 10:
        around_list.append("j")
    else:
        around_list.append("e")
    # 南
    if roby[0] == 9:
        around_list.append("w")
    elif board[roby[0]+1, roby[1]] == 10:
        around_list.append("j")
    else:
        around_list.append("e")
    # 西
    if roby[1] == 0:
        around_list.append("w")
    elif board[roby[0], roby[1]-1] == 10:
        around_list.append("j")
    else:
        around_list.append("e")
    # 北
    if roby[0] == 0:
        around_list.append("w")
    elif board[roby[0]-1, roby[1]] == 10:
        around_list.append("j")
    else:
        around_list.append("e")
    # 中
    if board[roby[0], roby[1]] == 10:
        around_list.append("j")
    else:
        around_list.append("e")
    around_str = "".join(around_list)
    return around_str

# 程序主体
# 读取dna序列
txt_obj = open("initialize_dna.txt", "w+")
txt_obj.write(str(initialize_dna()))
txt_obj.close()
txt_obj = open("initialize_dna.txt", "r+")
dna = eval(txt_obj.read())
txt_obj.close()
# 执行任务，每种基因执行dna_times次，每轮执行dna_count个dna轮回，执行sum_times次轮回，每一种基因每次执行opertion_times步操作，而所有基因存在dna_dic中
dna_times = 2  # 每一种基因执行dna_times次
dna_count = 2  # 每一轮中使用dna_count种基因组
sum_times = 1  # 执行sum_times轮
opertion_times = 100  # 每一种基因每次执行opertion_times步操作
dna_dic = {}
result_list = []
for x in range(0,sum_times):  # 执行sum_times轮
    result_list.append([])
    for y in range(0, dna_count):  # 每一轮中使用dna_count种基因组
        result_list[x].append([])
        if x == 0:  # 如果是第一轮，初始化使用随机数进行基因
            dna_dic[y] = random_dna(dna)
        for z in range(0, dna_times):  # 每一种基因执行dna_times次
            result_list[x][y].append(pick_jar(dna_dic[y], initialize_board(),opertion_times))
    # 基因变异
txt_obj = open("result.txt", "w+")
txt_obj.write(str(result_list))
txt_obj.close()