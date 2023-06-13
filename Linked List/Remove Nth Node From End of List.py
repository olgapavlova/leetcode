# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = head
        enum = []
        while pointer:
            enum.append(pointer)
            pointer = pointer.next
        enum[-n-1].next = enum[-n+1]
        return head