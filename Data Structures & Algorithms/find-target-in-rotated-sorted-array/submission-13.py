class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low, high = 0, len(nums)-1

        while low < high:

            mid = (low + high)//2

            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1

        min_index = low

        print(nums[:min_index],nums[min_index:])

        if target == nums[0]:
            return 0
        if min_index == 0:
            arr = nums
        elif target < nums[0]:
            arr = nums[min_index:]
        else:
            arr = nums[:min_index]
            min_index = 0
        
        print(arr, target)

        low, high = 0, len(arr)-1

        while low <= high:

            mid = (high + low)//2

            if target < arr[mid]:
                high = mid - 1
            elif target > arr[mid]:
                low = mid + 1
            else:
                print(mid)
                return mid+min_index

        return -1