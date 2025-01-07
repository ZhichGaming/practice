from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islandCount = 0

        def isValid(i, j):
            return i < len(grid) and i >= 0 and j < len(grid[0]) and j >= 0

        def bfs(start: str) -> set:
            q = deque([start])
            local_visited = set()

            while q:
                currentI, currentJ = map(int, q.popleft().split(" "))

                if not isValid(currentI, currentJ):
                    continue
                if grid[currentI][currentJ] == "0":
                    continue
                if f"{currentI} {currentJ}" in local_visited:
                    continue

                local_visited.add(f"{currentI} {currentJ}")

                q.append(f"{currentI - 1} {currentJ}")
                q.append(f"{currentI + 1} {currentJ}")
                q.append(f"{currentI} {currentJ - 1}")
                q.append(f"{currentI} {currentJ + 1}")

            return local_visited
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if f"{i} {j}" in visited:
                    continue

                if grid[i][j] == "0":
                    continue

                visited.update(bfs(f"{i} {j}"))
                islandCount += 1
        
        return islandCount
