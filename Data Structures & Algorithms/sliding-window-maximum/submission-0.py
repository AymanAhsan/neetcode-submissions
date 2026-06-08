class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l, r = 0, k
        while r <= len(nums):
            sub_list = nums[l:r]
            res.append(max(sub_list))
            r += 1
            l += 1
        return res