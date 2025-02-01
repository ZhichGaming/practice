N = int(input())

mem = {}

def getTreeCount(weight):
    if weight in mem:
        return mem[weight]

    if weight < 3:
        return 1

    res = 0

    last_subtree = 1
    each_weight = weight // 2
    subtrees = weight // each_weight
    

    while each_weight > 0:
        # print(subtrees, each_weight)
        res += getTreeCount(each_weight) * (subtrees - last_subtree)

        last_subtree = subtrees
        each_weight -= 1

        if each_weight <= 0:
            break

        subtrees = weight // each_weight
        

    mem[weight] = res
    return res

print(getTreeCount(N))
