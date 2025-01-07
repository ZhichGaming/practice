from collections import deque
from typing import List

'''
# This solution has an issue. When visiting nodes, I mark them as visited immediately.
# In situations such as this one,
# 0 → 1 → 2
#     ↑   ↓
#     4 ← 3
# Although there is a cycle, I would incorrectly think that there is a cycle because I am visiting node 1 multiple times

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # It is stupid that this stupid line sets a list of references to the same list holy shit
        # graph: List[List[int]] = [[]]*numCourses
        graph: List[List[int]] = [[] for _ in range(numCourses)]

        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])

        queue = deque()
        visited = set()
        unvisited = set(range(numCourses))

        while unvisited: # Watch out, you need this if the problem doesn't say that the graphs have to be connected!
            # Issue: When visiting the unvisited nodes, it sets the node as visited 
            # so when this class has a prerequisite, it returns False.
            queue.append(next(iter(unvisited)))

            while queue:
                current = queue.popleft()

                if current in visited:
                    return False
                
                visited.add(current)
                unvisited.remove(current)

                for ngbr in graph[current]:
                    queue.append(ngbr)


        return True
'''
'''
# I still had to rely on the answer key to get the answer. Once again. Bruh.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1
        
        queue = deque()
        visited = set()

        # while len(visited) != numCourses:
        queue.extend([i for (i, subject) in enumerate(indegree) if subject == 0])

        while queue:
            c = queue.popleft()
            visited.add(c)

            for next_class in graph[c]:
                indegree[next_class] -= 1

                if indegree[next_class] == 0:
                    queue.append(next_class)
        
        return len(set(indegree)) == 1 and indegree[0] == 0
'''

'''
# Should work, my own solution, but O(V^2+E) complexity
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
        
        global_visited = set()

        def dfs(current: int, visited: set[int]):
            new_visited = visited.copy()

            if current in new_visited:
                global_visited.add(current)
                return False

            new_visited.add(current)
            global_visited.add(current)

            neighbours = graph[current]
            for neighbour in neighbours:
                if not dfs(neighbour, new_visited):
                    return False
            
            return True
        
        while len(global_visited) != numCourses:
            curr = next(iter(set(range(numCourses)) - global_visited))

            if not dfs(curr, set()):
                return False
        
        return True
'''

'''
# My improved solution without set copying, O(V+E) but still runs into TLE on LeetCode. 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
        
        global_visited = set()
        visited = set()

        def dfs(current: int):
            if current in visited:
                global_visited.add(current)
                return False

            visited.add(current)

            neighbours = graph[current]
            for neighbour in neighbours:
                if not dfs(neighbour):
                    return False
            
            visited.remove(current)
            global_visited.add(current)

            return True
        
        for i in range(numCourses):
            if i in global_visited:
                continue

            if not dfs(i):
                return False
        
        return True
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for prereq in prerequisites:
            course = prereq[0]
            prerequisite = prereq[1]

            graph[prerequisite].append(course)

        states = [0] * numCourses
        
        def dfs(curr: int):
            if states[curr] == 1:
                return False
            if states[curr] == 2: # This is memoization.
                return True

            states[curr] = 1

            for ngbr in graph[curr]:
                if not dfs(ngbr):
                    return False
            
            states[curr] = 2
            return True
        
        for course_index in range(numCourses):
            if states[course_index] == 0:
                if not dfs(course_index):
                    return False
        
        return True

        


# print(Solution().canFinish(2, [[0, 1], [1, 0]]))
# print(Solution().canFinish(100, [[1,0],[2,0],[2,1],[3,1],[3,2],[4,2],[4,3],[5,3],[5,4],[6,4],[6,5],[7,5],[7,6],[8,6],[8,7],[9,7],[9,8],[10,8],[10,9],[11,9],[11,10],[12,10],[12,11],[13,11],[13,12],[14,12],[14,13],[15,13],[15,14],[16,14],[16,15],[17,15],[17,16],[18,16],[18,17],[19,17],[19,18],[20,18],[20,19],[21,19],[21,20],[22,20],[22,21],[23,21],[23,22],[24,22],[24,23],[25,23],[25,24],[26,24],[26,25],[27,25],[27,26],[28,26],[28,27],[29,27],[29,28],[30,28],[30,29],[31,29],[31,30],[32,30],[32,31],[33,31],[33,32],[34,32],[34,33],[35,33],[35,34],[36,34],[36,35],[37,35],[37,36],[38,36],[38,37],[39,37],[39,38],[40,38],[40,39],[41,39],[41,40],[42,40],[42,41],[43,41],[43,42],[44,42],[44,43],[45,43],[45,44],[46,44],[46,45],[47,45],[47,46],[48,46],[48,47],[49,47],[49,48],[50,48],[50,49],[51,49],[51,50],[52,50],[52,51],[53,51],[53,52],[54,52],[54,53],[55,53],[55,54],[56,54],[56,55],[57,55],[57,56],[58,56],[58,57],[59,57],[59,58],[60,58],[60,59],[61,59],[61,60],[62,60],[62,61],[63,61],[63,62],[64,62],[64,63],[65,63],[65,64],[66,64],[66,65],[67,65],[67,66],[68,66],[68,67],[69,67],[69,68],[70,68],[70,69],[71,69],[71,70],[72,70],[72,71],[73,71],[73,72],[74,72],[74,73],[75,73],[75,74],[76,74],[76,75],[77,75],[77,76],[78,76],[78,77],[79,77],[79,78],[80,78],[80,79],[81,79],[81,80],[82,80],[82,81],[83,81],[83,82],[84,82],[84,83],[85,83],[85,84],[86,84],[86,85],[87,85],[87,86],[88,86],[88,87],[89,87],[89,88],[90,88],[90,89],[91,89],[91,90],[92,90],[92,91],[93,91],[93,92],[94,92],[94,93],[95,93],[95,94],[96,94],[96,95],[97,95],[97,96],[98,96],[98,97],[99,97]]))
