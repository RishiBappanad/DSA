import heapq
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        sell, buy = [], []
        heapq.heapify(sell)
        heapq.heapify(buy)
        #implement scaffolding then actual logic post pop
        for i in orders:
            price, amount, action = i[0], i[1], i[2]
            if action:
                while amount and len(buy) and buy[0][0] * -1 >= price:
                    curr = heapq.heappop(buy)
                    if curr[1] > amount:
                        heapq.heappush(buy, (curr[0], curr[1] - amount))
                        amount = 0
                    else:
                        amount -= curr[1]
                heapq.heappush(sell, (price, amount))
            else:
                while amount and len(sell) and sell[0][0] <= price:
                    curr = heapq.heappop(sell)
                    if curr[1] > amount:
                        heapq.heappush(sell, (curr[0], curr[1] - amount))
                        amount = 0
                    else:
                        amount -= curr[1]    
                heapq.heappush(buy, (price * -1, amount))

        count = 0
        for i in buy:
            count = (i[1]  + count)  %   (10**9 + 7)
        for i in sell:
            count = (i[1] + count) % (10**9 + 7)
        return count


                    
