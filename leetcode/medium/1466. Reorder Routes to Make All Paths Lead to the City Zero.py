from typing import List
from collections import deque

'''
# This approach TLEs at n=17984 
# O(n^2), unnecessary to use an adj. matrix and use a getNeighbors function
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[False]*n for _ in range(n)]

        for connection in connections:
            graph[connection[0]][connection[1]] = True
        
        q = deque()
        visited = set() # unnecessary, it was mentioned that you are working with a tree-like structure
        reordered = 0

        def getNeighbors(node: int) -> List[int]:
            result = []

            for (i, ngbr) in enumerate(graph[node]): # O(n)
                if ngbr:
                    result.append(i)
            for i in range(n):
                ngbr = graph[i][node]

                if ngbr:
                    result.append(i)
            
            return result

        q.append(0)

        while q: # O(n)
            curr = q.popleft()
            visited.add(curr)

            ngbrs = getNeighbors(curr) # O(n)

            for ngbr in ngbrs:
                if ngbr not in visited:
                    if graph[curr][ngbr]:
                        reordered += 1

                    q.append(ngbr) # O(1)
                
        return reordered
'''

# This approach TLEed at n=44667 before I added connections_set
class Solution:
    rotated = 0
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        connections_set = set([tuple(cn_tuple) for cn_tuple in connections]) # I made this a set of tuples cuz list is unhashable 

        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])

        def dfs(current: int, parent: int | None) -> int:
            rotated = 0

            for ngbr in graph[current]:
                if ngbr == parent:
                    continue

                if (current, ngbr) in connections_set:
                    rotated += 1
                
                rotated += dfs(ngbr, current)
            
            return rotated

        return dfs(0, None)
