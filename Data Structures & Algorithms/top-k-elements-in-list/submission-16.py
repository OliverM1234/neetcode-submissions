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

        i = -1
        result = []
        print(freq_bucket)
        while k > 0 and i >= -len(nums):
            print(freq_bucket[i],i,k)
            if freq_bucket[i] != []:
                j=0
                while k > 0 and j < len(freq_bucket[i]):
                    result.append(freq_bucket[i][j])
                    j += 1
                    k -= 1
            i -= 1
        return result
