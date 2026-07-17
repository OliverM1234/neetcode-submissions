import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if len(piles) > h:
            return Fals

        low = 1
        high = max(piles)

        while low <= high:

            mid = low + (high - low)//2

            total = 0

            for p in piles:
                total += math.ceil(p/mid)

            print(low,high,total,mid)

            if total > h:
                low = mid + 1
            elif total < h:
                high = mid - 1
            else:
                if low == high:
                    return low
                else:
                    high = mid
                

        total = 0
        for p in piles:
            total += math.ceil(p/mid)
        if total > h:
            mid += 1

        return mid