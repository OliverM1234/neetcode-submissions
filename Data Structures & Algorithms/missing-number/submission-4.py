class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        true_nums = list(range(len(nums)+1))
        res = 0
        for n in true_nums:
            res ^= n
        for n in nums:
            res ^= n

        return res