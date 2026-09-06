class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        reversed_brackets = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in reversed_brackets.keys():
                try:
                    if stack[-1] == reversed_brackets[c]:
                        stack.pop()
                    else:
                        return False                    
                except IndexError:
                    return False

            else:
                stack.append(c)
        
        return not stack
            