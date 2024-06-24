import random

def initial_state(n):
    return [random.randint(0, n-1) for _ in range(n)]


def draw_state_with_conflicts(state, conflicts_count):
    n = len(state)
    for i in range(n):
        print("|", end="")
        for j in range(n):
            if j == state[i]:
                print("Q|", end="")
            else:
                print("_|", end="")
        print()
    print("Conflicts:", conflicts_count)
    print()


def conflicts(state):
    n = len(state)
    conflict_count = 0
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflict_count += 1
    return conflict_count


def get_user_input(n):
    print("Enter the initial positions of the queens (0-indexed) separated by spaces:")
    while True:
        try:
            positions = list(map(int, input().split()))
            if len(positions) != n:
                print(f"Please enter exactly {n} positions.")
                continue
            if any(pos < 0 or pos >= n for pos in positions):
                print("Positions must be between 0 and", n - 1)
                continue
            return positions
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")


def best_first_nqueens(n):
    start_state = get_user_input(n)
    queue = [(conflicts(start_state), start_state)]
    visited_states = set()
    count = 0
    while queue:
        queue.sort()
        current_conflicts, current_state = queue.pop(0)
        count += 1
        print("step:", count)
        draw_state_with_conflicts(current_state, current_conflicts)
        if current_conflicts == 0:
            print("Solution Obtained!")
            return
        visited_states.add(tuple(current_state))
        for i in range(n):
            for j in range(n):
                if j != current_state[i]:
                    new_state = list(current_state)
                    new_state[i] = j
                    if tuple(new_state) not in visited_states:
                        new_conflicts = conflicts(new_state)
                        queue.append((new_conflicts, new_state))
    print("Solution not found")

    
# Example usage
best_first_nqueens(8)
