class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, rem, curr):
            if i > len(nums) - 1:
                i = 0
                return None
            if rem == 0:
                res.append(curr.copy())
                return
            if rem < 0:
                return
            rem -= nums[i]
            curr.append(nums[i])
            dfs(i, rem, curr)

            curr.pop()
            rem += nums[i]
            dfs(i + 1, rem, curr)
            
        dfs(0, target, [])

        return res
