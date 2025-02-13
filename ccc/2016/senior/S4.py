n = int(input())
balls = list(map(int, input().split()))

dp = [[0] * (n + 3) for _ in range(n + 3)]
ans = max(balls)

for i in range(n):
    dp[i][i] = balls[i]

for length in range(1, n):
    for l in range(n - length):
        r = l + length
        i = l + 1
        j = r

        while i <= j:
            if dp[l][i - 1] != 0 and dp[l][i - 1] == dp[j][r] and (dp[i][j - 1] != 0 or i == j):
                dp[l][r] = dp[l][i - 1] + dp[j][r] + dp[i][j - 1]
                ans = max(dp[l][r], ans)

                break
            elif dp[l][i - 1] > dp[j][r]:
                j -= 1
            elif dp[l][i - 1] < dp[j][r]:
                i += 1
            else:
                j -= 1
                i += 1
        
print(ans)
