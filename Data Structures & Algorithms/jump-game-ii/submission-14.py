class Solution:
    def jump(self, nums: List[int]) -> int:

        jumpCap = 0
        jumps = 0
        farthest = 0

        for i in range(len(nums)-1):

            farthest = max(farthest, i+nums[i])

            if jumpCap <= 0:
                jumpCap = farthest - i
                jumps += 1
            
            jumpCap -= 1

        return jumps

        