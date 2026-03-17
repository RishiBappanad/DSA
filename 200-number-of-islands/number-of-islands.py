class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        islands = {}
        self.count = 0
        def bfs(i, j, parent):
            if grid[i][j] == "0":
                return
            if (i, j) in islands:
                return
            islands[(i, j)] = 1
            if not parent:
                self.count += 1
            if i > 0:
                up = int(grid[i-1][j])
                if up:
                    bfs(i-1, j, True)
            if j > 0:
                left = int(grid[i][j-1])
                if left:
                    bfs(i, j-1, True)
            if i < len(grid) - 1:
                down = int(grid[i + 1][j])
                if down:
                    bfs(i+1, j, True)
            if j < len(grid[i]) - 1:
                right = int(grid[i][j+1])
                if right:
                    bfs(i, j+1, True)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in islands and grid[i][j] == "1":
                    bfs(i, j, False)
                print(self.count, i, j)
        return self.count
            