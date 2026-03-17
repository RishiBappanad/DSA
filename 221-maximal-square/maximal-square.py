import operator
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        big = 0
        dp = []
        for i in range(len(matrix) + 1):
            dp.append([0] * (len(matrix[0]) + 1))
        print(dp)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j+1]) + 1
                    big = max(dp[i + 1][j + 1], big)
        return big**2