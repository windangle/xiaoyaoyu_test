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