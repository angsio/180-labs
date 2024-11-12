from gomoku import *

def test_detect_row():

    #---------------------------------------------------------------
    # Test Case 1
    board = make_empty_board(8)

    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    if detect_row(board, "w", 0, x, length, d_y, d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 2
    board = make_empty_board(8)

    x = 0; y = 0; d_x = 1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    if detect_row(board, "w", 0, 0, length, d_y, d_x) == (0, 1):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 3
    board = make_empty_board(8)

    x = 0; y = 0; d_x = 1; d_y = 1; length = 8
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)

    if detect_row(board, "w", 0, 0, length, d_y, d_x) == (0, 0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 4
    board = make_empty_board(8)

    x = 1; y = 1; d_x = 1; d_y = 1; length = 4
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")

    x = 0; y = 0; d_x = 0; d_y = 1; length = 8
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")

    print_board(board)

    if detect_row(board, "w", 0, 0, 4, 1, 1) == (0, 1):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 5
    board = make_empty_board(8)

    x = 1; y = 1; d_x = 1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")

    x = 5; y = 5; d_x = 1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")

    x = 0; y = 0; d_x = 0; d_y = 1; length = 8
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")

    x = 4; y = 0; d_x = 0; d_y = 1; length = 8
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")

    print_board(board)

    if detect_row(board, "w", 0, 0, 4, 1, 1) == (0, 0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 6
    board = make_empty_board(8)

    x = 1; y = 1; d_x = 1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")

    x = 5; y = 5; d_x = 1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")

    x = 0; y = 0; d_x = 0; d_y = 1; length = 8
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")

    print_board(board)

    if detect_row(board, "w", 0, 0, 3, 1, 1) == (0, 2):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 7
    board = make_empty_board(8)

    x = 1; y = 1; d_x = 1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")

    x = 5; y = 5; d_x = 1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")

    x = 0; y = 1; d_x = 0; d_y = 1; length = 7
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")

    print_board(board)

    if detect_row(board, "w", 0, 0, 3, 1, 1) == (1, 1):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_is_bounded():
    # Test case 1
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

    #---------------------------------------------------------------
    # Test Case 2
    board = make_empty_board(8)
    x = 0; y = 0; d_x = 1; d_y = 0; length = 5
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 0
    x_end = 4

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

    #---------------------------------------------------------------
    # Test Case 3
    board = make_empty_board(8)
    x = 0; y = 0; d_x = 1; d_y = 0; length = 8
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 0
    x_end = 7

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")
    
    #---------------------------------------------------------------
    # Test Case 4
    board = make_empty_board(8)
    x = 1; y = 0; d_x = 1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 2
    x_end = 3

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

    #---------------------------------------------------------------
    # Test Case 4
    board = make_empty_board(8)
    x = 1; y = 0; d_x = 1; d_y = 1; length = 7
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 6
    x_end = 7

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")
    
    #---------------------------------------------------------------
    # Test Case 5
    board = make_empty_board(8)
    x = 3; y = 2; d_x = -1; d_y = 1; length = 4
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 5
    x_end = 0

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

    #---------------------------------------------------------------
    # Test Case 6
    board = make_empty_board(8)
    x = 0; y = 0; d_x = 1; d_y = 1; length = 8
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 7
    x_end = 7

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")
    
    #---------------------------------------------------------------
    # Test Case 7
    board = make_empty_board(8)
    x = 0; y = 0; d_x = 1; d_y = 1; length = 7
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 7, 7, d_y, d_x, 1, "b")
    print_board(board)
    
    y_end = 6
    x_end = 6

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

    #---------------------------------------------------------------
    # Test Case 8
    board = make_empty_board(8)

    x = 0; y = 0; d_x = 0; d_y = 1; length = 6
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")

    x = 1; y = 3; d_x = 1; d_y = 1; length = 4
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")

    print_board(board)
    
    y_end = 6
    x_end = 4

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'SEMIOPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

if __name__ == '__main__':
    test_is_empty()
    test_is_bounded()
    test_detect_row()