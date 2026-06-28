class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if 0 in nums:
            old_nums = nums.copy()
            nums.remove(0)
            print(old_nums)
            print(nums)

            if 0 in nums:
                return [0]* len(old_nums)
            else:
                out = [0]* len(old_nums)

                total = 1

                for n in nums:
                    total *= n

                out[old_nums.index(0)] = total

                return out


        total = 1

        for n in nums:
            total *= n

        out = []

        for n in nums:
            out.append(int(total/n))

        return out