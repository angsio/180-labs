"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Nov. 1, 2023
"""

def is_empty(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] != " ":
                return False
    return True
    
    
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    # 0 is open
    # 1 is semi
    # 2 is closed
    state = 0
    direction = (d_y, d_x)
    if direction == (1, 0):
        if y_end + 1 == len(board) or board[y_end + 1][x_end] != " ":
            state += 1
        if (y_end + 1) - d_y*length == 0 or board[y_end - d_y*length][x_end] != " ":
            state += 1

    elif direction == (0, 1):
        if x_end + 1 == len(board[0]) or board[y_end][x_end + 1] != " ":
            state += 1
        if (x_end + 1) - d_x*length == 0 or board[y_end][x_end - d_x*length] != " ":
            state += 1

    elif direction == (1, 1):
        if y_end + 1 == len(board) or x_end + 1 == len(board[0]) or board[y_end + d_y][x_end + d_x] != " ":
            state += 1
        if y_end + 1 - d_y*length == 0 or x_end + 1 - d_x*length == 0 or board[y_end - length][x_end - length] != " ":
            state += 1
    elif direction == (1, -1):
        if y_end + 1 == len(board) or x_end == 0 or board[y_end + 1][x_end - 1] != " ":
            state += 1
        if y_end + 1 - length == 0 or x_end + 1 + length == len(board[0]) or board[y_end - length][x_end + length] != " ":
            state += 1

    if state == 0:
        return "OPEN"
    elif state == 1:
        return "SEMIOPEN"
    else:
        return "CLOSED"


    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    # available tools: is bounded
    opens, semis = 0, 0

    row = []
    for i in range(len(board)):

        # Checks if out of bounds
        if y_start + i*d_y >= len(board):
            break
        
        elif x_start + i*d_x >= len(board) or x_start + i*d_x == -1:
            break
            
        row.append(board[y_start + i*d_y][x_start + i*d_x])

    # Row is the row to be checked for sequences.
    instances = [0]*len(row)

    chain = False
    for i in range(1, len(row) - length):
        if chain == False and row[i + length] != col and row[i - 1] != col:
            if row[i:i + length] == [col]*length:
                instances[i] = 1
                chain = True
        else:
            if row[i + length - 1] != col:
                chain = False
    
    if row[:length] == [col]*length and row[length] != col:
        instances[0] = 1
    if row[-length:] == [col]*length and row[-length - 1] != col:
        instances[-length] = 1

    # is_bounded(board, y_end, x_end, length, d_y, d_x)
    for i in range(len(instances)):
        if instances[i] == 1:
            y_end = y_start + length*d_y + (i - 1)*d_y
            x_end = x_start + length*d_x + (i - 1)*d_x
            res = is_bounded(board, y_end, x_end, length, d_y, d_x)
            print(res)
            if res == "OPEN":
                opens += 1
            elif res == "SEMIOPEN":
                semis += 1
     
    return (opens, semis)

def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0

    for row in range(len(board)):
        row_counts = detect_row(board, col, row, 0, length, 0, 1)
        open_seq_count += row_counts[0]
        semi_open_seq_count += row_counts[1]
    
    for column in range(len(board[0])):
        row_counts = detect_row(board, col, 0, column, length, 1, 0)
        open_seq_count += row_counts[0]
        semi_open_seq_count += row_counts[1]

    return open_seq_count, semi_open_seq_count
    
def search_max(board):
    return move_y, move_x
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

    
def is_win(board):
    pass


def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    
def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                
def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
    

        
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
