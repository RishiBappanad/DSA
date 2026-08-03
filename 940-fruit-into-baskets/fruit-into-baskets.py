class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dp = [0] * len(fruits) #dp[i] = most fruit u can hold if you end selecting fruit there
        best = 0 #update on every dp or max at the end
        first, second = 0, 0 #first = 2nd recent, second = recent
        first_type, second_type = None, None
        curr = 0
        last = 0
        for i in fruits:
            if i == second or i == first:
                curr += 1
            else:
                curr = last + 1
            if i == second:
                last += 1
            else:
                last = 1
                first, second = second, i
            
            best = max(best, curr)

        return best
