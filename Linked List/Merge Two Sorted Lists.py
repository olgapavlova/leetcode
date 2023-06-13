# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = list1
        pointer2 = list2
        pointerResult = None

        if hasattr(pointer1, 'val') and hasattr(pointer2, 'val'):
            if pointer1.val > pointer2.val:
                pointerResult = ListNode(pointer2.val)
                pointer2 = pointer2.next
            else:
                pointerResult = ListNode(pointer1.val)
                pointer1 = pointer1.next

            result = pointerResult

            while pointer1 or pointer2:
                if hasattr(pointer1, 'val') and hasattr(pointer2, 'val'):
                    if pointer1.val > pointer2.val:
                        pointerResult.next = ListNode(pointer2.val)
                        pointer2 = pointer2.next
                    else:
                        pointerResult.next = ListNode(pointer1.val)
                        pointer1 = pointer1.next
                elif hasattr(pointer1, 'val'):
                    pointerResult.next = ListNode(pointer1.val)
                    pointer1 = pointer1.next
                elif hasattr(pointer2, 'val'):
                    pointerResult.next = ListNode(pointer2.val)
                    pointer2 = pointer2.next
                else: pass

            pointerResult = pointerResult.next

        elif hasattr(pointer1, 'val'):
            return pointer1

        elif hasattr(pointer2, 'val'):
            return pointer2

        else: return None
             
        return result

