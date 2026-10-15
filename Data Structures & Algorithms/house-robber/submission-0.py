class Solution:
    def rob(self, nums: List[int]) -> int:

        max_from = {}
        def maxRob(i):
            if i >= len(nums):
                return 0

            if i in max_from:
                return max_from[i]

            max_val = max(maxRob(i+2)+nums[i], maxRob(i+1))

            max_from[i] = max_val

            return max_val

        return maxRob(0)