class Solution:
    def subArrayRanges(self, a: List[int]) -> int:
        def sum_subarray_op(a, op):
            stack = []
            ans = 0
            
            for i in range(len(a)):
                while stack and op(a[i], a[stack[-1]]):
                    mid = stack.pop()
                    
                    right_span = i - mid
                    left_span = mid - (stack[-1] if stack else -1)
                    
                    ans += a[mid] * right_span * left_span 
                    
                stack.append(i)
            
            return ans
        
        return (
            + sum_subarray_op(a+[inf], operator.ge) 
            - sum_subarray_op(a+[-inf], operator.le)
        )
