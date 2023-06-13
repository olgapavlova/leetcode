# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        stepone = pointer.next
        while stepone:
            pointer.next = stepone.next
            stepone.next, head = head.next, stepone
            stepone = pointer.next
        return head