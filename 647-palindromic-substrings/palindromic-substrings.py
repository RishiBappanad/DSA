class Solution:
    def countSubstrings(self, s: str) -> int:
        def iterate(i, j):
            res = 0
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    res +=1
                    i -= 1
                    j += 1
                else:
                    break
            return res
        
        res = 0
        for i in range(len(s)):
            res += iterate(i, i + 1) + iterate(i, i)
        return res
            