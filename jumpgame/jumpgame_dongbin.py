board = []
OX = 0
memo = []

def jump(row, col, n):
    global board
    global OX
    global memo
    now = board[row][col]
    if(OX == 1):
        return 0
    if(now == 0):
        OX = 1
        return 0
    else:
        if (row + now < n and not col in memo[row+now]):
            memo[row+now].append(col)
            jump(row + now, col, n)
        if (col + now < n and not col+now in memo[row]):
            memo[row].append(col+now)
            jump(row, col + now, n)

C=int(input())

for i in range(C):
    board = []
    OX = 0
    memo = []
    n = int(input())
    for j in range(n):
        board.append([])
        tmp = input().split()
        memo.append([])
        for w in range(n):
            board[j].append(int(tmp[w]))


    jump(0, 0, n)
    if(OX == 1):
        print("YES")
    else:
        print("NO")