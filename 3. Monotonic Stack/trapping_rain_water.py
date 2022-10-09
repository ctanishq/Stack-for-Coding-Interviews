class Solution:
    def trap(self, a: List[int]) -> int:
        stack = []
        
        n = len(a)
        total = 0
        for r in range(n):
            while stack and a[r] >= a[stack[-1]]:
                m = stack.pop()
                
                if not stack: break
                # l = stack[-1]
                width = r - stack[-1] - 1
                height = min(a[r], a[stack[-1]])
                
                left_height = height - a[m]
                
                total += width * left_height
            
            stack.append(r)
        
        return total
