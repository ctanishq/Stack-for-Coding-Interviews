class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []     
        n = len(heights)
        
        # mono dec
        for i in range(n):
            while stack and heights[i] >= heights[stack[-1]]: 
                stack.pop()
                
            stack.append(i)
            
        return stack
