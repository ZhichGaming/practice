N = int(input())

row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))

total = 0

for i in range(N):
    first_contains = row1[i] == 1
    second_contains = row2[i] == 1

    if first_contains: 
        total += 3
    if second_contains: 
        total += 3

    even = i % 2 == 0

    if even and first_contains and second_contains:
        
        total -= 2
    
    prev_index = i - 1

    if prev_index >= 0:
        if row1[prev_index] == 1 and first_contains:
            total -= 2
        if row2[prev_index] == 1 and second_contains:
            total -= 2

print(total)
