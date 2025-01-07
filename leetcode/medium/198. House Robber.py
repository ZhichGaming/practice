from typing import List
import heapq


'''
# Pretty greedy algo, doesn't work
class Solution:
    def rob(self, nums: List[int]) -> int:
        q: List[tuple[int, int]] = []

        for i in range(len(nums)):
            heapq.heappush(q, (-nums[i], i))

        # What if i just use a list to track neighbors?
        # 0 means untaken, 1 means neighbor taken, 2 means taken
        state = [0] * len(nums)

        robbed_value = 0

        while q:
            neg_val, index = heapq.heappop(q)
            val = -neg_val

            if state[index] > 0:
                continue

            state[index] = 2

            if state[index - 1] == 0:
                state[index - 1] = 1
            if state[index + 1] == 0:
                state[index + 1] = 1

            robbed_value += val
        
        return robbed_value
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for index in range(len(dp)):
            # Check whether dp[index - 2] + nums[index] > dp[index - 1]

            take_value = nums[index]
            untake_value = 0

            if index - 1 >= 0:
                untake_value += dp[index - 1]
            if index - 2 >= 0:
                take_value += dp[index - 2]

            dp[index] = max(take_value, untake_value)
        
        return dp[-1]
    