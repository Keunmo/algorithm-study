def toScan1(nowRC): #모서리인지 검사
    if (0 < nowRC[0] < 4):
        if (0 < nowRC[1] < 4):
            return [0, 1, 2, 3, 4, 5, 6, 7]
        elif(nowRC[1] == 0):
            return [1, 2, 4, 6, 7]
        else: #nowRC[1] == 4
            return [0, 1, 3, 5, 6]
    elif(nowRC[0] == 0):
        if (0 < nowRC[1] < 4):
            return [3, 4, 5, 6, 7]
        elif (nowRC[1] == 0):
            return [4, 6, 7]
        else:  # nowRC[1] == 4
            return [3, 5, 6]
    else: #nowRC[0] == 4
        if (0 < nowRC[1] < 4):
            return [0, 1, 2, 3, 4]
        elif (nowRC[1] == 0):
            return [1, 2, 4]
        else:  # nowRC[1] == 4
            return [0, 1, 3]


def first_search(board, a): #보드, 알파벳
    abc = []
    for i in range(5):
        for j in range(5):
            if(board[i][j] == a):
                abc.append([i, j])
    return abc

def search(board, nowRC, word): #보드, 지금 좌표, 다음 글자
    toScan = toScan1(nowRC)
    for i in toScan:
        RC = []
        if(i == 0):
            RC.append(nowRC[0]-1)
            RC.append(nowRC[1]-1)
        elif(i == 1):
            RC.append(nowRC[0]-1)
            RC.append(nowRC[1])
        elif(i == 2):
            RC.append(nowRC[0]-1)
            RC.append(nowRC[1]+1)
        elif(i == 3):
            RC.append(nowRC[0])
            RC.append(nowRC[1]-1)
        elif(i == 4):
            RC.append(nowRC[0])
            RC.append(nowRC[1]+1)
        elif(i == 5):
            RC.append(nowRC[0] + 1)
            RC.append(nowRC[1] - 1)
        elif(i == 6):
            RC.append(nowRC[0] + 1)
            RC.append(nowRC[1])
        elif(i == 7):
            RC.append(nowRC[0] + 1)
            RC.append(nowRC[1] + 1)


        if(board[RC[0]][RC[1]] == word[0]):

            if(len(word)>1):
                return search(board, RC, word[1:])
            elif(len(word) == 1):
                return True

    return False


C = int(input())
board = []
preRC = []
for i in range(5):
    tmp = input()
    board.append([])
    for j in range(5):
        board[i].append(tmp[j])

for w in range(C):
    N = int(input())
    word = []
    for i in range(N):
        tmp = input()
        word.append([])
        for j in range(len(tmp)):
            word[i].append(tmp[j])

    for i in range(N):
        head = first_search(board, word[i][0])
        exist = 0
        for j in head:
            if(search(board,j,word[i][1:])):
                exist = 1

        for k in range(len(word[i])):
            print(word[i][k], end="")
        print(end=" ")
        if(exist == 1):
            print("YES")
        else:
            print("NO")

