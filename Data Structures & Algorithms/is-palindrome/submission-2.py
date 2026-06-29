class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        rev_s = ""

        for l in s:
            if l.isalnum():
                new_s += l.lower()
                rev_s = l.lower() + rev_s

        print(rev_s, new_s)

        return new_s == rev_s
        