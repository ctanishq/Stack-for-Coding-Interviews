class Solution:
    def calculate(self, s: str) -> int:        
        def read(s):
            infix = []
            
            i = 0
            while i < len(s):
                if s[i] == " ":
                    i += 1
                elif s[i] in operators:
                    if s[i] == "-": # 5 - (-2)
                        if i == 0 or i-1 >= 0 and s[i-1] == "(":
                            infix.append("0")

                    infix.append(s[i])
                    i += 1
                else:
                    # 2, 345
                    number = ""
                    while i < len(s) and s[i].isdigit():
                        number += s[i]
                        i += 1
                    infix.append(number)
            
            return infix
        
        def infix_to_postfix(infix): 
            postfix = []
            stack = []

            for token in infix: 
                if token == "(": 
                    stack.append(token) 
                elif token == ")": 
                    while stack[-1] != "(": 
                        postfix.append(stack.pop())
                    stack.pop() 
                elif token not in operators:
                    postfix.append(token)
                else: 
                    while stack and priority[stack[-1]] >= priority[token]: 
                        postfix += stack.pop() 
                    stack.append(token) 

            while stack: 
                postfix += stack.pop() 

            return postfix 

        def evaluate_postfix(postfix):
            stack = []
            ops = {
                '+' : operator.add,
                '-' : operator.sub,
                '*' : operator.mul,
                '/' : operator.truediv
            }

            for token in postfix:
                if token not in ops:
                    stack.append(int(token))
                else:
                    n2 = stack.pop()
                    n1 = stack.pop()
                    result = ops[token](n1, n2)
                    stack.append(int(result))

            return stack[0]
        
        operators = "()/*+-"
        priority = {
            "(": -1,
            "/": 1,
            "*": 1,
            "+": 0,
            "-": 0,
        }
        
        infix = read(s)
        postfix = infix_to_postfix(infix)
        return evaluate_postfix(postfix)
        
