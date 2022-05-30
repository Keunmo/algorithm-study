#https://leetcode.com/problems/length-of-last-word/

def lengthOfLastWord(s):
        cnt = 0
        s = s.rstrip()
        sl = list(s)
        sl.insert(0,' ')
        print(sl)
        # if len(sl) == 0:
        #     print(0)
        #     return 0
        # else:
        while sl.pop() != ' ':
            cnt+=1
        print(cnt)
        return cnt

s = 'a '
lengthOfLastWord(s)