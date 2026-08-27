class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0,0
        curr_sum = 0
        max_sub = nums[0]
        while r < len(nums):
            if curr_sum < 0:
                l = r
                curr_sum = 0
            curr_sum += nums[r]
            r += 1
            max_sub = max(max_sub, curr_sum)
        return max_sub