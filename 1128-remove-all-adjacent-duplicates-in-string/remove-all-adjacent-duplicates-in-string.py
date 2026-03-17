class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = ""
        stack = []
        for i in s:
            if len(res) > 0 and i == res[-1]:
                res = res[:-1]
            else:
                res += i
        return res