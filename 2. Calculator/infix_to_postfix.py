def infix_to_postfix(infix):
    postfix = []
    stack = []

    for token in infix:
        if token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        elif token not in operators:
            postfix.append(token)
        else:
            while stack and priority[stack[-1]] >= priority[token]:
                postfix.append(stack.pop())
            stack.append(token)

        while stack:
            postfix.append(stack.pop())

        return postfix
