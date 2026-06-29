class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = 0
        b = len(s)-1

        while b > f:
            fs = s[f].lower()
            bs = s[b].lower()
            if not fs.isalnum():
                f+=1
            elif not bs.isalnum():
                b-=1
            elif f == b:
                return False
            elif fs != bs:
                return False
            else:
                f+=1
                b-=1
        return True


        