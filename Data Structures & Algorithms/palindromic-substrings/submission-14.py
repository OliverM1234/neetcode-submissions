class Solution:
    def countSubstrings(self, s: str) -> int:

        total = 0

        for i in range(len(s)):

            width = 0

            while ((i-width)>=0 and (i+width)<len(s)):

                if s[i-width] == s[i+width]:
                    width += 1
                else:
                    break
            print(width)
            total += width


        
        for j in range(len(s)-1):

            i = j + 0.5

            width = 0.5

            while ((i-width)>=0 and (i+width)<len(s)):

                if s[int(i-width)] == s[int(i+width)]:
                    width += 1
                else:
                    break
            print(width)
            total += (width-0.5)

        return int(total)