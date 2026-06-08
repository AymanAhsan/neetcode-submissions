class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        res = []
        curr = 1
        for i in range(len(nums)):
            curr *= nums[i]
            prefix.append(curr)
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0] * len(nums)
        elif zero_count == 1:
            # Find product of non-zero elements
            product = 1
            for n in nums:
                if n != 0:
                    product *= n
            # Only the zero position gets this product
            return [product if n == 0 else 0 for n in nums]
        else:
            # No zeros - your original logic works
            total = prefix[-1]
            return [total // n for n in nums]

