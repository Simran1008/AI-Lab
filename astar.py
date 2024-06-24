from math import inf



def astar(graph, heuristic, start, goal):
    print("A* traveral:")
    open = []
    closed = []
    parent = {}
    shortestPathLength = {}
    F = {} # f = h+g = heuristic + currentShortestPathLength
    shortestPathLength[start] = 0
    F[start] = heuristic[start] + shortestPathLength[start]
    #(node, f=h+g, g)                 
    open.append(start)
    def print_node(node):
        print(f" ({node}, {parent.get(node, "NIL")}, {F.get(node, inf)}, {shortestPathLength.get(node, inf)})", end=" ")
    def propogateUpdate(node):
        current_g = shortestPathLength[node]

        for next_node, next_edge_weight in graph[node]:
            newLength = current_g + next_edge_weight
            newF = heuristic[next_node] + newLength
            if newF < F.get(next_node, inf):
               shortestPathLength[next_node] = newLength
               F[next_node] = newF
               parent[next_node] = current
               propogateUpdate(next_node)

    while len(open) != 0:
        current = open.pop(0)
        closed.append(current)
        current_g = shortestPathLength[current]
        print_node(current)
        print()
        if current == goal:
            return (True, parent)
        for next_node, next_edge_weight in graph[current]:
            if (next_node not in open) and (next_node not in closed):
                # print(next_node, next_edge_weight)

                shortestPathLength[next_node] = current_g + next_edge_weight
                # print(shortestPathLength[next_node])
                # print("F= ",F,"\nH= ", heuristic,"\nG= ", shortestPathLength)
                F[next_node] = heuristic[next_node] + shortestPathLength[next_node] 
                # print(F[next_node])
                # print("_______________")
                parent[next_node] = current
                open.append(next_node)
            elif (next_node in closed) or (next_node in open):
                newLength = current_g + next_edge_weight
                newF = heuristic[next_node] + newLength
                if newF < F[next_node]:
                   shortestPathLength[next_node] = newLength
                   F[next_node] = newF
                   parent[next_node] = current
                   propogateUpdate(next_node)

                
        open.sort(key=lambda x: F[x])
    return (False, parent)
    
        
 
def path(current, parent, start):
    if current == start:
        print(current, end="")
        return
    elif current not in parent:
        return
    else:
        path(parent[current], parent, start)
        print("->" + str(current), end="")               

                                                                                                    



graph = {
    'S' : [("A", 3), ("C", 4)],
    'A' : [("S", 3), ("C", 5), ("B", 4)],
    'C' : [("S", 4), ("A", 5), ("D", 3)],
    'B' : [("D", 4), ("G", 5), ("F", 4)],
    'D' : [("B", 4), ("E", 2), ("C", 3)],
    'E' : [("D", 2), ("G", 3)],
    'G' : [("B", 5), ("E", 3)],
    'F' : [("B", 4)]
}
heuristic = {
'S' : 18.5,
'A' : 10.5,
'C' : 9.2,
'B' : 6,
'D' : 6.2,
'E' : 4.5,
'G' : 0,
'F' : inf,
}


start = 'S'
final = 'G'

(found, parent_dict) = astar(graph, heuristic, start, final)
if found == True:
    print("\nPath from start to finish state")
    for f in final:
        path(f, parent_dict, start)
        print()
else:
    print("Path not found")

# print(graph)
# print(heuristic)

