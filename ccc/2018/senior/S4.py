N = int(input())

mem = {}

def getTreeCount(weight):
    if weight in mem:
        return mem[weight]

    if weight < 3:
        return 1

    res = 0

    subtrees = 2
    each_weight = weight // 2

    while each_weight > 0:
        # print(subtrees, each_weight)
        res += getTreeCount(each_weight)

        subtrees += 1
        each_weight = weight // subtrees

    mem[weight] = res
    return res

print(getTreeCount(N))
