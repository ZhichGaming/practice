from collections import defaultdict

X = int(input())
must_map = defaultdict(set)

for _ in range(X):
    t1, t2 = input().split()
    
    must_map[t1].add(t2)
    must_map[t2].add(t1)

Y = int(input())
cannot_map = defaultdict(set)

for _ in range(Y):
    t1, t2 = input().split()
    
    cannot_map[t1].add(t2)
    cannot_map[t2].add(t1)

G = int(input())
cannot_violations = 0

for _ in range(G):
    names = input().split()

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            name_i = names[i]
            name_j = names[j]

            if name_j in must_map[name_i]:
                X -= 1
            
            if name_j in cannot_map[name_i]:
                cannot_violations += 1

print(X + cannot_violations)
