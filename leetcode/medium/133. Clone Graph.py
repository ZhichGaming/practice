# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque
from typing import Optional
'''
# Solution 1
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph: dict[int, list[Node]] = {} # I did not need to make an adjacency list to represent the graph, could've just made a dict of clones.
        q = [] # Use deque instead! 
        visited = set() # No need for a visited array if I use a dict of clones.

        if node: # I should have checked for node == None at the beginning to avoid any more type checking later.
            q.append(node) 

        while q:
            current = q.pop(0)
            
            if current.val in visited:
                continue

            visited.add(current.val)

            graph[current.val] = current.neighbors
            q.extend(current.neighbors)

        nodes = [Node(n) for n in range(1, len(graph)+1)] # Would be unnecessary if I just made a dict of nodes at the start

        for node in nodes:
            for neighbor in graph[node.val]:
                node.neighbors.append(nodes[neighbor.val-1])

        return nodes[0] if len(nodes) > 0 else None
'''

# Better solution, correcting inaccuracies commented in the above snippet
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        q = deque([node])
        c_graph = { node.val: Node(node.val) }

        while q:
            curr = q.popleft()

            for neighbor in curr.neighbors:
                if neighbor.val not in c_graph:
                    c_graph[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)

                c_graph[curr.val].neighbors.append(c_graph[neighbor.val])
        
        return c_graph[1]
