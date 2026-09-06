class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        
        for num in nums:
            if num - 1 not in seen:
                curr = 1
                i = num
                while i + 1 in seen:
                    curr += 1
                    i += 1
                res = max(res, curr)
        return res





