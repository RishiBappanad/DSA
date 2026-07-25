class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        hashmap = [0] * 128
        count = len(t)
        start, end = 0, 0
        best = float('inf')
        curr = 0
        for i in t:
            hashmap[ord(i)] += 1

        while end < len(s):
            if hashmap[ord(s[end])] > 0:
                count -= 1 #decrement necessary characters
            hashmap[ord(s[end])] -= 1 #decrement necessary count per cahr
            end += 1
            while count == 0:
                if end - start < best: #if we find a best length, 
                    curr = start
                    best = end - start
                if hashmap[ord(s[start])] == 0: # if we need said character, add necessary character count
                    count += 1 
                hashmap[ord(s[start])] += 1
                start += 1
        
        if best == float('inf'):
            return ""
        else:
            return s[curr: curr + best]