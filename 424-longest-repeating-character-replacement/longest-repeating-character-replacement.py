class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        freq = {}
        l = 0
        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 0
            freq[s[r]] += 1
            while k + max(freq.values()) < r - l + 1:
                freq[s[l]] -= 1
                l += 1
            best = max(r - l + 1, best)
        return best

