graph = {}
graph["A"] = ["B", "E"]
graph["E"] = []
graph["B"] = ["C", "D"]
graph["C"] = ["F"]
graph["F"] = []
graph["D"] = ["G", "H"]
graph["G"] = []
graph["H"] = []

stack = ["A"]
path = []
finish = "F"
visited = set()

while stack:
    cell = stack.pop()
    print (cell)
    if cell == finish:
        print ("found it")
    else:
        for neighbor in graph[cell]:
            if neighbor not in visited:  # dead end
                stack.append(neighbor)
'''
def DFS (start, finish, graph, visited = [], path = []):
    search_stack = [start]
    while search_stack:
        print ("search_stack: ", search_stack)
        node = search_stack.pop()
        path.append(node)
        print ("path: ", path)

        if node in visited:
            print ("path: ", path)
            path.pop()
            print ("node ", node, " already visited")
            print ("path: ", path)

        elif node == finish:
            search_stack = []
            print("Path from " , start, " to ", finish, " : ", path)
            return True

        else:
            all_neighbors_visited = True
            for neighbor in graph[node]:
                if neighbor not in visited:
                    all_neighbors_visited = False
                    search_stack.append(neighbor)
            if all_neighbors_visited:
                visited.append(node)
                path.pop()
            


DFS("A", "G", graph, [], [])
print("-----------------------------------------------------")
DFS("A", "F", graph, [], [])
print("-----------------------------------------------------")
DFS("A", "D", graph, [], [])
'''

