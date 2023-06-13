# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        pointer = head
        while pointer:
            if pointer.next.val == val:
                if hasattr(pointer.next, 'next'):
                    pointer.next = pointer.next.next
                else:
                    pointer.next = None
            pointer = pointer.next

        if head.val == val:
            if head.next == None: head = None
            else: head = head.next