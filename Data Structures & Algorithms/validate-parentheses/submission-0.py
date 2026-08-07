class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for c in s:
            if c in pairs: #if closing
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else: # if open
                stack.append(c)

        if stack: # if the stack isn't empty
            return False
        else:
            return True