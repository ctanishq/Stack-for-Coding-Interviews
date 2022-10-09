class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for directory in path.split("/"):
            if directory == "":
                pass
            elif directory == ".":
                pass
            elif directory == "..":
                if stack:
                    stack.pop()
                else:
                    pass
            else:
                stack.append(directory)
        
        return "/" + "/".join(stack)
