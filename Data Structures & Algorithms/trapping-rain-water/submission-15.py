class Solution:
    def trap(self, height: List[int]) -> int:

        x = 0
        waterf = []
        ch = 0

        while (x<len(height)):

            if ch == 0:
                waterf.append(0)
            else:
                if height[x]<ch:
                    waterf.append(ch - height[x])
                else:
                    waterf.append(0)
            
            ch = max(height[x], ch)
            x += 1
        
        
        x = len(height)-1
        waterb = []
        ch = 0

        while (x>=0):

            if ch == 0:
                waterb.append(0)
            else:
                if height[x]<ch:
                    waterb.append(ch - height[x])
                else:
                    waterb.append(0)
            
            ch = max(height[x], ch)
            x -= 1
        waterb = list(reversed(waterb))

        total = 0
        for i in range(len(waterf)):
            total += min(waterf[i],waterb[i])

        return total