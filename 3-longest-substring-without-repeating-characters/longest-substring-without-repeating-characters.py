class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        chars = set()
        best = 0
        while right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
            else: 
                while s[left] != s[right]:
                    chars.remove(s[left])
                    left += 1
                left += 1
            right += 1
            best = max(best, right - left)

        
        return best

