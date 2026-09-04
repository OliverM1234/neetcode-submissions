class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def makeChange(index,subset,total):
            if total > target or index >= len(nums):
                return

            if total == target:
                res.append(subset.copy())
                return

            subset.append(nums[index])
            makeChange(index, subset, total+nums[index])

            subset.pop()

            makeChange(index+1,subset, total)

        makeChange(0, [], 0)

        return res

        