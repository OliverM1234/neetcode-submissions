class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        out = []

        def genParens(cur, opens, closes):
            
            if closes == 0 and opens == 0:
                out.append(cur)
                return
            elif closes <= 0:
                cur += "("
                genParens(cur, opens-1, closes+1)
                cur = cur[:-1]
            elif opens <= 0:
                cur += ")"
                genParens(cur, opens, closes-1)
                cur = cur[:-1]
            else:
                cur += "("
                genParens(cur, opens-1, closes+1)
                cur = cur[:-1]
                
                cur += ")"
                genParens(cur, opens, closes-1)
                cur = cur[:-1]

        genParens("", n, 0)
        return out
            
        