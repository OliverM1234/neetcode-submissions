import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:

            biggest = -heapq.heappop(maxHeap)
            second_biggest = -heapq.heappop(maxHeap)

            if biggest != second_biggest:
                heapq.heappush(maxHeap, -(biggest-second_biggest))
        


        if maxHeap:
            return -maxHeap[0]
        else:
            return 0
