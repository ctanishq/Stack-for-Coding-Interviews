class Solution:
    def sumSubarrayMins(self, a: List[int]) -> int:
        a.append(-inf)
        MOD = 1000000007   
        stack = [] # mono inc
        n = len(a)
        ans = 0
        
        for r in range(n):
            while stack and a[r] <= a[stack[-1]]:
                i = stack.pop()
                
                l = stack[-1] if stack else -1
                
                left_span = i - l
                right_span = r - i
                
                count = (left_span * right_span) % MOD
                ans += (a[i] * count) % MOD
                ans %= MOD
                
            stack.append(r)
        
        return ans % MOD
