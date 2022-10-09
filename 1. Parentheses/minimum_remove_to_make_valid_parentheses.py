class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        is_ok = [0]*len(s)
        stack = []
        
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    is_ok[stack.pop()] = 1
                    is_ok[i] = 1
                else:
                    continue
            else:
                continue
                
        # is_ok
        
        ans = ""
        for i, c in enumerate(s):
            if c in "()":
                if is_ok[i]:
                    ans += c
                else:
                    pass
            else:
                ans += c
        
        return ans
