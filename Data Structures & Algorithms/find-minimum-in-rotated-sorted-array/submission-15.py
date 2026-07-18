class Solution:
    def findMin(self, nums: List[int]) -> int:

        low = 0
        high = len(nums)-1

        while low <= high:

            mid = low + (high - low)//2

            if nums[low]<nums[high]:
                return nums[low]

            if nums[mid] > nums[low]:
                low = mid + 1
            else:
                if mid != 0 and nums[mid-1]>nums[mid]:
                    return nums[mid]
                elif mid != len(nums)-1 and nums[mid]>nums[mid+1]:
                    return nums[mid+1]
                else:
                    high = mid - 1

        return nums[0]