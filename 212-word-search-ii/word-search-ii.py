class Node:
    def __init__(self, val):
        self.children = {}
        self.val = val
        self.end = False
    def __str__(self):
        return self.val
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        def construct():
            start = {}
            for i in words:
                if i[0] not in start:
                    start[i[0]] = Node(i[0])
                curr = start[i[0]]
                if len(i) == 1:
                    curr.end = True
                for j in range(1, len(i)):
                    char = i[j]
                    if char not in curr.children:
                        curr.children[char] = Node(char)
                    curr = curr.children[char]
                    if j == len(i) - 1:
                        curr.end = True
            return start
        def search(coords):
            i, j = coords[0], coords[1]
            space = []
            if i - 1 >= 0:
                space.append((i - 1, j))
            if j - 1 >= 0:
                space.append((i, j - 1))
            if i + 1 < len(board):
                space.append((i + 1, j))
            if j + 1 < len(board[i]):
                space.append((i, j + 1))
            return space
        def get(coords):
            i, j = coords[0], coords[1]
            return board[i][j]

        def dfs(string, curr, coords, visited):   #curr = node, coords = location, visited = set()
            if coords not in visited:
                visited.add(coords)
            space = search(coords)
            if curr.end:
                res.append(string)
            for i in space:
                if i in visited:
                    continue
                char = get(i)
                if char in curr.children:
                    dfs(string + char, curr.children[char], i, visited)
            visited.remove(coords)
                
        
        
        start = construct()
        for i, k in enumerate(board):
            for j, l in enumerate(k):
                if l in start:
                    coords = (i, j)
                    visited = set()
                    visited.add(coords)
                    dfs(l, start[l], (i, j), visited)
        return list(set(res))
        

#        o a a n
#        e t a e
#        i h k r
#        i f l v