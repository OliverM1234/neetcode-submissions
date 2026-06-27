class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            
        num_bucket = {}

        for n in nums:

            if n in num_bucket:
                num_bucket[n] += 1
            else:
                num_bucket[n] = 1
        
        freq_bucket = [[] for _ in range(len(nums)+1)]

        for key in num_bucket:
            freq_bucket[num_bucket[key]].append(key)

        result = []

        for i in range(len(freq_bucket)-1, 0, -1):

            for elem in freq_bucket[i]:

                result.append(elem)

                if len(result) >= k:
                    return result
