class MyLinkedList:

    def __init__(self):
        pass

    def get(self, index: int) -> int:
        pointer = self
        result = -1
        for i in range(index + 1):
            if hasattr(pointer, 'next'):
                result = pointer.val
                pointer = pointer.next
            else: result = -1
        return result
        
    def addAtHead(self, val: int) -> None:
        pointer = self
        next_val = val
        while hasattr(pointer, 'next'):
            next_val, pointer.val = pointer.val, next_val        
            pointer = pointer.next
        pointer.next = MyLinkedList()
        pointer.val = next_val

    def addAtTail(self, val: int) -> None:
        pointer = self
        while hasattr(pointer, 'next'):
            # print(pointer.next)
            pointer = pointer.next
        pointer.val = val
        pointer.next = MyLinkedList()

    def addAtIndex(self, index: int, val: int) -> None:
        pointer = self
        ins = MyLinkedList()
        ins.val = val
        invalid = False
        for i in range(index-1):
            if hasattr(pointer, 'next'):
                pointer = pointer.next
            else: invalid = True
        if invalid == False:
            ins.next = pointer.next
            pointer.next = ins        

    def deleteAtIndex(self, index: int) -> None:
        pointer = self
        for i in range(index-1):
            if hasattr(pointer, 'next'):
                pointer = pointer.next
        
        if index > 0 and hasattr(pointer, 'next') and hasattr(pointer.next, 'next'):
            # print('$$$', pointer.next.val)
            pointer.next = pointer.next.next
            # print('%%%', pointer.next.val)
            # print('123')
        elif index == 1 and hasattr(pointer, 'next'):
            self.next = MyLinkedList()
            # print('456')
        elif index == 0 and hasattr(pointer, 'next'):
            pointer = self.next
            print('===', id(pointer.next))
            self = pointer
            print('===', id(self))
            print('789')
            print(self.val)
            print('===', id(self))
            print('===', id(myLinkedList))
        else:
            del(self.val)
            del(self.next)
            print('012')


myLinkedList = MyLinkedList()

myLinkedList.addAtHead(1)
""" print(myLinkedList.get(0))
print(myLinkedList.get(1)) """

myLinkedList.addAtTail(3)
""" print(myLinkedList.get(0))
print(myLinkedList.get(1))
print(myLinkedList.get(2)) """

myLinkedList.addAtIndex(1, 2)    # linked list becomes 1->2->3
myLinkedList.get(1)              # return 2
""" print(myLinkedList.get(0))
print(myLinkedList.get(1))
print(myLinkedList.get(2)) """


myLinkedList.deleteAtIndex(0)    # now the linked list is 1->3
myLinkedList.get(1)              # return 3
print(myLinkedList.get(0))
print('===', id(myLinkedList))

# print(myLinkedList.val)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)