class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_to_index = {}

        for i,n in enumerate(nums):
            comp = target - n


            if comp in nums_to_index:
                return [nums_to_index[comp] ,i]

            nums_to_index[n] = i