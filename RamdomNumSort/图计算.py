#**********************************************************#
#*  name	:图计算										  *#
#* 	author	:张祥春										  *#
#* 	create time	:2018/05/01								  *#
#* 	modify time	:2018/05/04								  *#
#* 	introduction:各类图计算练习							  *#
#**********************************************************#

#广度优先搜索算法————————————————————————————————————————————————————————————
from collections import deque

#找在散列表graph中查找name的人的邻居中的芒果seller结尾的名字的人
def search_mongo_seller(graph, name, searchname):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    path = {}
    path[name] = ""
    for item in graph[name]:
        path[item] = name
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person == searchname:
                break
            else:
                search_queue += graph[person]
                searched.append(person)
                for item in graph[person]:
                    if not item in searched:
                        path[item] = person
    strPath = searchname
    strItem = path[searchname]
    while strItem:
        strPath = strItem + "->" +strPath
        strItem = path[strItem]
    return strPath
	
#散列表实现图
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

path = search_mongo_seller(graph, "you", "jonny")
print(path)
#广度优先搜索算法————————————————————————————————————————————————————————————

#自己编写的狄克斯特拉算法——————————————————————————————————————————————————————————————
from collections import deque

#查找最近路线，路线带权重
def ds(graph, start, end):
    searched = dict(graph[start])   #搜索过的节点到起点的距离
    path = {start: ""}              #搜索过的节点的父节点
    search_queue = deque()
    search_queue += graph[start].keys()
    for item in graph[start].keys():
        path[item] = start
    while search_queue:
        point = search_queue.popleft()
        for item in graph[point].keys():
            if (not item in searched.keys()) or (searched[point] + graph[point][item] < searched[item]):
                searched[item] = searched[point] + graph[point][item]
                path[item] = point
                search_queue += graph[point].keys()
    strpath = end + ",共计%d公里。" %(searched[end])
    stritem = path[end]
    while stritem:
        strpath = stritem + "->" + strpath
        stritem = path[stritem]
    return strpath

#散列表实现图
graph = {}
graph["shenzhen"] = {"shaoguan": 350, "dongguan": 50, "huizhou": 150}
graph["huizhou"] = {"heyuan": 150}
graph["heyuan"] = {"dingnan": 150}
graph["dingnan"] = {"yingtan": 350}
graph["yingtan"] = {"guixi": 50}
graph["dongguan"] = {"zengcheng": 100}
graph["zengcheng"] = {"dingnan": 330, "ganzhou": 290}
graph["shaoguan"] = {"ganzhou": 100}
graph["ganzhou"] = {"yingtan": 400}
graph["guixi"] = {}

path = ds(graph, "shenzhen", "guixi")
print(path)
#自己编写的狄克斯特拉算法——————————————————————————————————————————————————————————————

#书上的狄克斯特拉算法——————————————————————————————————————————————————————————————————
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = int(costs[node])
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

#散列表实现图
graph = {}
graph["shenzhen"] = {"shaoguan": 350, "dongguan": 50, "huizhou": 150}
graph["huizhou"] = {"heyuan": 150}
graph["heyuan"] = {"dingnan": 150}
graph["dingnan"] = {"yingtan": 350}
graph["yingtan"] = {"guixi": 50}
graph["dongguan"] = {"zengcheng": 100}
graph["zengcheng"] = {"dingnan": 330, "ganzhou": 290}
graph["shaoguan"] = {"ganzhou": 100}
graph["ganzhou"] = {"yingtan": 400}
graph["guixi"] = {}
#消耗表
infinity =float("inf")
costs = {}
costs = {"shaoguan": 350, "dongguan": 50, "huizhou": 150, "heyuan": infinity, "dingnan": infinity, "yingtan": infinity, "zengcheng": infinity, "ganzhou": infinity, "guixi": infinity}
#父级节点表
parents = {}
costs = {"shaoguan": "shenzhen", "dongguan": "shenzhen", "huizhou": "shenzhen", "heyuan": infinity, "dingnan": infinity, "yingtan": infinity, "zengcheng": infinity, "ganzhou": infinity, "guixi": infinity}
processed = []

node = find_lowest_cost_node(costs)
while node is not None:
    cost = int(costs[node])
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print(costs)
#书上的狄克斯特拉算法——————————————————————————————————————————————————————————————————