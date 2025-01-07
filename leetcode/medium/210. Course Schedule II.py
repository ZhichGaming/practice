from collections import deque
from typing import List


# i'm literally the goat what can i say
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        prereq_count = [0] * numCourses

        for p in prerequisites:
            prereq = p[1]
            course = p[0]
            graph[prereq].append(course)
            prereq_count[course] += 1

        q = deque()
        visited = []

        for (i, count) in enumerate(prereq_count): 
            if count == 0:
                q.append(i)

        while q:
            c = q.popleft()
            visited.append(c)

            for ngbr in graph[c]:
                if ngbr in visited:
                    return []
                
                prereq_count[ngbr] -= 1

                if prereq_count[ngbr] == 0:
                    q.append(ngbr)
        
        return visited if len(visited) == numCourses else []
        