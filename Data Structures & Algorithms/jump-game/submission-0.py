class Solution:
    def canJump(self, nums: List[int]) -> bool:

        jumpCap = 0

        for i in range(len(nums)):

            if (jumpCap < 0):
                return False

            if nums[i] > jumpCap:
                jumpCap = nums[i]

            jumpCap -= 1

        return True
        