class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [None] * len(nums)
        def search(i):
            if i >= len(nums):
                return 0
            if cache[i] is not None:
                return cache[i]
            cache[i] = max(nums[i] + search(i + 2), search(i + 1))
            return cache[i]
        return search(0)
            
            