class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = ""
        stack = []
        for i in s:
            if len(stack) > 0 and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        for i in stack:
            res += i
        return res