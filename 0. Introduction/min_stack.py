class MinStack:
    def __init__(self):
        self.stack = [] # blue
        self.min_stack = [] # green
    
    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        
        if self.min_stack:
            self.min_stack.append(
                min(x, self.min_stack[-1])
            )
        else:
            self.min_stack.append(x)

    # @return nothing
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        else:
            pass

    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1
            
    # @return an integer
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return -1
