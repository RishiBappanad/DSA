class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        neg = False
        print(string)
        if string[0] == '-':
            neg = True
            string = string[1::]
        string = string[::-1]
        if len(f"{int(string):b}") < 32:
            if neg:
                return -1 * int(string)
            return int(string)
        return 0