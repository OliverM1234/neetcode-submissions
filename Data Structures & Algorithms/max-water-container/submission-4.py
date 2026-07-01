class Solution:
    def maxArea(self, heights: List[int]) -> int:

        f=0
        b=len(heights)-1
        maxvol = 0

        while b>f:

            new_vol = (b-f)*min(heights[f],heights[b])

            if new_vol > maxvol:
                maxvol = new_vol

            if heights[f]<heights[b]:
                f +=1
            elif heights[f]>heights[b]:
                b-=1
            else:
                while heights[f]==heights[b]:
                    if f+1 >= len(heights):
                        b-=1
                        break
                    if b-1 < 0:
                        b-=1
                        break
                    if heights[f+1]>heights[b-1]:
                        f+=1
                        break
                    elif heights[f+1]<heights[b-1]:
                        b-=1
                        break
                    else:
                        f+=1
                        b-=1
        return maxvol
