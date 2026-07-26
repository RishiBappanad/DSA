class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        beginning = {} # beginning -> end
        end = {} # end -> beginning
        best = 0
        visited = set()
        for i in nums:
            if i in visited:
                continue
            visited.add(i)
            res = 0
            if i + 1 not in beginning and i - 1 not in end:
                beginning[i] = i
                end[i] = i
                res = 1
            elif i + 1 in beginning and i - 1 in end:
                first = end[i - 1]
                last = beginning[i + 1]
                beginning[first] = last
                end[last] = first
                del beginning[i + 1]
                del end[i - 1]
                res = last - first + 1
            elif i + 1 in beginning:
                beginning[i] = beginning[i + 1]
                end[beginning[i]] = i
                del beginning[i + 1]
                res = beginning[i] - i + 1
            else:
                end[i] = end[i - 1]
                beginning[end[i]] = i
                del end[i - 1]
                res = i - end[i] + 1
            best = max(best, res)

        return best



