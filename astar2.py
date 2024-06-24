import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.heuristic = {}

    def add_node(self, value, heuristic): 
        self.nodes.add(value)
        self.heuristic[value] = heuristic

    def add_edge(self, from_node, to_node, cost):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, cost))

    def get_neighbors(self, node):
        if node in self.edges:
            return self.edges[node]
        else:
            return []

    def a_star(self, start, goal):
        frontier = [(0, start)]
        came_from = {}
        cost_so_far = {start: 0}

        while frontier:
            current_cost, current_node = heapq.heappop(frontier)

            if current_node == goal:
                path = []
                while current_node in came_from:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.append(start)
                path.reverse()

                # Calculate total cost
                total_cost = 0
                for i in range(len(path) - 1):
                    total_cost += self.get_cost(path[i], path[i+1])

                return path, total_cost

            for neighbor, cost in self.get_neighbors(current_node):
                new_cost = cost_so_far[current_node] + cost
                if neighbor not in cost_so_far:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self.heuristic[neighbor]
                    heapq.heappush(frontier, (priority, neighbor))
                    came_from[neighbor] = current_node

        return None, None

    def get_cost(self, from_node, to_node):
        for neighbor, cost in self.edges[from_node]:
            if neighbor == to_node:
                return cost
        return None


graph = Graph()
graph.add_node('S', heuristic=18.5)
graph.add_node('A', heuristic=10.5)
graph.add_node('B', heuristic=6)
graph.add_node('C', heuristic=9.2)
graph.add_node('D', heuristic=6.2)
graph.add_node('E', heuristic=4.5)
graph.add_node('F', heuristic=20)
graph.add_node('G', heuristic=0)

graph.add_edge('S', 'A', 3)
graph.add_edge('S', 'C', 4)
graph.add_edge('A', 'C', 5)
graph.add_edge('A', 'B', 4)
graph.add_edge('C', 'D', 3)
graph.add_edge('B', 'D', 4)
graph.add_edge('B', 'F', 4)
graph.add_edge('B', 'G', 5)
graph.add_edge('D', 'E', 2)
graph.add_edge('E', 'G', 3)


start_node = 'S'
goal_node = 'G'

path, total_cost = graph.a_star(start_node, goal_node)
if path:
    print(" -> ".join(path))
    print("Total Cost:", total_cost)
else:
    print("No path found")