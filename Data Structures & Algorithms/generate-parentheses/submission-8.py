class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        out = []

        def genParens(cur, opens, closes):
            
            if closes == 0 and opens == 0:
                out.append(cur)
                return
            elif closes <= 0:
                genParens(cur+"(", opens-1, closes+1)
            elif opens <= 0:
                genParens(cur+")", opens, closes-1)
            else:
                genParens(cur+"(", opens-1, closes+1)
                genParens(cur+")", opens, closes-1)

        genParens("", n, 0)
        return out
            
        