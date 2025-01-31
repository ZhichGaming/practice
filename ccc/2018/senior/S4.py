N = int(input())

mem = {}

def getTreeCount(weight):
    if mem[weight]:
        return mem[weight]

    if weight < 3:
        return 1

    res = 0

    

    mem[weight] = res
    return res
