class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        taken = [False] * len(nums)
        res = []

        def genPerms(taken, perm):
            print(perm, taken, res[:10])
            
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i in range(len(taken)):
                
                if not taken[i]:

                    perm.append(nums[i])
                    taken[i] = True
                    genPerms(taken, perm)
                    perm.pop()
                    taken[i] = False

        genPerms(taken, [])
        return res