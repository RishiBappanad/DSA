class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        curr = []
        counter = 0
        def justify(line, count):
            ans = ""
            if len(line) == 1:
                return line[0] + " " * (maxWidth - len(line[0]))
            spaces = maxWidth - count
            spaces = spaces // (len(line) - 1)
            extra = maxWidth - (spaces * (len(line) - 1) + count)
            for i in range(len(line) - 1):
                val = line[i]
                if extra:
                    extra -= 1
                    val += " "
                val += " " * spaces
                ans += val
            ans += line[-1]
            return ans 
                 
                
        for i in words:
            counter += len(i)
            if counter + len(curr) > maxWidth:
                counter -= len(i)
                res.append(justify(curr, counter))
                counter = len(i)
                curr = []
            curr.append(i)
        val = ""
        for i in range(len(curr) - 1):
            val += curr[i] + " "
        val += curr[-1]
        val += " " * (maxWidth - len(val))
        res.append(val)
        return res

