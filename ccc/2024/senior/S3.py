N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

compressed_B = []
index_B = []

block_start_index = 0
block_end_index = 0
prev = B[0]

for i in range(len(B)):
    el = B[i]

    if el != prev:
        compressed_B.append(prev)
        index_B.append((block_start_index, i - 1))

        prev = el
        block_start_index = i

compressed_B.append(prev)
index_B.append((block_start_index, N - 1))

curr_block = 0
left = []
right = []

for i in range(N):
    if curr_block == len(compressed_B):
        break

    if A[i] == compressed_B[curr_block]:
        if index_B[curr_block][0] < i:
            left.append((index_B[curr_block][0], i))
        if index_B[curr_block][1] > i:
            right.append((i, index_B[curr_block][1]))
        
        curr_block += 1

if curr_block == len(compressed_B):
    print("YES")
    print(len(left) + len(right))

    for el in left:
        print("L", el[0], el[1])
    for el in reversed(right):
        print("R", el[0], el[1])
else:
    print("NO")
    