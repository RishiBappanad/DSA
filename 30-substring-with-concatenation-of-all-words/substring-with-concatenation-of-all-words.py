from collections import defaultdict

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        
        target_counts = defaultdict(int)
        for w in words:
            target_counts[w] += 1
            
        res = []
        for i in range(word_len):
            left = i
            current_counts = defaultdict(int)
            
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right : right + word_len]
                current_counts[word] += 1
                
                if (right - left) // word_len >= num_words:
                    left_word = s[left : left + word_len]
                    current_counts[left_word] -= 1
                    if current_counts[left_word] == 0:
                        del current_counts[left_word]
                    left += word_len
                
                if current_counts == target_counts:
                    res.append(left)
                    
        return res