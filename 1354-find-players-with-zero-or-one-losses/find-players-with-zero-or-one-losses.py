class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        set1, set2, more = set(), set(), set()
        for i in matches:
            if i[0] not in set1 and i[0] not in set2 and i[0] not in more:
                set1.add(i[0])
            if i[1] in set1:
                set1.remove(i[1])
                set2.add(i[1])
            elif i[1] in set2:
                set2.remove(i[1])
                more.add(i[1])
            elif i[1] in more:
                continue
            else:
                set2.add(i[1])
        res = []
        res.append(sorted(list(set1)))
        res.append(sorted(list(set2)))
        return res