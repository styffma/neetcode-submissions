class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        arithmetic = ["+", "-", "*", "/"]
        for s in tokens:
            if s not in arithmetic:
                stack.append(s)
            else:
                a = int(stack.pop())
                b = int(stack.pop())

                if s == "+":
                    stack.append(b+a)
                elif s == "-":
                    stack.append(b-a)
                elif s == "*":
                    stack.append(b*a)
                elif s == "/":
                    stack.append(int(b/a))
        
        return int(stack[0]) if stack else 0


