# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        trace = {}
        pointer = head
        num = 0
        result = None
        while pointer:
            i = id(pointer)
            if getattr(trace, i, None):
                result = trace[id]
                break
            else:
                trace[i] = num
                pointer = pointer.next
                num += 1
        return result