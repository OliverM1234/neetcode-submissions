class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def subsetGen(nums, out):
            
            if not nums:
                return [out]
            
            return subsetGen(nums[1:],[nums[0]]+out) + subsetGen(nums[1:],out)
        
        return subsetGen(nums, [])