class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        out = [0] * len(temperatures)
        stack = []

        for x,t in enumerate(temperatures):

            while stack and t > stack[-1][1]:
                index = stack.pop()[0]
                out[index] = x - index

            stack.append((x,t))

        return out


        