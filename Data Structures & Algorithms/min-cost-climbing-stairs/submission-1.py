
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [None] * (len(cost) + 1)
        def search(i):
            if i >= len(cost):
                return 0
            if cache[i] is not None:
                return cache[i]
            cache[i] = cost[i] + min(search(i + 1), search(i + 2))
            return cache[i]
        
        return min(search(0), search(1))
