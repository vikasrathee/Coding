class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None

class LRU:
    def __init__(self, size):
        self.capacity = size
        self.d = {}
        self.head = None
        self.tail = None

    def get(self, key):
        if key in self.d:
            self.d[key]
        else:
            return -1

    def put(self, key, val):
        if len(self.d) < self.size:
            self.d[key] = val
        else:
            pass


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
#grid = [[0,0,0,0,0,0,0,0]]

def find_max_area(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    visited = set() 

    def dfs(i,j):
        if i < 0 or j < 0 or (i,j) in visited or i == ROWS or j == COLS or grid[i][j] == 0:
            return 0

        visited.add((i,j))
        
        return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1) 

    max_area = 0
    
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            max_area = max(max_area, dfs(i,j))
    
    return max_area


print(find_max_area(grid))