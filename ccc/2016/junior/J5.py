problem_type = int(input())
length = int(input())
list_a = sorted(input().split())
list_b = sorted(input().split())

def getMax():
    total = 0

    for i in range(length):
        total += max(int(list_a[i]), int(list_b[length-1-i]))
    
    return total

def getMin():
    total = 0

    for i in range(length):
        total += max(int(list_a[i]), int(list_b[i]))
    
    return total

if problem_type == 1:
    print(getMin())
else:
    print(getMax())
