# Given a list of strings/words, return a list/table of all the letters found in multiple strings where it’s occurring most with other letter or letters.
# Input: ["abef", "bcd", "bde", "cadf"]

# Output:
# {
#  a: {f} // f occurs 2 times with a
#  b: {d,e} // d and e occur 2 times with b
#  c: [d] // d occurs 2 times with c
#  d: [b,c] // b and c occur 2 times with d 
#  e: [b] // b occurs 2 times with e 
#  f: [a] // a occurs 1 time with f
# }

def freq(counterlist):
    l = []
    max = 0

    for ix, v in enumerate(counterlist):
        if v > max:
            max  = v
    
    if max == 0:
        return []

    for ix, v in enumerate(counterlist):
        if v == max:
            l.append(chr(ix + 97))
            
    return l

def frequent_pair(words):
    counter = [[0] * 26 for i in range(26)]
    
    for word in words:
        for ix, x in enumerate(word):
            for iy, y in enumerate(word):
                if x != y:
                    counter[ord(x)-97][ord(y)-97] += 1
    
    res = {}

    for ix, charlist in enumerate(counter):
        l = freq(charlist)
        if l:
            res[chr(ix +97)] = l

    return res


# for word in words:
#A = ["abef", "bcd", "bde", "cadf"]
#print(frequent_pair(A))


# A = [ [1,2], [], [3,4,5], [] , [6], [7,8] ]
# Implement hasNext and next 

class DDL_iterator:
    def __init__(self, data):
        self.data = data
        self._max_x = len(self.data) - 1
        self._max_y = len(self.data[self._max_x]) - 1
        self._x = 0
        self._y = 0
        
    def next(self):
        for ix in range(self._x, len(self.data)):
            for iy in range(self._y, len(self.data[ix])):
                if iy == len(self.data[ix])-1:
                    self._x += 1
                    self._y = 0
                else:
                    self._y += 1
                
                return self.data[ix][iy]
                
    def has_next(self):
        if self._x == self._max_x and self._y == self._max_y:
            return False
        return True


A = DDL_iterator([ [1,2], [], [3,4,5], [] , [6], [7,8] ])

while A.has_next():
    print(A.has_next())
    print(A.next())