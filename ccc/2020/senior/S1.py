import heapq

N = int(input())

q = []

for _ in range(N):
    t, p = map(int, input().split())

    heapq.heappush(q, (t, p))

ans = 0

prev = heapq.heappop(q)

while q:
    curr = heapq.heappop(q)

    ans = max(ans, abs(curr[1]-prev[1])/(curr[0]-prev[0]))

    prev = curr

print(ans)
