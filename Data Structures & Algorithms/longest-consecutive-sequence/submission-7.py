class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        s_nums = sorted(nums)

        max_len = 0
        c_len = 1
        count= True

        print(s_nums)

        for i in range(1, len(s_nums)):
            print(i,c_len)
            if s_nums[i-1]+1 == s_nums[i]:
                c_len+=1
            elif s_nums[i-1] == s_nums[i]:
                continue
            else:
                if c_len > max_len:
                    max_len = c_len
                c_len = 1
            
        if c_len > max_len:
            max_len = c_len
        return max_len

            
        