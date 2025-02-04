import math

n, k = map(int, input().split())

a = list(map(int, input().split()))

days = math.ceil(n / k)

head = 0
count = 0
total = 0

for i in range(n):
    curr = a[i]

    if count >= k:
        count = 0
        total += head

    if curr > head:
        head = curr

    count += 1

print(total)
