
from abc import abstractmethod

from abc import ABC

class B:
    @abstractmethod
    def call(self):
        pass

    def call1(self):
        return 11



class D(B):
    def __init__(self) -> None:
        super().__init__()

    def call(self):
       return 10


d = D()
print(d.call1())
    

from collections import Counter

c =Counter(["a","a","b","b","a","","v"])  
print(c.most_common(2))

from abc import abstractmethod
from abc import ABC

class A(ABC):
    
    @abstractmethod
    def method():
        return 0

class B(A):
    def __init__(self) -> None:
        super().__init__()

    def method(self):
        return 1

b = B()
print(b.method())

    