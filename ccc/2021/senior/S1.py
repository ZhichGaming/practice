N = int(input())
heights = list(map(int, input().split()))
widths = list(map(int, input().split()))

total_area = 0

for i in range(N):
    total_area += widths[i] * (heights[i]+ heights[i + 1]) / 2

print(total_area)
