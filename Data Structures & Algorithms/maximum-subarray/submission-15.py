import functools

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cur_max = nums[0]
        act_max = nums[0]

        for i in range(1,len(nums)):
            cur_max = max(cur_max + nums[i], nums[i])
            act_max = max(cur_max, act_max)

        return act_max