import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        maxHeap = []
        task_count = {}
        queue = deque()
        time = 0

        maxHeap = Counter(tasks)
        maxHeap = [(-c[1], c[0]) for c in maxHeap.items()]

        heapq.heapify(maxHeap)

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

            


