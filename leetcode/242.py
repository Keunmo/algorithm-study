# https://leetcode.com/problems/valid-anagram/

def isAnagram(s, t):
    s=list(s)
    t=list(t)
    s.sort()
    t.sort()
    print('s:',s)
    print('t:',t)
    if s == t:
        return True
    else:
        return False

isAnagram("rat","car")