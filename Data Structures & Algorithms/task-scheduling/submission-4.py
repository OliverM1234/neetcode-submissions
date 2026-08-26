import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        maxHeap = []
        task_count = {}
        queue = deque()
        time = 0

        for task in tasks:

            if task in task_count:
                task_count[task] += 1
            else:
                task_count[task] = 1

        for task in task_count:
            heapq.heappush(maxHeap, (-task_count[task], task))

        while queue or maxHeap:
            if queue:
                new_time, new_count, new_task = queue[-1]
                if new_time <= time:
                    heapq.heappush(maxHeap, (new_count, new_task))
                    queue.pop()

            if not maxHeap:
                time += 1
                continue

            max_count, max_task = heapq.heappop(maxHeap)
            max_count += 1
            if max_count < 0:
                queue.appendleft((time+n+1, max_count, max_task))

            time += 1

        return time

            


