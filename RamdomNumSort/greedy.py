#贪婪算法，greedy algorithm
def greedy(dicThing):
    best_thing = []
    discovered = set()
    for item_a, item_b in dicThing.items():
        discovered = discovered.union(item_b)
    dicTemp = dict(dicThing)
    while discovered:
        best_thing.append(greedy_c(dicTemp, discovered))
    return best_thing

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