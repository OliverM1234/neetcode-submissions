class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f=0
        b= len(numbers)-1

        while b>f:

            total = numbers[b]+numbers[f]

            if total > target:
                b -= 1
            elif total < target:
                f += 1
            else:
                return [f+1,b+1]
        
        return [-1,-1]