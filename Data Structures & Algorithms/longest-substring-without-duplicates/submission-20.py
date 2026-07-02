class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        l=0
        r=1
        word=set()
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        word.add(s[0])
        maxlen = 0
        while (r<len(s)):
            print(l,r,maxlen,word)
            if s[r] in word:

                while s[r] in word:
                    word.remove(s[l])
                    l += 1
                word.add(s[r])
            else:
                word.add(s[r])
            if (r-l+1) > maxlen:
                maxlen = r-l+1
            r+=1
        return maxlen