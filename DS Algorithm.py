graph = {"Start": {"A":6,"B":2},
         "A"    : {"F":1},
         "B"    : {"A":3,"F":5}}

infinity = float("inf")

costs = {"Start": 0,    
         "A"    :infinity,
         "B"    :infinity,
         "F"    :infinity}

parents = {}

def find_lowest_cost_node(graph):
    lowest_cost = infinity
    for node in costs:
        if node not in processed and costs[node] < lowest_cost:
            lowest_cost = costs[node]
            lowest_node = node
    return lowest_node

processed = []

while len(processed) < len(graph):
    node =  find_lowest_cost_node(graph)
    processed.append(node)
    print("Processing ", node)
    cost = costs[node]

    for i in graph[node].keys():
        print (i)
        new_cost = graph[node][i] + cost
        print (new_cost)
        if new_cost < costs[i]:
            costs[i] = new_cost
        parents[i] = node

def build_path():
    cost = 0
    print ("------------")
    node = "F"
    path = [node]
    while node != "Start":
        cost += graph[parents[node]][node]
        node = parents[node]
        path.append(node)
    print ("Shortest path: ", path[::-1], "  Total cost: ", cost)
    return path[::-1],cost

build_path()


        
        
        

