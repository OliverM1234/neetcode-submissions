class Solution:
    def maxArea(self, heights: List[int]) -> int:

        f=0
        b=len(heights)-1
        maxvol = 0

        while b>f:

            new_vol = (b-f)*min(heights[f],heights[b])

            if new_vol > maxvol:
                maxvol = new_vol

            if heights[f]<=heights[b]:
                f +=1
            elif heights[f]>heights[b]:
                b-=1
                
        return maxvol
