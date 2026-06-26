class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_set = set()

        for n in nums:
            if n in number_set:
                return True
            else:
                number_set.add(n)

        return False
        