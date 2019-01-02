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
    board = {} # 用字典存储棋盘
    JAR_SUM = 50 # 棋盘中的罐子的数量
    EMPTY_GRID = -1 # 空格子的分数
    JAR_GRID = 10 # 放罐子的格子的分数
    # 用两个简单循环填充棋盘，-1代表没有罐子，10代表有罐子。初始化为-1，后面再放罐子。
    for x in range(0,10):
        for y in range(0,10):
            board[10*x + y] = EMPTY_GRID;
    # 随机往棋盘上放JAR_SUM个罐子
    x = 0
    while x < JAR_SUM:
        y = random.randint(0,99)
        if board[y] == EMPTY_GRID:
            board[y] = JAR_GRID
            x += 1
    return board
# 初始化基因组
def initialize_dna():
    # 用字典存储dna，用key代表具体的基因，用value表示基因的序列。
    # 基因由5个字母的字符串组成，每一位分别表示东南西北中的方位，而其中的字母e代表空，j代表罐子，w代表墙。
    # 基因有由1种组成、有2种基因组成、3种基因组成三种情况。1种基因的情况只有3种，因此定义时直接给出。
    dna = { "eeeee":0,"jjjjj":0,"wwwww":0 } 
    dna.update(sequence_2dna(dna, "eeeee", "j", 0, 5))
    dna.update(sequence_2dna(dna, "eeeee", "w", 0, 5))
    dna.update(sequence_2dna(dna, "jjjjj", "w", 0, 5))

def sequence_2dna(dict_dna, str_dic, item_dic, s_num, e_num):    
    for x in range(s_num, e_num):
        if x == 0:
            str_dic_x = item_dic + str_dic[1:e_num]
        else:
            str_dic_x = str_dic[0:x] + item_dic + str_dic[x+1:e_num]
        dict_dna[str_dic_x] = 0
        if s_num < e_num:
            dict_dna.update(sequence_dna(dict_dna, str_dic_x, item_dic, s_num+1, e_num))
    return dict_dna