import heapq
from collections import defaultdict

n, pipe_count, delimiter_value = map(int, input().split())

# Handle input
pipes_inputs = []

for _ in range(pipe_count):
    inp = input()
    pipes_inputs.append(list(map(int, inp.split())))

pq = []

# Adjacency list graph and mst
graph: dict[int, list[tuple[int, int]]] = defaultdict(list)
mst = []

# City-made plan
prev_active_pipes = set()
prev_total_cost = 0
prev_max_cost_pipe = 0

# Process the inputs, adding to the graph, the priority queue and the city-made plan
for (i, pipe) in enumerate(pipes_inputs):
    from_building, to_building, cost = pipe
    graph[from_building].append((cost, to_building))
    heapq.heappush(pq, (cost, from_building, to_building))

    if (i < n - 1):
        prev_active_pipes.add((from_building, to_building))
        prev_total_cost += cost

        if cost > prev_max_cost_pipe:
            prev_max_cost_pipe = cost

# Substract the cost of the delimiter value if it is cheaper than the most expensive pipe
prev_total_cost -= min(prev_max_cost_pipe, delimiter_value)

# Union find
parent: dict[int, int] = dict()
rank: dict[int, int] = dict()

def find(node: int):
    if node not in parent:
        parent[node] = node

    if parent[node] != node:
        parent[node] = find(parent[node])
    
    return parent[node]

def union(node1: int, node2: int):
    root1 = find(node1)
    root2 = find(node2)

    if root1 == root2:
        return
    
    if root1 not in rank:
        rank[root1] = 1
    if root2 not in rank:
        rank[root2] = 1
    
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    elif rank[root1] < rank[root2]:
        parent[root1] = root2
    else:
        parent[root1] = root2
        rank[root2] += 1

# Kruskal's algorithm
# Count of new activated pipes and set of active new pipes
activated_count = 0
active_set = set()

total_cost = 0
expensivest_pipe = 0

# Process the priority queue and add to the mst
while pq:
    cost, from_pipe, to_pipe = heapq.heappop(pq)

    # There is a cycle, continue
    if find(from_pipe) == find(to_pipe):
        continue

    # Add to the mst
    union(from_pipe, to_pipe)
    active_set.add((from_pipe, to_pipe))
    total_cost += cost

    if cost > expensivest_pipe:
        expensivest_pipe = cost

    if (from_pipe, to_pipe) not in prev_active_pipes and (to_pipe, from_pipe) not in prev_active_pipes:
        activated_count += 1

# Count of new desactivated pipes
desactivated_count = 0

for pipe in prev_active_pipes:
    if pipe not in active_set and (pipe[1], pipe[0]) not in active_set:
        desactivated_count += 1

# Substract the cost of the delimiter value if it is cheaper than the most expensive pipe
total_cost -= min(expensivest_pipe, delimiter_value)

# Print the bigger value between the activated and desactivated pipes (number of days required) if 
# the total cost is less than the previous total cost
# Else, print 0 because the previous plan is a valid and cheap plan
print(max(activated_count, desactivated_count) if total_cost < prev_total_cost else 0)
