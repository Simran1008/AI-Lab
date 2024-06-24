import heapq

# Function to calculate Manhattan distance
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                target_x = (state[i][j] - 1) // 3
                target_y = (state[i][j] - 1) % 3
                distance += abs(i - target_x) + abs(j - target_y)
    return distance


# Function to find the possible moves from a given state
def get_neighbors(state):
    neighbors = []
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= x + dx < 3 and 0 <= y + dy < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[x + dx][y + dy] = new_state[x + dx][y + dy], new_state[x][y]
            neighbors.append(new_state)
    return neighbors


# Best First Search algorithm
def best_first_search(initial_state, goal_state):
    visited = set()
    priority_queue = [(manhattan_distance(initial_state), 0, initial_state)]
    while priority_queue:
        _, moves, current_state = heapq.heappop(priority_queue)
        if current_state == goal_state:
            return moves
        visited.add(tuple(map(tuple, current_state)))
        neighbours = get_neighbors(current_state)
        for neighbor in neighbours:
            if tuple(map(tuple, neighbor)) not in visited:
                heapq.heappush(priority_queue, (manhattan_distance(neighbor), moves + 1, neighbor))


# Function to print the state in a readable format
def print_state(state, heuristic):
    for row in state:
        print(row)
    print("Heuristic value:", heuristic)
    print()


# Input initial state from user
initial_state = [[1, 2, 3],
                 [4, 5, 6],
                 [0, 7, 8]]

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]    

# Solve the puzzle
moves = best_first_search(initial_state, goal_state)

# Print the steps
if moves is None:
    print("No solution exists!")
else:
    print("Solution found in {} moves:".format(moves))
    state = initial_state
    heuristic = manhattan_distance(state)
    print_state(state, heuristic)
    for move in range(moves):
        for neighbor in get_neighbors(state):
            if manhattan_distance(neighbor) + 1 == manhattan_distance(state):
                state = neighbor
                heuristic = manhattan_distance(state)
                break
        print("Move", move + 1)
        print_state(state, heuristic)
