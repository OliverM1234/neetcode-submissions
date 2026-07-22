class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        dupset = set()

        for n in nums:
            if n in dupset:
                return n
            else:
                dupset.add(n)
        