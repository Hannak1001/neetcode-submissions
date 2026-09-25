class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for c in s:
            if c in pairs: # c is a closing bracket
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else: # open bracket
                stack.append(c)

        if stack:
            return False
        else:
            return True
