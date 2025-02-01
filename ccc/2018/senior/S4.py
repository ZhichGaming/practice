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
        # we are substracting because we aren't counting the weights but rather the number of possibilities we skipped by doing weight -1
        res += getTreeCount(each_weight) * (subtrees - last_subtree)

        last_subtree = subtrees
        # This skips weights, but that is fine because we only want the possibilities of the maximum weights.
        each_weight = weight // (subtrees + 1)
        # each_weight -= 1

        if each_weight <= 0:
            break

        subtrees = weight // each_weight
        

    mem[weight] = res
    return res

print(getTreeCount(N))
