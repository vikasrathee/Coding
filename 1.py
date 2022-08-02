# Hash table
INITIAL_CAPACITY = 50


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:

    def __init__(self) -> None:
        self.size = 0
        self.capacity = INITIAL_CAPACITY
        self.slots = [None] * INITIAL_CAPACITY
    
    def insert(self, key, value):
        self.size += 1
        index = self.get_hash(key)

        node = self.slots[index] 
        if node is None:
            self.slots[index] = Node(key, value)
            return
        
        while node is not None:
            prev = node
            node = node.next
        
        node.next = Node(key, value)


        
    def search(self, value):\
        pass

    def get_hash(self, value):
        return value % self.capacity
    

    


        
