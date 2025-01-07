graph = [
    [1, 2, 3],
    [0, 2],
    [0, 1],
    [0]
]
start = 1
end = 3

visited = set()
queue = [start]

reverse_graph = [-1]*len(graph)

while queue:
    node = queue.pop(0)
    visited.add(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            queue.append(neighbour)

            reverse_graph[neighbour] = node

path = []
current = end

while current != -1:
    path.append(current)
    current = reverse_graph[current]

print(list(reversed(path)))
