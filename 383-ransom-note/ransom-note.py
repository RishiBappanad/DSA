class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for i in magazine:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1
        for i in ransomNote:
            if i not in hashmap or hashmap[i] == 0:
                return False
            hashmap[i] -= 1
        return True