class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_perim():
            res = set()
            for i in range(len(board[0])):
                if board[0][i] == "O":
                    res.add((0, i))
            for i in range(len(board[-1])):
                if board[-1][i] == "O":
                    res.add((len(board) - 1, i))
            for i in range(len(board)):
                if board[i][0] == "O":
                    res.add((i, 0))
                if board[i][-1] == "O":
                    res.add((i, len(board[i]) - 1))
            return res
        outer_os = get_perim()
        def neighbor(coords):
            i, j = coords[0], coords[1]
            res = []
            if i > 0:
                res.append((i - 1, j))
            if j > 0:
                res.append((i, j - 1))
            if i < len(board) - 1:
                res.append((i + 1, j))
            if j < len(board[i]) - 1:
                res.append((i, j + 1))
            return res
        safe = set()
        visited = set()
        def dfs(coords):
            neighbors = neighbor(coords)
            safe.add(coords)
            for i in neighbors:
                if i in visited:
                    continue
                visited.add(i)
                x, y = i[0], i[1]
                if board[x][y] == "O":
                    dfs(i)
        
        for i in outer_os:
            dfs(i)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in safe:
                    board[i][j] = "X"
        


