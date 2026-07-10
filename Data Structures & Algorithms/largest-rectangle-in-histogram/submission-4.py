class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        for x,h in enumerate(heights):
            l=x
            r=x
            while l>0 and heights[l-1] >= h:
                l -= 1

            while r<(len(heights)-1) and heights[r+1] >= h:
                r += 1

            res = (r-l+1) * h

            print(l,r,h,res)

            max_area = max(res,max_area)

        return max_area


            

