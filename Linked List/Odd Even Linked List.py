# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointerOdd = head
        if head.next:
            pointerEven = head.next
        else: return head

        while pointerEven:
            if hasattr(pointerEven, 'next'):
                temp = pointerEven.next
                pointerEven.next = temp.next
                pointerEven = pointerEven.next

                temp.next = pointerOdd.next
                pointerOdd.next = temp
                pointerOdd = temp
        
        return head
            
