class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for item in path.split("/"):
            if item:
                if item == "..":
                    if stack:
                        stack.pop()
                elif item != ".":
                    stack.append(item)

        return "/" + "/".join(stack)