class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def get(pos):
            i, j = pos[0], pos[1]
            return heights[i][j]
        def dfs(pos, res): #pos = (i, j), res = set of propagates
            i, j = pos[0], pos[1]  
            neighbors = []
            if i > 0:
                neighbors.append((i - 1, j))
            if i < len(heights) - 1:
                neighbors.append((i + 1, j))
            if j > 0:
                neighbors.append((i, j - 1))
            if j < len(heights[0]) - 1:
                neighbors.append((i, j + 1))
            for i in neighbors:
                if i in res:
                    continue
                if get(i) >= get(pos):
                    res.add(i)
                    dfs(i, res)
            return
        atlantic = set()
        pacific = set()
        for i in range(len(heights)):
            pacific.add((i, 0))
            dfs((i, 0), pacific)
            atlantic.add((i, len(heights[0]) - 1))
            dfs((i, len(heights[0]) - 1), atlantic)
        for i in range(len(heights[0])):
            pacific.add((0, i))
            dfs((0, i), pacific)
            atlantic.add((len(heights) - 1, i))
            dfs((len(heights) - 1, i), atlantic)
        
        final = atlantic & pacific
        res = []
        for i in final:
            res.append(list(i))
        return res
            