
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = [None] * len(nums)

        def jumps(i):
            if i >= len(nums) - 1:
                return True
            elif nums[i] == 0:
                return False
            if cache[i] is not None:
                return cache[i]
            for j in range(1, nums[i] + 1):
                cache[i] = jumps(i + j)
                if cache[i]:
                    return True
            return False
        return jumps(0)
            