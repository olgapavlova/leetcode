class Node():
    """ Элемент связного списка """
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    """ Связный список """
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        pointer = self.head
        allowGet = hasattr(self.head, 'val')
        for i in range(index):
            if hasattr(pointer, 'next'):
                pointer = pointer.next
            else: allowGet = False
        if allowGet:
            if hasattr(pointer, 'val'):
                return pointer.val
            else: return -1
        else:
            return -1
        
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
        pointer = self.head
        if index == 0:
            self.addAtHead(val)
        else:
            position = 0
            allowInsert = True
            for i in range(1, index):
                if hasattr(pointer, 'next') and pointer.next:
                    # print(position, pointer.val)
                    pointer = pointer.next
                    position += 1
                else: allowInsert = False
            # print(position, ' ! ', index)
            if (position < index - 2): allowInsert = False
            if allowInsert:
                if pointer:
                    insNode = Node(val)
                    insNode.next = pointer.next
                    pointer.next = insNode
                else:
                    self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        pass

myLinkedList = MyLinkedList()
myLinkedList.addAtHead(7)
myLinkedList.addAtTail(2)
myLinkedList.addAtHead(5)
myLinkedList.addAtTail(4)
print([myLinkedList.get(i) for i in range(7)])
myLinkedList.addAtIndex(0, 9)
print([myLinkedList.get(i) for i in range(7)])
myLinkedList.addAtIndex(3, 99)
print([myLinkedList.get(i) for i in range(7)])
myLinkedList.addAtIndex(7, 90)
print([myLinkedList.get(i) for i in range(8)])
""" print(myLinkedList.get(0))
print(myLinkedList.get(1))
print(myLinkedList.get(2))
print(myLinkedList.get(3))
print(myLinkedList.get(4)) """

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