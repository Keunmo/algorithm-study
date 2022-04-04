def in_range(y, x):
    if (0 <= y <= 4) and (0 <= x <= 4):
        return True
    else:
        return False


ry = [-1, -1, -1, 0, 0, 1, 1, 1]
rx = [-1, 0, 1, -1, 1, -1, 0, 1]


# hasWord 함수 구현
def has_word(bog, y, x, word):
    # print(bog[y][x])
    if not in_range(y, x):  # not in range
        return False
    if bog[y][x] != word[0]:  # mismatch first char
        return False
    if len(word) == 1:
        return True
    for i in range(8):
        if has_word(bog, y + ry[i], x + rx[i], word[1:]):
            return True
    return False


# 입력 받기
c = int(input())
boggle = [[None for j in range(5)] for i in range(c)]
words = [[] for i in range(c)]
for t in range(c):
    for i in range(5):
        boggle[t][i] = list(input())
    n = int(input())
    for i in range(n):
        words[t].append(input())
# print(boggle)
# print(words)

for t in range(c):
    for word in words[t]:
        flag = False
        for i in range(5):
            for j in range(5):
                if has_word(boggle[t], i, j, word):
                    print(word, 'YES')
                    flag = True
                    break
            if flag:
                break
        if not flag:
            print(word, 'NO')
