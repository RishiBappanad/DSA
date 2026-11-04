import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        tot = m + n - 2
        return math.comb(tot, m - 1)