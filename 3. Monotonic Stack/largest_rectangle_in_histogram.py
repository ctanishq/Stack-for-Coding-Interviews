class Solution:
    def largestRectangleArea(self, a: List[int]) -> int:
        stack = [] # mono inc
        
        a.append(0)
        
        n = len(a)
        ans = 0
        for r in range(n):
            while stack and a[r] <= a[stack[-1]]:
                i = stack.pop()
                l = stack[-1] if stack else -1
                
                right_span = r - i - 1
                left_span = i - l - 1
                
                width = right_span + left_span + 1
                
                area = width * a[i]
                ans = max(ans, area)
            
            stack.append(r)
        
        return ans
