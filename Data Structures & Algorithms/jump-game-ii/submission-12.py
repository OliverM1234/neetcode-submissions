class Solution:
    def jump(self, nums: List[int]) -> int:

        jumpCap = 0
        jumps = 0
        oldPos = -1

        possible = []

        for i in range(len(nums)-1):

            possible.append(i + nums[i])

            if jumpCap <= 0:
                jumpCap = max(possible) - i
                jumps += 1
            
            jumpCap -= 1

        return jumps

        