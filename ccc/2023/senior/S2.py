# Doesn't pass in DMOJ but works in CCC

import math

N = int(input())

mountains = list(map(int, input().split()))

final = [float("inf")] * N
answers = []

for i in range(N):
    answers.append([])

    answer_index = 0
    left_pointer = i
    right_pointer = i

    while left_pointer >= 0 and right_pointer < N:
        absolute_height_diff = abs(mountains[left_pointer] - mountains[right_pointer])

        if answer_index > 1:
            absolute_height_diff += answers[i][answer_index - 2]

        if absolute_height_diff < final[answer_index]:
            final[answer_index] = absolute_height_diff

        answers[i].append(absolute_height_diff)

        if right_pointer - i == i - left_pointer:
            right_pointer += 1
        else:
            left_pointer -= 1

        answer_index += 1

print(" ".join(map(str, final)))
