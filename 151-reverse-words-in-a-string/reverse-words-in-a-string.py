class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def word(s, pos):
            while pos < len(s) and s[pos] == ' ':
                pos += 1
            res = ''
            while pos < len(s) and s[pos] != ' ' :
                res += s[pos]
                pos += 1
            return res, pos
        i = 0
        res = []
        while i < len(s):
            term, ind = word(s, i)
            i = ind
            res.append(term)
        final = ''
        for i in range(len(res) - 1, -1, -1):
            if res[i] == '':
                continue
            final += (res[i] + ' ')
        return final[:-1:]
            