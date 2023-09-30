# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next

        part_size, extra = divmod(count, k)

        result = []
        current = head
        prev = None

        for i in range(k):
            result.append(current)

            part_count = part_size + (1 if i < extra else 0)

            for j in range(part_count):
                prev, current = current, current.next

            if prev:
                prev.next = None

        return result