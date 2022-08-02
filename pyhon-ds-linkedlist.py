
from unittest.mock import NonCallableMagicMock


class Node:
    def __init__(self, data) -> None:
        self.val = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.count = 0
        self.head = None
        self.tail = None
    
    def traverse(self):
        curr = self.head

        while curr is not None:
            print(curr.val)
            curr = curr.next
        
    def insert(self, value, index):
        newNode = Node(value)
        
        if index > self.count or index <0:
            return None 
        elif index == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            count = 1
            curr = self.head
            while count < index:
                count +=  1
                curr = curr.next
            
            newNode.next = curr.next
            curr.next = newNode
            self.count += 1

    # method to delete at particular position
    def delete(self, index):
        curr = self.head
        prev = self.head

        if index > self.count or index < 0:
            return None
        else:
            curr = curr.next
            count = 1
            while curr is not None:
                if count == index:
                    prev.next = curr.next
                    self.count -= 1
                else:
                    count += 1
                    prev = curr
                    curr = curr.next
