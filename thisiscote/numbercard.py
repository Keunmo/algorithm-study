n, m = map(int, input().split())
cards = [None for i in range(n)]
# version 1
# for i in range(n):
#     cards[i] = list(map(int, input().split()))
#     cards[i].sort()
# 
# candidates = []
# for i in range(n):
#     candidates.append(cards[i][0])
#
# candidates.sort()
# print(candidates[-1])

# version 2
res = 0
for i in range(n):
    cards = list(map(int, input().split()))
    minval = min(cards)
    res = max(minval, res)

print(res)