class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        props = {}
        for i in range(len(equations)):
            j = equations[i]
            a = j[0]
            b = j[1]
            if a not in props:
                props[a] = {}
            props[a][b] = values[i]
            if b not in props:
                props[b] = {}
            props[b][a] = 1 / values[i]
        def dfs(a, b, visited):
            if b not in props or a not in props:
                return -1
            if b in props[a]:
                return props[a][b]
            for i in props[a]:
                if i in visited:
                    continue
                visited.add(i)
                prop = dfs(i, b, visited)
                if prop is not None:
                    return prop * props[a][i]
            return None
        res = []

        for i in queries:
            val = dfs(i[0], i[1], set())
            if val is not None:
                res.append(val) 
            else:
                res.append(-1.0)
        return res

                
                    
    #a->b = 2 b->a = 0.5 b->c = 3, c->b = 1/3