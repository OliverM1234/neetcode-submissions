class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_palin = ""
        for i in range(len(s)):

            width = 1
            while (i-width) >= 0 and (i+width < len(s)):
                if s[i-width] == s[i+width]:
                    width += 1
                else:
                    break

            width -= 1

            if (2*width+1) > len(max_palin):
                max_palin = s[(i-width) : (i+width+1)]

        for j in range(len(s)-1):

            i = j+0.5

            width = 0.5
            while (i-width) >= 0 and (i+width < len(s)):
                if s[int(i-width)] == s[int(i+width)]:
                    width += 1
                else:
                    break

            width -= 1

            if (2*width+1) > len(max_palin):
                max_palin = s[int(i-width) : int(i+width+1)]

        return max_palin