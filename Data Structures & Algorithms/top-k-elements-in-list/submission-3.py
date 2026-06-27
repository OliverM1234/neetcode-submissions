class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for n in nums:

            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        return list(map(lambda x: x[0], sorted(tuple(freq.items()), key = lambda x: x[1])))[-k:]