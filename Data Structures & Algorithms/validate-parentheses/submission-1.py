class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        reversed_brackets = {"(":"", "{":"", "[":"", ")":"(", "}":"{", "]":"["}

        for c in s:
            if stack:
                if reversed_brackets[c] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        
        return not stack
            