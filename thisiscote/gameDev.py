# better sol
n, m = map(int, input().split())
a, b, d = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

d_left = [(0,-1), (-1,0), (0,1), (1,0)]
d_back = [(-1,0), (0,-1), (1,0), (0,1)]

visited = [[False]*m for _ in range(n)]
visited[a][b] = True


def in_board(a, b):
    if (0<=a<=n) and (0<=b<=m):
        return True
    else:
        return False


step = 1
no_way_cnt = 0

while(True):
    print('pos:', a, b)
    left_a = a + d_left[d][0]
    left_b = b + d_left[d][1]
    if in_board(left_a, left_b) and (board[left_a][left_b]==0) and (not visited[left_a][left_b]):
        d = (d-1) % 4
        a, b = left_a, left_b
        visited[a][b] = True
        step += 1
        no_way_cnt = 0
        pass

    else:
        d = (d-1) % 4
        no_way_cnt += 1
    
    if no_way_cnt == 4:
        na, nb = a+d_back[d][0], b+d_back[d][1]
        if board[na][nb] == 1:
            break
        else:
            a, b = na, nb    

print(step)


# my first sol
n, m = map(int, input().split())
a, b, d = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

d_left = [(0,-1), (-1,0), (0,1), (1,0)]
d_back = [(-1,0), (0,-1), (1,0), (0,1)]

visited = [[False]*m for _ in range(n)]
visited[a][b] = True


def in_board(a, b):
    if (0<=a<=n) and (0<=b<=m):
        return True
    else:
        return False

def no_way_to_go(a, b): # check 4 directions and check if new step available
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    chk = 0
    for dir in dirs:
        na, nb = a+dir[0], b+dir[1]
        if in_board(na, nb):
            if visited[na][nb] or (board[na][nb] == 1):
                chk += 1
    if chk == 4:
        return True
    else:
        return False

step = 1

while(True):
    left_a = a + d_left[d][0]
    left_b = b + d_left[d][1]
    if no_way_to_go(a, b):
        na, nb = a+d_back[d][0], b+d_back[d][1]
        if board[na][nb] == 1:
            break
        else:
            a, b = na, nb
            step += 1
            pass

    elif in_board(left_a, left_b) and (board[left_a][left_b]==0) and (not visited[left_a][left_b]):
        d = (d-1) % 4
        a, b = left_a, left_b
        visited[a][b] = True
        step += 1
        pass

    else:
        d = (d-1) % 4

print(step)