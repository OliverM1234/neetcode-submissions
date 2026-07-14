class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        low = 0
        high = len(matrix)-1

        n = len(matrix[0])-1
        
        m = -1

        while low<=high:

            mid = low + (high-low)//2

            if matrix[mid][0] <= target and target <= matrix[mid][n]:
                m = mid
                break
            elif target < matrix[mid][0]:
                high = mid-1
            else:
                low = mid + 1

        if m == -1:
            return False
        
        low = 0
        high = n

        while low <= high:

            mid = low + (high - low)//2

            if matrix[m][mid] == target:
                return True
            elif matrix[m][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False