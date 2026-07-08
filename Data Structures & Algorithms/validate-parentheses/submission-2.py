class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for l in s:
            if l in ['(', '{', '[']:
                stack.append(l)
                continue

            if len(stack) == 0:
                return False
                
            if l == ")":
                top = stack.pop()
                if top != "(":
                    return False

            elif l == "}":
                top = stack.pop()
                if top != "{":
                    return False

            elif l == "]":
                top = stack.pop()
                if top != "[":
                    return False

            
        if len(stack) != 0:
            return False

        return True