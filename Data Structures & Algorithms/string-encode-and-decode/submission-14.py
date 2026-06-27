class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""

        for s in strs:
            out += str(len(s))+"#"+s

        return out

    def decode(self, s: str) -> List[str]:
        out = []

        print(s)

        i=0
        
        while i< len(s):
            print(i)
            num = ""
            while s[i] != "#":
                num += s[i]
                i+=1
            i+=1

            n = int(num)

            out.append(s[i:(i+n)])

            i = i+n

        return out
