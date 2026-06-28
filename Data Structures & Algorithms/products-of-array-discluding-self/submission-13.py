class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = []
        total = 1
        for n in nums:
            total*=n
            prefix_arr.append(total)

        suffix_arr = []
        total = 1
        for n in reversed(nums):
            total*=n
            suffix_arr.append(total)

        suffix_arr = list(reversed(suffix_arr))

        out = [suffix_arr[1]]

        for i in range(1,len(nums)-1):
            out.append(prefix_arr[i-1]*suffix_arr[i+1])

        out.append(prefix_arr[-2])

        print(prefix_arr)
        print(suffix_arr)
        print(out)
        return out


