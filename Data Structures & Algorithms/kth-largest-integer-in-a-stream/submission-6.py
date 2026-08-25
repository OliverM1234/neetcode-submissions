class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = list(reversed(sorted(nums)))
        self.k = k

    def add(self, val: int) -> int:
        if not self.nums:
            self.nums.append(val)
            return val

        index = 0
        while index < len(self.nums) and self.nums[index] > val:
            index += 1
        if index == len(self.nums):
            self.nums.append(val)
        else:
            self.nums.insert(index, val)
        print(self.nums, self.k,val)
        return self.nums[self.k-1]
        
