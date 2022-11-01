
from collections import deque


class Graph:

    def __init__(self) -> None:
        self.adj = [None] * len(V)
        self. = []
        self.E = []

    def addEdge():
        pass



##### Courses:
def if_courses_possible(self, numCourses: int, preReq: list[list[int]] ) -> bool:

    graph = {i: [] for i in numCourses}
    in_degree = {i: 0 for i in numCourses}
    
    for pre in preReq:
        graph[pre[0]].append(pre[1])
        in_degree[pre[0]] += 1

    source = []
    for vertex in in_degree.keys:
        if in_degree[vertex] == 0:
            source.append(vertex)

    sorted_list = []
    while source:
        vertex = source.pop[0]
        sorted_list.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                source.append(child)
    
    return len(sorted_list) == numCourses




def can_finish(self, numCourses, prereq):
    sorter_list = []

    if numCourses <= 0:
        return False
    
    graph = {i: [] for i in range{numCourses}}
    in_degree = {i: 0 for i in range{numCourses}}

    for preReq in prereq:
        parent, child = preReq[0], preReq[1]
        graph[parent].append[child]
        in_degree[child] += 1
    
    source = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            source.append(key)

    while source:
        vertex = source.pop(0)
        


