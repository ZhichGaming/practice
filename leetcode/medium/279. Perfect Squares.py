import math

'''
# This approach doesn't work. It's too greedy, taking the largest number available that doesn't surpass.
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)

        for i in range(1, n+1):
            if i**2 <= n:
                dp[i**2] = 1
            
            if dp[i] > 0:
                continue

            value = 0
            amount = 0
            
            start = math.floor(i**(1/2))

            for j in range(start, 0, -1):
                while value + j*j <= i:
                    value += j*j
                    amount += 1

                    if value == i:
                        break
                
                if value == i:
                    break

            dp[i] = amount
        
        print(dp)
        return dp[-1]

Solution().numSquares(12)
'''


