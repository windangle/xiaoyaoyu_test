#**********************************************************#
#*  name	:贪婪算法									  *#
#* 	author	:张祥春										  *#
#* 	create time	:2018/05/04								  *#
#* 	modify time	:2018/05/04								  *#
#* 	introduction:贪婪算法练习							  *#
#**********************************************************#

#贪婪算法，greedy algorithm
#原始版本————————————————————————————————————————————————————————————
#贪婪算法主体，用来做数据初始化和输出最终结果
def greedy(dicThing):
    best_thing = []
    discovered = []
    for item_a in dicThing:
        for item_b in dicThing[item_a]:
            if item_b not in discovered:
                discovered.append(item_b)
    dicTemp = dict(dicThing)
    while discovered:
        best_thing.append(greedy_c(dicTemp, discovered))
    return best_thing
#贪婪算法循环体，用来循环不断找出覆盖最广的一个元素
def greedy_c(dicTemp,discovered):
    covered = {}
    max_thing = list(dicTemp.keys())[0]
    for item in dicTemp.keys():
        discovered_count = 0
        for item_b in dicTemp[item]:
            if item_b in discovered:
                discovered_count += 1
        covered[item] = discovered_count
    for item in covered.keys():
        if covered[item] > covered[max_thing]:
            max_thing = item
    for item in dicTemp[max_thing]:
        if item in discovered:
            discovered.remove(item)
    dicTemp.pop(max_thing)
    return max_thing

#定义覆盖区域的散列表
stations = {}
stations["100"] =["guangdong", "guangxi", "jiangxi", "hunan"]
stations["101"] =["guangdong", "fujian", "jiangxi", "hunan", "zhejiang", "anhui", "hubei", "jiangsu"]
stations["102"] =["gansu", "qinghai", "shanqi", "neimeng", "chongqing", "sichuan", "hubei", "ningxia"]
stations["103"] =["beijing", "tianjing", "hebei", "henan", "shandong", "shanxi", "neimeng", "liaoning", "jiangsu"]
stations["104"] =["liaoning", "jilin", "heilongjiang", "neimenggu"]
stations["105"] =["guangdong", "jilin", "jiangxi", "henan"]

broadcast = greedy(stations)
print(broadcast)
#原始版本————————————————————————————————————————————————————————————

#用集合对象优化后版本————————————————————————————————————————————————
#贪婪算法主体，用来做数据初始化和输出最终结果
def greedy(dicThing):
    best_thing = []
    discovered = set()
    for item_a, item_b in dicThing.items():
        discovered = discovered.union(item_b)
    dicTemp = dict(dicThing)
    while discovered:
        best_thing.append(greedy_c(dicTemp, discovered))
    return best_thing
#贪婪算法循环体，用来循环不断找出覆盖最广的一个元素
def greedy_c(dicTemp, discovered):
    max_covered = set()
    for item_a, item_b in dicTemp.items():
        covered = discovered.intersection(item_b)
        if len(covered) > len(max_covered):
            max_covered = covered
            max_thing = item_a
    discovered.difference_update(dicTemp[max_thing])
    dicTemp.pop(max_thing)
    return max_thing

#定义覆盖区域的散列表
stations = {}
stations["100"] =["guangdong", "guangxi", "jiangxi", "hunan"]
stations["101"] =["guangdong", "fujian", "jiangxi", "hunan", "zhejiang", "anhui", "hubei", "jiangsu"]
stations["102"] =["gansu", "qinghai", "shanqi", "neimeng", "chongqing", "sichuan", "hubei", "ningxia"]
stations["103"] =["beijing", "tianjing", "hebei", "henan", "shandong", "shanxi", "neimeng", "liaoning", "jiangsu"]
stations["104"] =["liaoning", "jilin", "heilongjiang", "neimenggu"]
stations["105"] =["guangdong", "jilin", "jiangxi", "henan"]

broadcast = greedy(stations)
print(broadcast)
#用集合对象优化后版本————————————————————————————————————————————————