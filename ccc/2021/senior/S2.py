M = int(input())
N = int(input())
K = int(input())

rows = [False] * (M + 1)
cols = [False] * (N + 1)

for _ in range(K):
    direction, value = input().split()
    value = int(value)

    if direction == "R":
        rows[value] = not rows[value]
    else:
        cols[value] = not cols[value]

result = 0

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if (rows[i] or cols[j]) and not (rows[i] and cols[j]):
            result += 1

print(result)
