class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def equals(a, b):
            if a == b:
                return True
            if b == '.' and a is not None:
                return True
            return False
        def backtrack(s, p, i, j):  #string is propagated through s, comparison string remains the same, i represents index on s and j is index on p
            if (i, j) in dp:
                return dp[(i, j)]
            if i == len(s) and j == len(p): 
                dp[(i, j)] = True
                return True
            if i == len(s):
                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[(i, j)] = backtrack(s, p, i, j + 2)
                    return dp[(i, j)]
            if i == len(s) or j == len(p):
                dp[(i, j)] = False
                return False
            if j + 1 != len(p):
                if p[j + 1] == '*':
                    dp[(i, j)] = backtrack(s, p, i, j + 2) or (backtrack(s, p, i + 1, j) and equals(s[i], p[j]))
                    return dp[(i, j)]
            if not equals(s[i], p[j]):
                dp[(i, j)] = False
                return False 
            dp[(i, j)] = backtrack(s, p, i + 1, j + 1)
            return dp[(i, j)]
        return backtrack(s, p, 0, 0)