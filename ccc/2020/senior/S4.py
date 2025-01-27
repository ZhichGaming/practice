seats = input()
N = len(seats)

rounded_seats = 2 * seats

presum_A = [0] * N * 2
presum_B = [0] * N * 2
presum_C = [0] * N * 2

A_count = 0
B_count = 0
C_count = 0

for i in range(N * 2):
    if i > 0:
        presum_A[i] = presum_A[i - 1]
        presum_B[i] = presum_B[i - 1]
        presum_C[i] = presum_C[i - 1]
    
    if rounded_seats[i] == "A":
        presum_A[i] += 1
        A_count += 1
    if rounded_seats[i] == "B":
        presum_B[i] += 1
        B_count += 1
    if rounded_seats[i] == "C":
        presum_C[i] += 1
        C_count += 1
    
A_count = A_count // 2
B_count = B_count // 2
C_count = C_count // 2

min_swaps = float("inf")

for start in range(N):
    good_A = presum_A[start + A_count] - presum_A[start]
    bad_A = A_count - good_A

    good_B = presum_B[start + A_count + B_count] - presum_B[start + A_count]
    bad_B = B_count - good_B
    ab = bad_A + bad_B - min(presum_A[start + A_count + B_count] - presum_A[start + A_count], presum_B[start + A_count] - presum_B[start])
    
    good_C = presum_C[start + A_count + C_count] - presum_C[start + A_count]
    bad_C = C_count - good_C
    ac = bad_A + bad_C - min(presum_A[start + A_count + C_count] - presum_A[start + A_count], presum_C[start + A_count] - presum_C[start])

    min_swaps = min(min_swaps, ab, ac)

print(min_swaps)


