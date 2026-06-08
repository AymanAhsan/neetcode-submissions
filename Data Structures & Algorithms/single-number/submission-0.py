class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        duplicate = set()
        for n in nums:
            if n in duplicate:
                duplicate.remove(n)
            else:
                duplicate.add(n)
        return duplicate.pop()