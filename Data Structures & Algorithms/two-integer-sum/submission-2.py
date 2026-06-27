class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_set = set(nums)

        for n in nums_set:
            if (target - n) in nums_set:
                if n != (target - n):
                    a, b = nums.index(n), nums.index(target-n)
                else:
                    a = nums.index(n)
                    nums[a] = None
                    b = nums.index(target-n)
                return [min(a,b), max(a,b)]