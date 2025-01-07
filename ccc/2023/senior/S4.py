import heapq

# class Road:
#     length: int
#     cost: int
#     # visited: bool = False

#     def __init__(self, _length, _cost):
#         self.length = _length
#         self.cost = _cost


# N, M = map(int, input().split())
# graph = [[] for _ in range(N + 1)]

# for _ in range(M):
#     u, v, l, c = map(int, input().split())

#     road_info = Road(l, c)

#     graph[u].append((v, road_info))
#     graph[v].append((u, road_info))

# mst = [[] for _ in range(N + 1)]
# q = []
# visited = set()
# total_cost = 0

# for i in range(1, N + 1):
#     if i in visited:
#         continue

#     heapq.heappush(q, (1, i, None))

#     while q:
#         cost, current, parent = heapq.heappop(q)
        
#         if current in visited:
#             continue

#         visited.add(current)

#         # mst[current].append((neighbour, info))
#         # mst[neighbour].append((current, info))
#         print(parent, current)

#         total_cost += cost

#         for neighbour, info in graph[current]:
#             heapq.heappush(q, (info.cost, neighbour, current))
        
# print(total_cost)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
edges = []

for i in range(M):
    u, v, l, c = map(int, input().split())

    edges.append((u, v, l, c, i))

    graph[u].append((v, l, c, i))
    graph[v].append((u, l, c, i))
    
edges.sort(key=lambda x: x[3], reverse=True)
do_not_use = set()
total_cost = 0

def distance(u, v):
    distances = [float('inf')] * (N + 1)
    distances[u] = 0

    q = [(0, u)]

    while q:
        weight, current = heapq.heappop(q)

        if current == v:
            return weight
        
        for neighbour, length, _, i in graph[current]:
            if i in do_not_use:
                continue

            new_weight = distances[current] + length

            if new_weight < distances[neighbour]:
                heapq.heappush(q, (new_weight, neighbour))
                distances[neighbour] = new_weight
    
    return float('inf')

for u, v, l, c, i in edges:
    do_not_use.add(i)

    if distance(u, v) > l:
        do_not_use.remove(i)
        total_cost += c

print(total_cost)
