N, M, R, C = map(int, input().split())

def do_stuff(N, M, R, C):
    letters = ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    answer = [[] for _ in range(N)]

    for row in range(N):
        for col in range(M):
            if R > 0:
                answer[row].append("a")
            elif col < C:
                answer[row].append("a")
            else:
                answer[row].append(letters[(row+col) % len(letters)])
        
        R -= 1
    
    return filter(lambda x: len(x) != 0, answer)

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


# it's impossible if the number of rows is even and R is odd, applies to C and M as well
if (R == N and C != M):
    if (C % 2 != 0 and M % 2 == 0):
        print("IMPOSSIBLE")
    # else:

elif (R != N and C == M):
    if (R % 2 != 0 and N % 2 == 0):
        print("IMPOSSIBLE")
    else:
        ans = [["a"] * M for _ in range(N)]

        index = 0

        while R >= 2:
            

            R -= 2
            index += 1
        
else:
    for ans in do_stuff(N, M, R, C):
        print("".join(ans))
