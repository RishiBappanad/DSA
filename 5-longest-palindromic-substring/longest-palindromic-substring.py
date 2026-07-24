class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal(l, r):
            left, right = l, r
            while l >= 0 and r < len(s) and s[l] == s[r]:
                left, right = l, r
                l -= 1
                r += 1
            return s[left:right + 1]
        best = ""
        for i in range(len(s)):
            string = pal(i, i)
            if len(string) > len(best):
                best = string
            if i < len(s) - 1 and s[i + 1] == s[i]:
                string2 = pal(i, i + 1)
                if len(string2) > len(best):
                    best = string2
        
        return best

            
            
