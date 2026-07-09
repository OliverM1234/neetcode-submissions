class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pos_times = []

        for i in range(len(position)):
            pos_times.append((position[i],(target - position[i])/speed[i]))
        

        pos_times = sorted(pos_times, key = lambda x: x[0])

        stack = []

        for i in range(len(position)):

            while stack and pos_times[i][1] >= stack[-1]:

                time = stack.pop()

            stack.append(pos_times[i][1])



        return len(stack)