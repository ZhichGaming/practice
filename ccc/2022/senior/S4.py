from math import comb

n, c = map(int, input().split())

points = [0] * c

for p in map(int, input().split()):
    points[p] += 1

prefix_sum = [points[0]]

for i in range(1, c):
    prefix_sum.append(prefix_sum[i - 1] + points[i])

result = comb(n, 3)

for i in range(c):
    opp_i = i + c // 2

    points_between = 0

    if opp_i < c:
        points_between = (prefix_sum[opp_i] - prefix_sum[i])
    else:
        points_between = (prefix_sum[opp_i % c] + (prefix_sum[c - 1] - prefix_sum[i]))

    # bug 1: i didn't choose a combination of the points between
    result -= comb(points_between, 2) * points[i]
    result -= (points_between) * comb(points[i], 2)
    result -= comb(points[i], 3)

# bug 2: i didn't consider the duplicate points if the circumference is even (triangles in a straight line)
if c % 2 == 0:
    for i in range(c // 2):
        opp_i = (i + c // 2) % c

        result += points[opp_i] * comb(points[i], 2)
        result += points[i] * comb(points[opp_i % c], 2)

print(result)
