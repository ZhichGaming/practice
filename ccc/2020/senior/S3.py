'''
# My first implementation was valid, the only way of going faster would be using hashes
N = input()
H = input()

visited = set()

needle_prefix = [0] * 26
haystack_prefix = [[0] * len(H) for _ in range(26)]

for i in range(len(N)):
    needle_prefix[ord(N[i]) - ord("a")] += 1

for i in range(len(H)):
    letter_index = ord(H[i]) - ord("a")

    if i > 0:
        for j in range(26):
            haystack_prefix[j][i] = haystack_prefix[j][i - 1]
    
    haystack_prefix[letter_index][i] += 1
    

def getRangeSum(prefix_sum, letter, l, r):
    return prefix_sum[letter][r] - (prefix_sum[letter][l] if l >= 0 else 0)

ans = 0

for i in range(len(H) - len(N) + 1):
    l = i - 1
    r = i + len(N) - 1

    if H[i:r+1] in visited:
        continue

    allgood = True

    for j in range(26):
        allgood = needle_prefix[j] == getRangeSum(haystack_prefix, j, l, r)

        if not allgood:
            break
    
    if not allgood:
        continue

    visited.add(H[i:r+1])
    ans += 1

print(ans)
'''


'''
# My second implementation is even more stupid, I'm not checking for a full match

from collections import defaultdict
import sys

N = input()
H = input()

visited = set()

needle_prefix = defaultdict(int)
haystack_prefix = defaultdict(int)

ans = 0


if len(N) > len(H):
    print(0)
    sys.exit()

for i in range(len(N)):
    needle_prefix[N[i]] += 1
    haystack_prefix[H[i]] += 1

allgood = True

for i in range(26):
    letter = chr(i + ord("a"))

    allgood = needle_prefix[letter] == haystack_prefix[letter]

    if not allgood:
        break

if allgood:
    visited.add(H[0:len(N)])
    ans += 1

for i in range(1, len(H) - len(N) + 1):
    j = i + len(N)

    removal_char = H[i - 1]
    added_char = H[j - 1]

    haystack_prefix[removal_char] -= 1
    haystack_prefix[added_char] += 1

    if H[i:j] in visited:
        continue

    removal_correct = needle_prefix[H[i - 1]] == haystack_prefix[H[i - 1]]
    added_correct = needle_prefix[H[j - 1]] == haystack_prefix[H[j - 1]]

    if removal_correct and added_correct:
        visited.add(H[i:j])
        ans += 1

print(ans)

'''
