class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        stack = []
        # mono inc --> <= <
        
        n = len(A)
        ans = [-1] * n
        
        for i in reversed(range(n)):
            while stack and A[i] < A[stack[-1]]:
                ans[stack.pop()] = A[i]
            stack.append(i)
            
        return ans
