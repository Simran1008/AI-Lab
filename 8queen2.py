# no queens share same row/column/diagonal
# [2,4,7,3,1,0,6,5] : queen in row 2 is placed in column 7 so values rep column and index is row

import random

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if (j+1) == board[i]:
                print(" Q ", end="")
            else:
                print(" __ ",end="")
        print("\n")

def heuristic(chessboard):
    conflicts = 0
    for i in range(len(chessboard)):
        for j in range(i+1, len(chessboard)):
            if chessboard[i] == chessboard[j] or abs(i-j) == abs(chessboard[i] - chessboard[j]):
                conflicts += 1
    return conflicts

def solve_queens(board):
    current_board = board[:]
    current_heuristic = heuristic(board)

    same_state_count=0
    max_same_state_count=3

    print("Initial board", current_board)
    print_board(current_board)
    print("Initial heuristic", current_heuristic)

    while current_heuristic > 0 :
        # randomly select 2 rows to swap positions
        row1, row2 = random.sample(range(1, 9), 2)
        current_board[row1 - 1], current_board[row2 - 1] = current_board[row2 - 1], current_board[row1 - 1]

        new_board_heuristic = heuristic(current_board)

        if new_board_heuristic < current_heuristic:
            current_heuristic = new_board_heuristic
            same_state_count = 0
            print("Current board: ", current_board)
            print_board(current_board)
            print("Current heuristic: ", current_heuristic)

        else:
            current_board[row1 - 1], current_board[row2 - 1] = current_board[row2 - 1], current_board[row1 - 1]
            same_state_count +=1

        if same_state_count >= max_same_state_count:
            row1, row2 = random.sample(range(1, 9), 2)
            current_board[row1 - 1], current_board[row2 - 1] = current_board[row2 - 1], current_board[row1 - 1]
            same_state_count = 0

    print("Solution found!")
    print("Final board: ", current_board)
    print_board(current_board)
    print("Final heuristic: ", current_heuristic)

initial_board = []
t=8
print("Initial Board")

while t:
    inp = int(input())
    initial_board.append(inp) # input column
    t -=1
solve_queens(initial_board)