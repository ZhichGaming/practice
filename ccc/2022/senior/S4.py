n, c = map(int, input().split())

points = [0] * c

for p in map(int, input().split()):
    points[p] += 1

prefix_sum = [points[0]]

for i in range(len(points)):
    prefix_sum[i] += 
