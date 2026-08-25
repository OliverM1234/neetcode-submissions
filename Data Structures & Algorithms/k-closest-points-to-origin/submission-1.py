class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        points = [(- ( (p[0])**2 + (p[1])**2 )**0.5, p) for p in points]

        maxHeap = []
        heapq.heapify(maxHeap)

        for item in points:
            heapq.heappush(maxHeap, item)

            if len(maxHeap)>k:
                heapq.heappop(maxHeap)

        return [p[1] for p in maxHeap]

