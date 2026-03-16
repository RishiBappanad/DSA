class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def get(coords):
            i, j = coords[0], coords[1]
            return board[i][j]
        def search(coords):
            i, j = coords[0], coords[1]
            space = []
            if i + 1 < len(board):
                space.append((i + 1, j))
            if i - 1 > -1:
                space.append((i - 1, j))
            if j + 1 < len(board[0]):
                space.append((i, j + 1))
            if j - 1 > -1:
                space.append((i, j - 1))
            return space
        def dfs(curr, visited, coords):
            if word[len(curr) - 1] != curr[-1]:
                return False
            if len(curr) == len(word):
                return True
            space = search(coords)
            for i in space:
                if i in visited:
                    continue
                visited.add(i)
                if dfs(curr + get(i), visited, i):
                    return True
                visited.remove(i)
            return False
        for i in range(len(board)):
            for j in range(len(board[i])):
                visited = set()
                visited.add((i, j))
                if dfs(get((i, j)), visited, (i, j)):
                    return True
        return False
        