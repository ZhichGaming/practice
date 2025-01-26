'''
N = int(input())
friends = []
vertices = []

for i in range(N):
    P, W, D = map(int, input().split())

    friends.append((P, W, D))
    
    if D > 0:
        vertices.append((max(0, P - D), i))
    
    vertices.append((P + D, i))

vertices = sorted(vertices)


def getTime(concert_pos):
    cost = 0

    for P, W, D in friends:
        left = P - D
        right = P + D

        if concert_pos < left:
            cost += W * (left - concert_pos)
        elif concert_pos > right:
            cost += W * (concert_pos - right)

    return cost

left = vertices[0][0]
right = vertices[-1][0]

mid = 0
score = 0

while left <= right:
    mid = (left + right) // 2

    score = getTime(mid)

    score_left = getTime(mid - 1)
    score_right = getTime(mid + 1)

    if (score < score_left and score < score_right) or score == score_left or score == score_right:
        break

    if score < score_right:
        right = mid - 1
    elif score < score_left:
        left = mid + 1
         
print(score)
'''

N = int(input())
friends = []

l = float("inf")
r = 0

for _ in range(N):
    P, W, D = map(int, input().split())

    friends.append((P, W, D))

    l = min(l, P)
    r = max(r, P)

def findTime(c):
    total = 0

    for P, W, D in friends:
        if P - D <= c and c <= P + D:
            continue

        total += W * max(abs(c - P) - D, 0)
    
    return total

cost = 0

while l <= r:
    center_index = (l + r) // 2

    cost = findTime(center_index)
    cost_left = findTime(center_index - 1)
    cost_right = findTime(center_index + 1)


    if (cost < cost_left and cost < cost_right) or cost == cost_left or cost == cost_right:
        break

    if cost < cost_right:
        r = center_index 
    elif cost < cost_left:
        l = center_index 

print(cost)

