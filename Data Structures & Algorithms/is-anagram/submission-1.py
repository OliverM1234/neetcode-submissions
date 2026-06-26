class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        letters = {}
        
        for l in s:
            if l in letters:
                letters[l] += 1
            else:
                letters[l] = 1

        for l in t:
            if l in letters:
                letters[l] -= 1
            else:
                return False

        for l in letters:
            if letters[l] != 0:
                return False
        return True


        