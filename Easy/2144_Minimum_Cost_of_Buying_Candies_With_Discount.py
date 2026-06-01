import heapq
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        costs = []
        for i in cost:
            heapq.heappush(costs, -i)
        total_cost = 0
        while costs:
            i = 0
            while i < 2 and costs:
                total_cost += -heapq.heappop(costs)
                i += 1
            if costs:
                heapq.heappop(costs)
        return total_cost
