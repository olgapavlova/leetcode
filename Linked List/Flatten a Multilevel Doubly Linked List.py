"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pointer = head
        while pointer:
            if pointer.child:
                temp = self.flatten(pointer.child)
                tempTail = temp
                while hasattr(tempTail, 'next') and (tempTail.next):
                    tempTail = tempTail.next
                tempTail.next = pointer.next
                pointer.next = temp
                pointer.child = None
                pointer = tempTail.next

            else:
                temp = pointer.next
                pointer.next = temp
                if hasattr(temp, 'next'): pointer = temp.next
                else: pointer = None
                
        return head
            