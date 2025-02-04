from collections import deque

# MARK: Inputs
n, w, d = map(int, input().split())

walkways = [[] for _ in range(n + 1)]

for _ in range(w):
    a, b = map(int, input().split())

    walkways[b].append(a)

stations = [0] + list(map(int, input().split()))

swaps = list(list(map(int, input().split())) for _ in range(d))

# MARK: BFS walkways
q = deque()
walk_dist = [float("inf")] * (n + 1)
visited = set()

q.append(n)
walk_dist[n] = 0

while q:
    current = q.popleft()

    for neighbour in walkways[current]:
        if neighbour in visited:
            continue
    
        visited.add(current)

        q.append(neighbour)
        
        walk_dist[neighbour] = min(walk_dist[neighbour], walk_dist[current] + 1)

def getStationDistance(station):
    return n - station

def getWalkingDistance(station):
    return walk_dist[station]

# MARK: Swaps
for i in range(d):
    swap = swaps[i]
    stations[swap[0]], stations[swap[1]] = stations[swap[1]], stations[swap[0]]


