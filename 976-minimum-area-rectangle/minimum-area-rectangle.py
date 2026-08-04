class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        #valid rectangles = 4 points , each must have the same x or y coordinate as another point
        x = {} #all y coordinates for i in x
        y = {} #all x coordinates for j in y
        for i in points:
            a, b = i[0], i[1]
            if a not in x:
                x[a] = set()
            if b not in y:
                y[b] = set()
            x[a].add(b)
            y[b].add(a)
        print(x, y)
        def compute(i, j, k, m):
            return max(k - i, i - k) * max(m - j, j - m)
        best = float('inf')
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                a, b, c, d = points[i][0], points[i][1], points[j][0], points[j][1]
                if a != c and b != d:
                    if a in y[d] and c in y[b]:
                        best = min(compute(a, b, c, d), best)

        return best if best != float('inf') else 0

                