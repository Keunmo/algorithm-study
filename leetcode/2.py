# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add = 0
        carry = 0
        result = ListNode()
        head = ListNode()
        head.next = result
        while l1 != None or l2 != None:
            if l1 == None:
                l1val = 0
            else:
                l1val = l1.val
            if l2 == None:
                l2val = 0
            else:
                l2val = l2.val
            add = l1val + l2val + carry
            carry = add // 10
            result.next = ListNode(add%10)
            result = result.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if carry > 0:
            result.next = ListNode(carry)
        head = head.next.next
        return head