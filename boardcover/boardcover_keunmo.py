def print_board(board):
    print("===============")
    for i in range(len(board)):
        print(board[i])


cover_type = [
    [[0, 0], [1, 0], [1, 1]],
    [[0, 0], [0, 1], [1, 0]],
    [[0, 0], [1, 0], [1, 1]],
    [[0, 0], [1, -1], [1, 0]]
]

# board의 y,x를 cover type별로 덮거나 깐다. 잘 덮이면 true, 안덮이면 false 반환.
# opt 1이면 덮고 -1이면 깐다.
def set(y, x, board, type, opt):
    ok = True
    for i in range(3):
        ny = y + cover_type[type][i][0]
        nx = x + cover_type[type][i][1]
        if (ny < 0) or (ny >= len(board)) or (nx < 0) or (nx >= len(board[0])): # 보드 범위 밖이면 false
            ok = False
        else:  # 보드 범위 안이면 덮되, 겹치면 false
            board[ny][nx] += opt
            if board[ny][nx] > 1:
                ok = False
    return ok


# board의 모든 빈 칸을 덮을 수 있는 방법의 수를 반환한다.
def cover(board):
    y = -1
    x = -1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                y = i
                x = j
                break
        if y != -1:
            break
    if y == -1:
        return 1
    # print('y= ', y, 'x= ', x)
    count = 0
    for i in range(4):
        if set(y, x, board, i, 1):
            # print_board(board)
            count += cover(board)
        set(y, x, board, i, -1)
    return count


if __name__ == "__main__":
    # 입력받기
    c = int(input())
    boards = [None for i in range(c)]
    for t in range(c):
        h, w = map(int, input().split(' '))
        boards[t] = [None for i in range(h)]
        for i in range(h):
            boards[t][i] = list(map(int, input().replace('.', '0').replace('#', '1')))

    # 해결하기
    for i in range(c):
        board = boards[i]
        print(cover(board))
