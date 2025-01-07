N = int(input())

hats = []

for _ in range(N):
    hats.append(int(input()))

people_count = 0

for i in range(int(N/2)):
    if hats[i] != hats[int((i + N/2) % N)]:
        continue
        
    people_count += 2

print(people_count)
