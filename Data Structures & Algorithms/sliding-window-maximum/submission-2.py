class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []

        for i in range(len(nums)-(k-1)):
            out.append(max(nums[i:(i+k)]))

        return out        