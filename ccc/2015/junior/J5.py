import math

pies = int(input())
people = int(input())

ways = 1

def recursiveMaxPies(remaining_pieces, remaining_people):
    

for i in range(people):
    ways *= math.floor(remaining_pieces/(people-i))

print(ways)
