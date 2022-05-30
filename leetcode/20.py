# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i=='('or i=='{'or i=='[':
                stack.append(i)
            if i == ')':
                if len(stack) == 0:
                    return False
                elif stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            if i == '}':
                if len(stack) == 0:
                    return False
                elif stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            if i == ']':
                if len(stack) == 0:
                    return False
                elif stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

s = input()
stack = []
for i in s:
    if i=='('or i=='{'or i=='[':
        print("pass if. i:",i)
        stack.append(i)
    print("i:",i)
    print("stack0:",stack)
    if i == ')':
        print("detack )")
        if len(stack) == 0:
            print("False")
            break
        elif stack[-1] == '(':
            stack.pop()
            print("stack1:",stack)
        else:
            # stack.append(i)
            print("False")
            break
    if i == '}':
        print("detack }")
        if len(stack) == 0:
            print("False")
            break
        elif stack[-1] == '{':
            stack.pop()
            print("stack1:",stack)
        else:
            # stack.append(i)
            print("False")
            break
    if i == ']':
        print("detack ]")
        if len(stack) == 0:
            print("False")
            break
        elif stack[-1] == '[':
            stack.pop()
            print("stack1:",stack)
        else:
            # stack.append(i)
            print("False")
            break
    print("stack4:",stack)
if len(stack) == 0:
    print("True")
else:
    print("False")