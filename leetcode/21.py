# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        head = ListNode()
        head.next = result
        while l1 != None and l2 != None:
            if l1.val<=l2.val:
                result.next=l1
                result=result.next
                l1=l1.next
            else:
                result.next=l2
                result=result.next
                l2=l2.next
        if l1 == None:
            result.next=l2
        if l2 == None:
            result.next=l1
        head=head.next
        head=head.next
        return head