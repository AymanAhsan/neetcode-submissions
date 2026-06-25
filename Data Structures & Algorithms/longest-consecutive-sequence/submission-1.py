class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 0
        seen = set()
        for num in nums:
            seen.add(num)
        for num in seen:
            if num - 1 not in seen:
                length = 1
                while num + length in seen:
                    length += 1
                if length > max_seq:
                    max_seq = length
        return max_seq
