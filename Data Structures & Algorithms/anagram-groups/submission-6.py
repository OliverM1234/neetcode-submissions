class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        stringdict = {}

        for s in strs:
            freq = {}

            for l in s:
                if l in freq:
                    freq[l] += 1
                else:
                    freq[l] = 1

            key = tuple(sorted(freq.items()))

            if key in stringdict:
                stringdict[key].append(s)
            else:
                stringdict[key] = [s]
        
        return list(stringdict.values())