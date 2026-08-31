class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        
        def subsetGen(index,subset):
            print(nums, subset)

            if index >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[index])
            subsetGen(index+1, subset)

            subset.pop()

            subsetGen(index+1,subset)
        
        subsetGen(0, [])
        return res