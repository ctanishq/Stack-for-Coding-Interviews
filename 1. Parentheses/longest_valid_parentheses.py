class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        is_ok = [0] * n
        stack = []
        
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                if stack:
                    is_ok[stack.pop()] = 1
                    is_ok[i] = 1
                else:
                    pass
        
        count = 0
        ans = 0
        
        for i in range(n):
            if is_ok[i]: count += 1
            else: count = 0
            ans = max(ans, count)
        return ans
