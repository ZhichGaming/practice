from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parents = [i for i in range(n)]
        rank = [0] * n

        def find(node: int) -> int:
            if node != parents[node]:
                return find(parents[node])
            
            return parents[node]
        
        def union(node1: int, node2: int):
            root_1 = find(node1)
            root_2 = find(node2)

            if root_1 != root_2:
                if rank[root_1] > rank[root_2]:
                    parents[root_2] = root_1
                elif rank[root_2] > rank[root_1]:
                    parents[root_1] = root_2
                else:
                    parents[root_1] = root_2
                    rank[root_2] += 1

        
        for edge in edges:
            union(edge[0], edge[1])
        
        return find(source) == find(destination)
