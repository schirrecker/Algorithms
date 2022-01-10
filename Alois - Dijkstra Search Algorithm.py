print("__________________________________________________")
print("Processing:")

graph = {"Start": {"A":5,"B":2},
         "A"    : {"C":4,"D":2},
         "B"    : {"A":8,"D":7},
         "C"    : {"Fin":3,"D":6},
         "D"    : {"Fin":1},
         "Fin"  : {}}

infinity = float("inf")

costs = {"Start": 0,    
         "A"    :infinity,
         "B"    :infinity,
         "C"    :infinity,
         "D"    :infinity,
         "Fin"  :infinity}

def find_lowest_cost_node(graph, processed):
    
    '''
    search all nodes in graph (costs[]) 
    find the one with the lowest cost, and which has not been processed yet
    '''
               
    lowest_cost = infinity
    lowest_cost_node = "Start"

    for node in costs:
        if node not in processed and costs[node] < lowest_cost:
            lowest_cost = costs[node] 
            lowest_cost_node = node
    return lowest_cost_node

#_______________________________________________
#
# Main algorithm
#_______________________________________________

processed = []
parents = {}

while len(processed) < len(graph):
    current_node =  find_lowest_cost_node(graph, processed)
    processed.append(current_node)
    print("Processing ", current_node)

    '''
    current_cost = cost at current_node

    for ....go through all direct neighbors of current_node:
        check their costs and add it to current_cost
        if that new cost is lower than the cost of the neighbor:
            update cost of neighbor with that new cost
        Make current_node parent to neighbor (this will be used to record the best path)
    '''
    
    for n in graph[current_node]:
        new_cost = costs[current_node] + graph[current_node][n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = current_node
        
print (parents)   # parents will end up being the shortest path

path = []
i = "Fin"
while i != "Start":
    path.append(i)
    i = parents[i]

path.append("Start")
path.reverse()

print("__________________________________________________")
for i in range(1,10):
    print(" ")
print("__________________________________________________")
print("Results:  ")
print(" ")
print("Path: ","  ".join(path))
print("__________________________________________________")

        
        

