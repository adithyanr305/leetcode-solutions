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
        
''' 
2144. Minimum Cost of Buying Candies With Discount

Approach
1. Sort the array in ascending order.
2. Traverse from the most expensive candy to the cheapest.
3. For every group of three candies:
   - Pay for the two most expensive.
   - Get the third one for free.
4. Add only the paid candies to the answer.

Time Complexity
O(n log n)

Space Complexity
O(1) (excluding sorting space)'''
