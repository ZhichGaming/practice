from collections import defaultdict

N, M = map(int, input().split())
strings = []

for _ in range(N):
    strings.append(input())

def isHeavy(char, charmap):
    return charmap[char] > 1

def compute(string):
    charmap = defaultdict(int)

    for char in string:
        charmap[char] += 1

    heavy = None

    for char in string:
        current_is_heavy = isHeavy(char, charmap)
        
        if heavy is not None and heavy == current_is_heavy:
            return "F"
        
        heavy = current_is_heavy
    
    return "T"

for string in strings:
    print(compute(string))    
