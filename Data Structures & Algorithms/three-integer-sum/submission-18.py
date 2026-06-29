class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)

        print(nums)

        out = []
        
        for x in range(len(nums)-2):
            if x>0 and nums[x] == nums[x-1]:
                continue

            n = nums[x]
            f=x+1
            b=len(nums)-1

            print(x,f,b)

            while b>f:

                total = nums[f]+nums[b]+n

                if total > 0:
                    b-=1
                elif total < 0:
                    f+=1
                else:
                    out.append([n,nums[f],nums[b]])
                    f += 1
                    b -=1 

                    while f<b and nums[f] == nums[f-1]:
                        f+=1

        return out