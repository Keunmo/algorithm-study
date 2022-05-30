#https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

def numOfSteps(n):
    cnt = 0
    while n!=0:
        if n%2 == 0:
            n = n/2
        else:
            n = n=1
        cnt += 1
    return cnt

numOfSteps(14)