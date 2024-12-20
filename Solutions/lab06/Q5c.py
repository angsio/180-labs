'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random
def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

def find_coord(square_num):
    row = (square_num - 1) // 3
    column = (square_num - 1) % 3
    coord = [row, column]
    return coord

def put_in_board(board, mark, square_num):
    coord = find_coord(square_num)
    board[coord[0]][coord[1]] = mark
    
def get_free_squares(board):
    free_squares = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                free_squares.append([i, j])
    return free_squares

def make_random_move(board, mark):
    free = get_free_squares(board)
    chosen = random.randint(0, len(free) - 1)
    move = free[chosen]
    board[move[0]][move[1]] = mark

def valid(board, move):
    if move not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        return False
    else:
        move = int(move)
        coord = find_coord(move)
        if coord not in get_free_squares(board):
            return False
        else:
            return True

def check_winner(board):
    # ROWS
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # COLUMNS
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # DIAGONALS
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    
    return None

if __name__ == '__main__':
    board = make_empty_board()
    for i in range(4):
        # Computer goes first
        make_random_move(board, "O")
        print_board_and_legend(board)
        # Check if computer wins
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins.")
            break

        # User goes second
        move = input("Enter a move: ")
        while not valid(board, move):
            print("Invalid input.")
            move = input("Enter a move: ")
        put_in_board(board, "X", int(move))
        # Check if user wins
        print_board_and_legend(board)
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins.")
            break

    # If no winner yet, let the computer make one final move
    if not winner:
        make_random_move(board, "O")
        print_board_and_legend(board)
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins.")
        else:
            print("Tie.")
