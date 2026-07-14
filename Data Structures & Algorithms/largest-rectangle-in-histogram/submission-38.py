class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for r in range(len(heights)):
            while stack and heights[r] < heights[stack[-1]]:
                h = heights[stack.pop()]
                if stack == []:
                    max_area = max(max_area, (r)*h)
                else:
                    if (r-stack[-1])*h > max_area:
                        print(r,stack[-1],h)
                    max_area = max(max_area, (r-stack[-1]-1)*h)
                


            stack.append(r)

        print(stack)
        max_area = max(max_area, heights[stack[0]]*len(heights))
        for j in range(len(stack)-1):
            
            max_area = max(max_area, (len(heights)-(stack[j]+1))*heights[stack[j+1]])

        return max_area

                





        
        
                