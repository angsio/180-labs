from gomoku import *

def test_detect_row():

    #---------------------------------------------------------------
    # Test Case 1
    board = make_empty_board(8)

    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    if detect_row(board, "w", 0, x, 3, d_y, d_x) == (1,0):
        print("TEST CASE 1 for detect_row PASSED")
    else:
        print("TEST CASE 1 for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 2
    board = make_empty_board(8)

    x = 0; y = 0; d_x = 1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    if detect_row(board, "w", 0, 0, length, d_y, d_x) == (0, 1):
        print("TEST CASE 2 for detect_row PASSED")
    else:
        print("TEST CASE 2 for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 3
    board = make_empty_board(8)

    x = 0; y = 0; d_x = 1; d_y = 1; length = 8
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)

    if detect_row(board, "w", 0, 0, length, d_y, d_x) == (0, 0):
        print("TEST CASE 3 for detect_row PASSED")
    else:
        print("TEST CASE 3 for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 4
    board = make_empty_board(8)

    x = 1; y = 1; d_x = 1; d_y = 1; length = 4
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")

    x = 0; y = 0; d_x = 0; d_y = 1; length = 8
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")

    print_board(board)

    if detect_row(board, "w", 0, 0, 4, 1, 1) == (0, 1):
        print("TEST CASE 4 for detect_row PASSED")
    else:
        print("TEST CASE 4 for detect_row FAILED")

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
        print("TEST CASE 5 for detect_row PASSED")
    else:
        print("TEST CASE 5 for detect_row FAILED")

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
        print("TEST CASE 6 for detect_row PASSED")
    else:
        print("TEST CASE 6 for detect_row FAILED")

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
        print("TEST CASE 7 for detect_row PASSED")
    else:
        print("TEST CASE 7 for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 8
    board = make_empty_board(8)

    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 1, 1, 1, 0, 2, "w")
    put_seq_on_board(board, 4, 1, 1, 0, 3, "w")

    print_board(board)
    # detect_row(board, col, y_start, x_start, length, d_y, d_x)
    if detect_row(board, "w", 0, 1, 2, 1, 0) == (1, 0):
        print("TEST CASE 8 for detect_row PASSED")
    else:
        print("TEST CASE 8 for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 9
    board = make_empty_board(8)

    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 1, 2, 1, 1, 2, "w")
    put_seq_on_board(board, 4, 5, 1, 1, 2, "w")

    print_board(board)
    # detect_row(board, col, y_start, x_start, length, d_y, d_x)
    if detect_row(board, "w", 0, 1, 2, 1, 1) == (2, 0):
        print("TEST CASE 9 for detect_row PASSED")
    else:
        print("TEST CASE 9 for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 10
    board = make_empty_board(8)

    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 0, 1, 1, 1, 2, "w")
    put_seq_on_board(board, 4, 5, 1, 1, 3, "w")

    print_board(board)
    # detect_row(board, col, y_start, x_start, length, d_y, d_x)
    if detect_row(board, "w", 0, 1, 3, 1, 1) == (0, 1):
        print("TEST CASE 10 for detect_row PASSED")
    else:
        print("TEST CASE 10 for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 11
    board = make_empty_board(8)

    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 0, 1, 1, 1, 2, "w")
    put_seq_on_board(board, 4, 5, 1, 1, 3, "w")

    print_board(board)
    # detect_row(board, col, y_start, x_start, length, d_y, d_x)
    if detect_row(board, "w", 0, 1, 2, 1, 1) == (0, 1):
        print("TEST CASE 11 for detect_row PASSED")
    else:
        print("TEST CASE 11 for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 12
    board = make_empty_board(10)

    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 2, 6, 1, -1, 3, "w")
    put_seq_on_board(board, 6, 2, 1, -1, 2, "w")
    put_seq_on_board(board, 5, 3, 1, -1, 1, "b")

    print_board(board)
    # detect_row(board, col, y_start, x_start, length, d_y, d_x)
    if detect_row(board, "w", 0, 8, 3, 1, -1) == (0, 1):
        print("TEST CASE 12 for detect_row PASSED")
    else:
        print("TEST CASE 12 for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 13
    board = make_empty_board(10)

    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 2, 6, 1, -1, 3, "w")
    put_seq_on_board(board, 6, 2, 1, -1, 3, "w")
    put_seq_on_board(board, 5, 3, 1, -1, 1, "b")

    print_board(board)
    # detect_row(board, col, y_start, x_start, length, d_y, d_x)
    if detect_row(board, "w", 0, 8, 3, 1, -1) == (0, 1):
        print("TEST CASE 13 for detect_row PASSED")
    else:
        print("TEST CASE 13 for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 14
    board = make_empty_board(12)

    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 6, 0, 0, 1, 3, "w")
    put_seq_on_board(board, 6, 4, 0, 1, 2, "w")
    put_seq_on_board(board, 6, 7, 0, 1, 3, "w")
    put_seq_on_board(board, 6, 3, 0, 1, 1, "b")

    print_board(board)
    # detect_row(board, col, y_start, x_start, length, d_y, d_x)
    if detect_row(board, "w", 6, 0, 3, 0, 1) == (1, 0):
        print("TEST CASE 14 for detect_row PASSED")
    else:
        print("TEST CASE 14 for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 15
    board = make_empty_board(8)

    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 1, 7, 1, -1, 4, "w")
    

    print_board(board)
    # detect_row(board, col, y_start, x_start, length, d_y, d_x)
    if detect_row(board, "w", 1, 7, 4, 1, -1) == (0, 1):
        print("TEST CASE 15 for detect_row PASSED")
    else:
        print("TEST CASE 15 for detect_row FAILED")

    #---------------------------------------------------------------
    # Test Case 16
    board = make_empty_board(8)

    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 2, 1, 0, 1, 3, "w")
    put_seq_on_board(board, 2, 5, 0, 1, 3, "w")
    put_seq_on_board(board, 1, 4, 1, 0, 3, "b")
    

    print_board(board)
    # detect_row(board, col, y_start, x_start, length, d_y, d_x)
    if detect_row(board, "w", 2, 0, 3, 0, 1) == (0, 1):
        print("TEST CASE 16 for detect_row PASSED")
    else:
        print("TEST CASE 16 for detect_row FAILED")

    #----------------------------------------------------------
    # Test Case 17
    board = make_empty_board(8)

    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 0, 5, 1, -1, 2, "w")
    put_seq_on_board(board, 2, 3, 0, 1, 1, "b")
    put_seq_on_board(board, 3, 2, 1, -1, 2, "w")
    

    print_board(board)
    # detect_row(board, col, y_start, x_start, length, d_y, d_x)
    if detect_row(board, "w", 0, 5, 2, 1, -1) == (0, 1):
        print("TEST CASE 17 for detect_row PASSED")
    else:
        print("TEST CASE 17 for detect_row FAILED")

    #----------------------------------------------------------
    # Test Case 18
    board = make_empty_board(8)

    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 0, 5, 1, -1, 2, "w")
    put_seq_on_board(board, 2, 3, 0, 1, 1, "b")
    put_seq_on_board(board, 3, 2, 1, -1, 2, "w")
    

    print_board(board)
    # detect_row(board, col, y_start, x_start, length, d_y, d_x)
    if detect_row(board, "w_c", 0, 5, 2, 1, -1) == (0, 1, 1):
        print("TEST CASE 188 for detect_row PASSED")
    else:
        print("TEST CASE 18 for detect_row FAILED")

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

    #---------------------------------------------------------------
    # Test Case 9
    board = make_empty_board(8)

    x = 6; y = 3; d_x = -1; d_y = 1; length = 4
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")

    print_board(board)
    
    y_end = 6
    x_end = 3

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE 9 for is_bounded PASSED")
    else:
        print("TEST CASE 9 for is_bounded FAILED")

    #---------------------------------------------------------------
    # Test Case 10
    board = make_empty_board(8)

    x = 4; y = 0; d_x = -1; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    put_seq_on_board(board, 1, 1, 1, 0, 4, "w")

    print_board(board)
    
    y_end = 2
    x_end = 2

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'CLOSED':
        print("TEST CASE 10 for is_bounded PASSED")
    else:
        print("TEST CASE 10 for is_bounded FAILED")

    #---------------------------------------------------------------
    # Test Case 11
    board = make_empty_board(8)
    # put_seq_on_board(board, y, x, d_y, d_x, length, col)
    put_seq_on_board(board, 0, 0, 1, 1, 4, "w")

    print_board(board)
    
    y_end = 4
    x_end = 4

    if is_bounded(board, y_end, x_end, 4, 1, 1) == 'SEMIOPEN':
        print("TEST CASE 11 for is_bounded PASSED")
    else:
        print("TEST CASE 11 for is_bounded FAILED")

    #---------------------------------------------------------------
    # Test Case 12
    board = make_empty_board(8)
    # put_seq_on_board(board, y, x, d_y, d_x, length, col)
    put_seq_on_board(board, 1, 0, 1, 1, 4, "w")

    print_board(board)
    
    y_end = 5
    x_end = 4

    if is_bounded(board, y_end, x_end, 4, 1, 1) == 'SEMIOPEN':
        print("TEST CASE 12 for is_bounded PASSED")
    else:
        print("TEST CASE 12 for is_bounded FAILED")

    #---------------------------------------------------------------
    # Test Case 13
    board = make_empty_board(8)
    # put_seq_on_board(board, y, x, d_y, d_x, length, col)
    put_seq_on_board(board, 0, 3, 1, -1, 4, "w")

    print_board(board)
    
    y_end = 3
    x_end = 0

    if is_bounded(board, y_end, x_end, 4, 1, -1) == 'CLOSED':
        print("TEST CASE 13 for is_bounded PASSED")
    else:
        print("TEST CASE 13 for is_bounded FAILED")

    #---------------------------------------------------------------
    # Test Case 14
    board = make_empty_board(8)
    # put_seq_on_board(board, y, x, d_y, d_x, length, col)
    put_seq_on_board(board, 0, 3, 1, 1, 4, "w")

    print_board(board)
    
    y_end = 3
    x_end = 6

    if is_bounded(board, y_end, x_end, 4, 1, 1) == 'SEMIOPEN':
        print("TEST CASE 14 for is_bounded PASSED")
    else:
        print("TEST CASE 14 for is_bounded FAILED")

def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_detect_rows():
    #---------------------------------------
    # TEST CASE 1
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col, length) == (1,0):
        print("TEST CASE 1 for detect_rows PASSED")
    else:
        print("TEST CASE 1 for detect_rows FAILED")

    #---------------------------------------
    # TEST CASE 2
    board = make_empty_board(8)
    
    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 0, 0, 1, 1, 5, "w")
    put_seq_on_board(board, 0, 1, 1, 1, 5, "w")

    print_board(board)

    if detect_rows(board, "w", 2) == (7,2):
        print("TEST CASE 2 for detect_rows PASSED")
    else:
        print("TEST CASE 2 for detect_rows FAILED")

    #---------------------------------------
    # TEST CASE 3
    board = make_empty_board(8)
    
    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 0, 0, 1, 1, 5, "w")
    put_seq_on_board(board, 0, 1, 1, 1, 5, "w")
    put_seq_on_board(board, 2, 4, 1, 1, 3, "b")

    print_board(board)

    if detect_rows(board, "w", 2) == (3, 6):
        print("TEST CASE 3 for detect_rows PASSED")
    else:
        print("TEST CASE 3 for detect_rows FAILED")

    #---------------------------------------
    # TEST CASE 4
    board = make_empty_board(8)
    
    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 2, 4, 1, -1, 3, "w")
    put_seq_on_board(board, 1, 2, 1, 1, 3, "b")
    put_seq_on_board(board, 2, 5, 1, 0, 2, "w")
    put_seq_on_board(board, 4, 4, 0, 1, 3, "w")

    print_board(board)

    if detect_rows(board, "w", 3) == (4, 0):
        print("TEST CASE 4 for detect_rows PASSED")
    else:
        print("TEST CASE 4 for detect_rows FAILED")

    #---------------------------------------
    # TEST CASE 5
    board = make_empty_board(8)
    
    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 2, 4, 1, -1, 3, "w")
    put_seq_on_board(board, 1, 2, 1, 1, 3, "b")
    put_seq_on_board(board, 2, 5, 1, 0, 2, "w")
    put_seq_on_board(board, 4, 4, 0, 1, 3, "w")

    print_board(board)

    if detect_rows(board, "w", 3) == (4, 0):
        print("TEST CASE 5 for detect_rows PASSED")
    else:
        print("TEST CASE 5 for detect_rows FAILED")

    #---------------------------------------
    # TEST CASE 5
    board = make_empty_board(8)
    
    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 0, 5, 1, 0, 4, "w")
    put_seq_on_board(board, 0, 6, 1, 0, 5, "b")

    print_board(board)

    if detect_rows(board, "b", 5) == (0, 1):
        print("TEST CASE 5 for detect_rows PASSED")
    else:
        print("TEST CASE 5 for detect_rows FAILED")

    #---------------------------------------
    # TEST CASE 6
    board = make_empty_board(8)
    
    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 0, 0, 1, 1, 5, "b")
    put_seq_on_board(board, 5, 5, 1, 1, 2, "w")

    print_board(board)

    if detect_rows(board, "b", 5) == (0, 0):
        print("TEST CASE 6 for detect_rows PASSED")
    else:
        print("TEST CASE 6 for detect_rows FAILED")

    #---------------------------------------
    # TEST CASE 7
    board = make_empty_board(8)
    
    # put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    put_seq_on_board(board, 0, 0, 1, 1, 5, "b")
    put_seq_on_board(board, 5, 5, 1, 1, 2, "w")

    print_board(board)

    if detect_rows(board, "b_c", 5) == (0, 0, 1):
        print("TEST CASE 7 for detect_rows PASSED")
    else:
        print("TEST CASE 7 for detect_rows FAILED")

def test_search_max():
    # ------------------------------------
    # TEST CASE 1
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE 1 for search_max PASSED")
    else:
        print("TEST CASE 1 for search_max FAILED") 

    # ------------------------------------
    # TEST CASE 2
    board = make_empty_board(8)

    # put_seq_on_board(board, y, x, d_y, d_x, length, col)
    put_seq_on_board(board, 1, 1, 1, 1, 4, "b")
    put_seq_on_board(board, 5, 5, 1, 1, 2, "w")

    print_board(board)
    if search_max(board) == (0, 0):
        print("TEST CASE 2 for search_max PASSED")
    else:
        print("TEST CASE 2 for search_max FAILED")

    # ------------------------------------
    # TEST CASE 3
    board = make_empty_board(8)

    # put_seq_on_board(board, y, x, d_y, d_x, length, col)
    put_seq_on_board(board, 1, 1, 1, 1, 4, "b")
    put_seq_on_board(board, 5, 5, 1, 1, 1, "w")
    put_seq_on_board(board, 1, 0, 1, 0, 4, "w")
    put_seq_on_board(board, 5, 0, 1, 1, 1, "b")

    print_board(board)
    if search_max(board) == (0, 0):
        print("TEST CASE 3 for search_max PASSED")
    else:
        print("TEST CASE 3 for search_max FAILED")     
    
def test_score():
    board = make_empty_board(8)
    put_seq_on_board(board, 0, 0, 1, 1, 3, "w")
    print(score(board))

    print_board(board)

if __name__ == '__main__':
    # test_is_empty()
    # test_is_bounded()
    # test_detect_row()
    # test_detect_rows()
    test_search_max()
    # test_score()