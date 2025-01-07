graph = [
    [1, 2],  # Node 0 has edges to Node 1 and Node 2
    [3],     # Node 1 has an edge to Node 3
    [3],     # Node 2 also has an edge to Node 3
    [4],     # Node 3 has an edge to Node 4
    [2]      # Node 4 has an edge back to Node 2, forming a cycle with Node 2 and Node 3
]

start = 0

def dfs(current: int, visited: list[int]):
    new_visited = visited.copy()

    if current in new_visited:
        first_index = new_visited.index(current)
        return new_visited[first_index:]

    new_visited.append(current)

    for neighbour in graph[current]:
        return dfs(neighbour, new_visited)

print(dfs(start, list()))
