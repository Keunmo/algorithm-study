# https://leetcode.com/problems/regular-expression-matching/

import re
def isMatch(s, p):
    p = re.compile(p)
    m = p.fullmatch(s)
    print(m)
    if m:
        print(m)
        return True
    else:
        print("False")
        return False

# isMatch('ab','.*')
# isMatch("mississippi","mis*is*p*.")