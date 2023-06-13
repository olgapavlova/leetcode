# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointerA = headA
        pointerB = headB
        ids = set([])
        result = None

        while (pointerA is not None) and (pointerB is not None):
            if id(pointerA) in ids:
                result = pointerA
            else: ids.add(id(pointerA))
            if id(pointerB) in ids:
                result = pointerB
            else: ids.add(id(pointerB))
            pointerA = pointerA.next
            pointerB = pointerB.next
        
        return result
            