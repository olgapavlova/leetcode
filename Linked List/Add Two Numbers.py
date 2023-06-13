# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def listToNumber(l: ListNode):
            result = 0
            decimal = 1
            pointer = l
            while pointer:
                result += pointer.val * decimal
                decimal *= 10
                pointer = pointer.next
            return result
        
        sum = listToNumber(l1) + listToNumber(l2)
        digit = sum % 10
        sum = sum // 10

        result = ListNode(digit)
        pointer = result
        while sum > 0:
            digit = sum % 10
            sum = sum // 10
            pointer.next = ListNode(digit)
            pointer = pointer.next
        return result


