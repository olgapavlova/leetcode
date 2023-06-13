# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head
        while hasattr(p1, 'next'):
            if hasattr(p2, 'next') and hasattr(p2.next, 'next'):
                p2 = p2.next.next
            else: return False

            p1 = p1.next

            if (p1 is None) or (p2 is None): return False

            if (p1 == p2): return True
        return False