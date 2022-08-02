
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
        
    def insert(self, value):
        pass
    
    def delete(self, index):
        pass

    def get(self, index):
        pass
