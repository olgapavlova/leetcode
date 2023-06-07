class Node():
    """ Элемент связного списка """
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    """ Связный список """
    def __init__(self):
        self.head = None

    def shift(self, index: int):
        pointer = self.head
        for i in range(index):
            if hasattr(pointer, 'next') and pointer.next:
                pointer = pointer.next
            else: return -1
        return pointer

    def get(self, index: int) -> int:
        pointer = self.shift(index)
        if hasattr(pointer, 'val'):
            return pointer.val
        else: return -1
        
    def addAtHead(self, val: int) -> None:
        first = self.head
        self.head = Node(val)
        self.head.next = first

    def addAtTail(self, val: int) -> None:
        pointer = self.head
        if self.head is None:
            self.head = Node(val)
        else:
            while hasattr(pointer, 'next') and pointer.next:
                pointer = pointer.next
            pointer.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            pointer = self.shift(index-1)
            if hasattr(pointer, 'next'):
                nextPointer = pointer.next
                pointer.next = Node(val)
                pointer.next.next = nextPointer
            elif pointer is None:
                pointer = Node(val)
            elif pointer != -1:
                pointer.next = Node(val)
            else: pass

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if hasattr(self.head, 'next'):
                self.head = self.head.next
            else: self.head = None
        else:
            pointer = self.shift(index-1)
            if hasattr(pointer, 'next') and hasattr (pointer.next, 'next'):
                pointer.next = pointer.next.next
            elif pointer is None:
                pass
            elif pointer != -1:
                pointer.next = None
            else: pass




myLinkedList = MyLinkedList()
myLinkedList.addAtHead(7)
myLinkedList.addAtTail(2)
myLinkedList.addAtHead(5)
myLinkedList.addAtTail(4)
print([myLinkedList.get(i) for i in range(9)])
myLinkedList.addAtIndex(1, 0)
print([myLinkedList.get(i) for i in range(9)])
myLinkedList.addAtIndex(0, 7)
print([myLinkedList.get(i) for i in range(9)])
myLinkedList.addAtIndex(0, 9)
print([myLinkedList.get(i) for i in range(9)])
myLinkedList.addAtIndex(3, 11)
print([myLinkedList.get(i) for i in range(9)])
myLinkedList.deleteAtIndex(0)
print([myLinkedList.get(i) for i in range(8)])
myLinkedList.deleteAtIndex(6)
print([myLinkedList.get(i) for i in range(8)])
myLinkedList.deleteAtIndex(3)
print([myLinkedList.get(i) for i in range(8)])
myLinkedList.deleteAtIndex(0)
myLinkedList.deleteAtIndex(0)
myLinkedList.deleteAtIndex(0)
myLinkedList.deleteAtIndex(0)
myLinkedList.deleteAtIndex(0)
myLinkedList.deleteAtIndex(0)
print([myLinkedList.get(i) for i in range(8)])

""" two = Node(5)
myLinkedList.head.next = two
print(myLinkedList.get(0))
print(myLinkedList.get(2))
 """


""" myLinkedList.addAtHead(1)
print(myLinkedList.get(0))
print(myLinkedList.get(1)) """

""" myLinkedList.addAtTail(3)
print(myLinkedList.get(0))
print(myLinkedList.get(1))
print(myLinkedList.get(2)) """

""" myLinkedList.addAtIndex(1, 2)    # linked list becomes 1->2->3
myLinkedList.get(1)              # return 2
print(myLinkedList.get(0))
print(myLinkedList.get(1))
print(myLinkedList.get(2)) """


""" myLinkedList.deleteAtIndex(0)    # now the linked list is 1->3
myLinkedList.get(1)              # return 3
print(myLinkedList.get(0))
print('===', id(myLinkedList))
 """
# print(myLinkedList.val)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)