from collections import deque
import heapq

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

heap = []

for i in range(1, n + 1):
    # if stations[i] == n:
    #     heapq.heappush(heap, (i, i))
    #     continue
    if walk_dist[stations[i]] == float("inf"):
        continue

    heapq.heappush(heap, (i - 1 + walk_dist[stations[i]], i))

# MARK: Swaps
for i in range(d):
    swap = swaps[i]
    stations[swap[0]], stations[swap[1]] = stations[swap[1]], stations[swap[0]]

    if walk_dist[stations[swap[0]]] != float("inf"):
        heapq.heappush(heap, (swap[0] - 1 + walk_dist[stations[swap[0]]], swap[0]))
    if walk_dist[stations[swap[1]]] != float("inf"):
        heapq.heappush(heap, (swap[1] - 1 + walk_dist[stations[swap[1]]], swap[1]))
    
    # we cannot heap pop this step because if we do so, the heap will be missing a value even if the value is up to date
    current = heap[0][1] - 1 + walk_dist[stations[heap[0][1]]]

    while current != heap[0][0]:
        heapq.heappop(heap)

        current = heap[0][1] - 1 + walk_dist[stations[heap[0][1]]]

    print(current)



