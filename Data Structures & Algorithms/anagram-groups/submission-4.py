class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictset = {}
        for s in strs:
            c_str = "".join(sorted(s))
            if c_str in dictset:
                dictset[c_str].append(s)
            else:
                dictset[c_str] = [s]

        return list(dictset.values())