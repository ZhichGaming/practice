'''
from collections import defaultdict, deque
from sys import exit

M = int(input())
N = int(input())

grid = [[]]

for _ in range(M):
    grid.append([0] + list(map(int, input().split())))

dp = defaultdict(list)
visited = set()

q = deque()

q.append([1, 1])

def isValid(i, j):
    return i <= M and j <= N

while q:
    curr_pos = q.popleft()

    if curr_pos[0] == M or curr_pos[1] == N:
        print("yes")
        exit()

    curr = grid[curr_pos[0]][curr_pos[1]]    

    i = 1

    # if curr not in dp:
    while i**2 <= curr:
        if not isValid(i, 1):
            break
        
        if curr % i != 0:
            continue

        j = curr // i

        # dp[curr].extend([(i, j), (j, i)])

        if isValid(i, j) and grid[i][j] not in visited:
            visited.add(grid[i][j])
            q.append([i, j])
        
        if isValid(j, i) and grid[j][i] not in visited:
            visited.add(grid[j][i])
            q.append([j, i])
        
        i += 1

print("no")
'''

from collections import defaultdict, deque
from sys import exit

M = int(input())
N = int(input())

graph = defaultdict(list)

for i in range(1, M + 1):
    row = list(map(int, input().split()))

    for j in range(1, N + 1):
        graph[row[j - 1]].append(i*j)

q = deque()

q.append(M*N)

visited = set()
visited.add(M*N)

while q:
    curr_value = q.popleft()

    # print(curr_value)

    if curr_value == 1:
        print("yes")
        exit()

    for neighbor in graph[curr_value]:
        if neighbor in visited:
            continue

        visited.add(neighbor)

        q.append(neighbor)

print("no")
