import functools

class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        mem = [-1] * len(nums)

        def check_sols(i):
            if (i >= len(nums)):
                return 0

            if mem[i] != -1:
                return mem[i]

            mem[i] = max(nums[i] + check_sols(i+2), check_sols(i+1))

            return mem[i]

        option1 = check_sols(1)
        nums = nums[:-1]
        mem = [-1] * len(nums)
        option2 = check_sols(0)

        return max(option1, option2)
        