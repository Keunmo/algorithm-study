# c = int(input("c: ")) # test case num
# n_list = []     # friends num
# m_list = []     # pairs num
# pair_list = []  # pairs
# for i in range(c):
#     n_t, m_t = map(int, input("n, m: ").split(' '))
#     n_list.append(int(n_t))
#     m_list.append(int(m_t))
#     pair_list.append(list(map(int, input('friends: ').split(' '))))

# c = int(input("c: ")) # test case num
# n_list = [None for i in range(c)] # friends num
# m_list = [None for i in range(c)] # pairs num
# pair_list = [None for i in range(c)]  # pairs
# for i in range(c):
#     n_list[i], m_list[i] = map(int, input("n, m: ").split(' '))
#     pair_list[i] = list(map(int, input('friends: ').split(' ')))

c = int(input()) # test case num
n_list = [None for i in range(c)] # friends num
m_list = [None for i in range(c)] # pairs num
pair_list = [None for i in range(c)]  # pairs
for i in range(c):
    n_list[i], m_list[i] = map(int, input().split(' '))
    pair_list[i] = list(map(int, input().split(' ')))

# print(c)
# print(n_list)
# print(m_list)
# print(pair_list)


def counting_pairs(taken):
    # print('taken: ', taken)
    first_free = -1
    for i in range(n):
        if not taken[i]:
            first_free = i
            break
    # print('firstFree:', first_free)
    if first_free == -1:
        return 1
    count = 0
    for pairs_with in range(first_free+1, n):
        if not taken[pairs_with] and areFriends[first_free][pairs_with]:
            taken[first_free] = True
            taken[pairs_with] = True
            # print('make pair', first_free, pairs_with)
            count += counting_pairs(taken)
            taken[first_free] = False
            taken[pairs_with] = False
    return count


for t in range(c):
    n = n_list[t]
    m = m_list[t]
    pairs = pair_list[t]
    areFriends = [[False for i in range(n)] for i in range(n)]
    for i in range(len(pairs)//2):
        areFriends[pairs[i*2]][pairs[i*2+1]] = True
        areFriends[pairs[i*2+1]][pairs[i*2]] = True
    taken = [False for i in range(n)]
    print(counting_pairs(taken))

