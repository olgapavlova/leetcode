class MyLinkedList:

    def __init__(self):
        self.val = None
        self.next = None

    def get(self, index: int) -> int:
        temp = self.next
        for i in range(index):
            if temp: temp = temp.next
        return temp.val
        

    def addAtHead(self, val: int) -> None:
        first = MyLinkedList()
        first.val = val
        first.next = self
        self.next = first
        
    def addAtTail(self, val: int) -> None:
        pointer = self
        end = MyLinkedList()
        end.val = val
        while pointer.next:
            pointer = pointer.next
        pointer.next = end

    def addAtIndex(self, index: int, val: int) -> None:
        pointer = self
        ins = MyLinkedList
        ins.val = val
        for i in range(index):
            if pointer.next: pointer = pointer.next
        ins.next = pointer.next
        pointer.next = ins        

    def deleteAtIndex(self, index: int) -> None:
        pointer = self
        for i in range(index):
            if pointer.next: pointer = pointer.next
        pointer.next = pointer.next.next        


myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
print(myLinkedList.next.next.next.val)
""" myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)    # linked list becomes 1->2->3
myLinkedList.get(1)              # return 2
myLinkedList.deleteAtIndex(1)    # now the linked list is 1->3
myLinkedList.get(1)              # return 3
 """
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)