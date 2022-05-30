# https://leetcode.com/problems/arranging-coins/

def arrangeCoins(n):
    if n == 0:
        return 0
    num = n
    for i in range(n):
        num = num-(i+1)
        print("i+1:",i+1, " num:", num)
        if num < i+2:
            print("ans:",i+1)
            return i+1

arrangeCoins(1)