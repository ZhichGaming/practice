'''
import heapq

# N: Number of nodes
# M: Number of edges
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

order = dict()

for i in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

    order[(u, v)] = i
    order[(v, u)] = i

queue = [(1, 1)]
visited = set()

connections = [0 for _ in range(N + 1)]
minimum_graphs = []
starting_values = []
graph_index = -1

# We don't need Prim or Kruskal algo for this simple unweighted graph.
for i in range(1, N + 1):
    if i not in visited:
        heapq.heappush(queue, (1, i))
        graph_index += 1
        minimum_graphs.append([[] for _ in range(N + 1)])
        starting_values.append(i)

    while queue:
        weight, current = heapq.heappop(queue)

        visited.add(current)

        for neighbour in graph[current]:
            if neighbour in visited:
                continue

            if connections[neighbour] >= 2:
                continue

            connections[neighbour] += 1

            heapq.heappush(queue, (1, neighbour))
            
            minimum_graphs[graph_index][current].append(neighbour)
            minimum_graphs[graph_index][neighbour].append(current)

ans = ["G" for _ in range(M)]

def dfs(cur, prevIsBlue, visited, minimumGraphIndex):
    visited.add(cur)

    for neighbour in minimum_graphs[minimumGraphIndex][cur]:
        if neighbour in visited:
            continue

        ans[order[(cur, neighbour)]] = "R" if prevIsBlue else "B"
        dfs(neighbour, not prevIsBlue, visited, minimumGraphIndex)

for i in range(len(minimum_graphs)):
    dfs(starting_values[i], True, set(), i)

print("".join(ans))
'''
import sys
sys.setrecursionlimit(300000)

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())

    graph[u].append((v, i))
    graph[v].append((u, i))

visited = set()
colors = ["G"] * M

def dfs(curr, color):
    visited.add(curr)

    for neighbour in graph[curr]:
        if neighbour[0] in visited:
            continue

        colors[neighbour[1]] = color
        dfs(neighbour[0], "R" if color == "B" else "B")

for i in range(1, N + 1):
    if i in visited:
        continue

    dfs(i, "R")

print("".join(colors))
