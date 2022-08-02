### Some userfull notes for graphs

# Adj-List is more effficient in terms of storage since it is not impacted by sparsity,
# Adj-Matrix, grpah representation is always similar since there is no ordering involbed for the representation.

# Adj-List Implemenation for Graphs


from queue import Queue


class Vertex:
    def __init__(self, node) -> None:
        self.id = node
        self.connections = {}
        self.visited = False

class Graph:
    def __init__(self) -> None:
        self.vertices = {}
        self.numVertices = 0
    


    def dfs(self, G, vertex, visited):
        visited[vertex] = True

        for nbr in vertex.connections:
            if nbr not in visited:
                dfs(G,nbr, visited)


    def dfs_traversal(self, G):
        visited = {}   # This should be a dictionary to make quick lookup.
        for vertex in G:
            if vertex not in visited:
                dfs(G, vertex, visited) # run once if the graph is connected. multiple times if disconnected graph.
                

    def bfs_traversal(self, G):
        for vertex in G:
            bfs(G, vertex)

    def bfs(self, G, vertex):
        q = Queue()
        visited = {}
        visited[vertex] = True
        





        





    
