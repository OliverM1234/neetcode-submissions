import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
        if not self.min_heap:
            heapq.heappush(self.min_heap, num)
            return
        
        if num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        if len(self.min_heap) - len(self.max_heap) >= 2:
            temp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -temp)

        if len(self.max_heap) - len(self.min_heap) >= 2:
            temp = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -temp)



    def findMedian(self) -> float:

        if len(self.max_heap) - len(self.min_heap) == 1:
            return -self.max_heap[0]

        if len(self.min_heap) - len(self.max_heap) == 1:
            return self.min_heap[0]

        return (self.min_heap[0]+(-self.max_heap[0]))/2
        
        