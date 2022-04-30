def compute_square(board, a, end_board, high_square):
    left = 1
    right = 1
    width = 1
    if(high_square >= board[a]*end_board):
        return 0
    while(a-left>=0):
        if(board[a-left] >= board[a]):
            left += 1
            width += 1
        else:
            break
    while(a+right<end_board):
        if(board[a+right] >= board[a]):
            right += 1
            width += 1
        else:
            break

    return board[a]*width

max_square = 0
asd = []
C = int(input())

for i in range(C):
    board_num = int(input())
    board = input().split()
    for j in range(board_num):
        board[j] = int(board[j])
    high_square = 0
    for j in range(board_num):
        a = compute_square(board, j, board_num, high_square)
        if(a>high_square):
            high_square = a
    asd.append(high_square)

for i in range(C):
    print(asd[i])