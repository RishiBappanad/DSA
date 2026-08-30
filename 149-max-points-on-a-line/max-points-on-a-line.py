class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lines = {} #line (m, b) -> points
        xs = {} #everytime we create a line between two points, search through xs and see if there's any other matches. O(N) for N^2 matches 

        def match(m, b, x):
            return m * x  + b
        
        def connect(a, b):
            x1, y1 = a[0], a[1]
            x2, y2 = b[0], b[1]
            if x2 == x1:
                return (math.inf, x1)
            m = (y2 - y1) / (x2 - x1)
            b = y2 - m * x2
            return (m, b)
        best = 1
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                m, b = connect(tuple(points[i]), tuple(points[j]))
                if (m, b) not in lines:
                    lines[(m, b)] = set() 
                lines[(m, b)].add(tuple(points[i]))
                lines[(m, b)].add(tuple(points[j]))
                best = max(len(lines[(m, b)]), best)
        
        return best

