from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = { }
        rank = { }
        neq: dict[str, list] = { }

        def find(node: str):
            if parent[node] != node:
                return find(parent[node])
            
            return node
        
        def union(node1: str, node2: str):
            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2:
                return
            
            if rank[root1] > rank[root2]:
                parent[root2] = root1
                neq[root1].extend(neq[root2])
            elif rank[root2] > rank[root1]:
                parent[root1] = root2
                neq[root2].extend(neq[root1])
            else:
                parent[root1] = root2
                rank[root2] += 1
                neq[root2].extend(neq[root1])
        
        for equation in equations:
            incl = False if equation.find("!") != -1 else True
            first = equation[0]
            last = equation[-1]

            if first not in parent:
                parent[first] = first
                rank[first] = 1
                neq[first] = []
            if last not in parent:
                parent[last] = last
                rank[last] = 1
                neq[last] = []

            root_first = find(first)
            root_last = find(last)

            if incl:
                if root_last in neq[root_first] or root_first in neq[root_last]:
                    return False
                
                union(root_first, root_last)
            else:
                neq[root_first].append(root_last)
                neq[root_last].append(root_first)

                if root_first == root_last:
                    return False

        return True
