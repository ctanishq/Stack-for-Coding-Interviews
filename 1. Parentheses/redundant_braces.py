class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        ops = "+-*/"
        for c in A:
            if c == "(":
                stack.append(c)
            if c in ops:
                if stack and stack[-1] == "(":
                    stack.append(c)
            if c == ")":
                if stack[-1] not in ops:
                    return 1
                stack.pop()
                stack.pop()
        
        return 0
