class Solution(object):
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        memo = {}
        
        def dfs(start_idx):
            if start_idx == len(s):
                return True
            if start_idx in memo:
                return memo[start_idx]
            
            # Try every possible end position for the current word
            for end_idx in range(start_idx + 1, len(s) + 1):
                word = s[start_idx:end_idx]
                if word in word_set:
                    if dfs(end_idx):
                        memo[start_idx] = True
                        return True
                        
            memo[start_idx] = False
            return False
            
        return dfs(0)