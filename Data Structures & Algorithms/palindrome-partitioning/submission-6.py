class Solution:
    def partition(self, s: str) -> List[List[str]]:

        out = []

        def genParts(cur, sLeft):
            if sLeft == "":
                out.append(cur.copy())
                return

            for i in range(len(sLeft)):
                cur_substr = sLeft[:(i+1)]
                print(cur_substr)
                if cur_substr == cur_substr[::-1]:
                    cur.append(cur_substr)
                    genParts(cur, sLeft[(i+1):])
                    cur.pop()

        genParts([], s)

        return out