n = int(input())
pathplan = list(input().split())

# sol 1
# loc_x = 1
# loc_y = 1
# for path in pathplan:
#     if path == 'L':
#         next_y = loc_y - 1
#         next_x = loc_x
#     if path == 'R':
#         next_y = loc_y + 1
#         next_x = loc_x
#     if path == 'U':
#         next_y = loc_y
#         next_x = loc_x - 1
#     if path == 'D':
#         next_y = loc_y
#         next_x = loc_x + 1
#
#     if (1 <= next_x <= n) and (1 <= next_y <= n):
#         loc_x, loc_y = next_x, next_y
#
# print(loc_x, loc_y)

# sol 2
x, y = 1, 1
# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
types = ['L', 'R', 'U', 'D']

for path in pathplan:
    nx, ny = x+dx[types.index(path)], y+dy[types.index(path)]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        pass
    else:
        x, y = nx, ny

print(x, y)
