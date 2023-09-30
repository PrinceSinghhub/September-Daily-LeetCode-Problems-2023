# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        prev = dummy = ListNode(0, head)

        for i in range(left - 1):
            prev = prev.next
        curr = prev.next

        for i in range(right - left):
            tmp = prev.next
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = tmp
        return dummy.next