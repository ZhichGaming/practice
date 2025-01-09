N, M, R, C = map(int, input().split())

def do_stuff(N, M, R, C):
    letters = ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    answer = [[] for _ in range(N)]

    if R == N or C == M:
        answer = [["a"] * M for _ in range(N)]

        curr_index = 0

        if R == N:
            extra = M - C

            while extra >= 2:
                answer[0][curr_index] = "b" 
                answer[0][M - 1 - curr_index] = "b"

                extra -= 2
                curr_index += 1
            
            if extra == 1:
                answer[0][(M - 1)//2] = "b" 
        else:
            extra = N - R

            while extra >= 2:
                answer[curr_index][0] = "b" 
                answer[N - 1 - curr_index][0] = "b"

                extra -= 2
                curr_index += 1
            
            if extra == 1:
                answer[(N - 1)//2][0] = "b" 
    else:
        for row in range(N):
            for col in range(M):
                if R > 0:
                    answer[row].append("a")
                elif col < C:
                    answer[row].append("a")
                else:
                    answer[row].append(letters[(row+col) % len(letters)])
            
            R -= 1
    
    return list(filter(lambda x: len(x) != 0, answer))

# it's impossible if the number of rows is even and R is odd, applies to C and M as well
if (R == N and C != M and C % 2 != 0 and M % 2 == 0) or (R != N and C == M and R % 2 != 0 and N % 2 == 0):
    print("IMPOSSIBLE")
        
else:
    for ans in do_stuff(N, M, R, C):
        print("".join(ans))
