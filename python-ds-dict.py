from unittest.mock import NonCallableMagicMock


a = [1,2,3,4,5,6,7,8,9]
print(a[1])


a = {}
a["name"] = "Vikas"
#b = a["name"]

b = a.get("name1") # Python3.10 would give none for missing key.


if "name1"  in a:
    print("Yes")
else:
    print("No")

print(type(a.keys()))


if type(a.keys()) == 'dict_keys':
    print("True")

else:
    print("False")


for x in a.keys():
    print(x)

print(b)



##### chaining implemenatation.

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
        
    def find(self, key):
        index = self.get_hash(key)

        node = self.slots[index]

        if node is None:
            return False
        

    def get_hash(self, value):
        return value % self.capacity
    

    
########## Open addressing implementation.

class HashTable:

    def __init__(self) -> None:
        self.size = 13 # This should be a prime number
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def put(self, key, value) -> None:
        index = self.generate_hash(key)

        if self.slots[index] is None:
            self.slots[index] = key
            self.data[index] = value
        else:
            if self.slots[index] == key:
                self.data[index] == value
            else:
                next_slot = self.generate_rehash(index)

                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.generate_rehash(next_slot)

                if self.slots[next_slot] == key:
                    self.data[next_slot] = value
                else:
                    self.slots[next_slot] == key
                    self.data[next_slot] = value

    def generate_hash(self, key):
        return key % self.size
    
    def generate_rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def get(self, key):
        index = self.generate_hash(key)

        while self.slots[index] != None:
            if self.slots[index] == key:
                return self.slots[index]
            
            index = self.generate_rehash(index)
        
        return -1

    def delete(self, key):
        index = self.generate_hash(key)

        while index is not None:
            if index == key:
                self.slots[index] == None
                return 

            index = self.generate_rehash(index)

        


    











        