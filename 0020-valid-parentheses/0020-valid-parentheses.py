class Solution:
    def isValid(self, s: str) -> bool:
        m = {')': '(', '}': '{', ']': '['}
        stack = []

        for i in s:
            if i in m:
                top_element = stack.pop() if stack else '#'
                if m[i] != top_element:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0