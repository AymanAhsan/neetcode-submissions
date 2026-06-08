class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j_ptr = i + 1  # start after i
            k_ptr = len(nums) - 1

            while j_ptr < k_ptr:
                sums = nums[i] + nums[j_ptr] + nums[k_ptr]
                if sums == 0:
                    ans.append([nums[i], nums[j_ptr], nums[k_ptr]])
                    # skip duplicates
                    while j_ptr < k_ptr and nums[j_ptr] == nums[j_ptr + 1]:
                        j_ptr += 1
                    while j_ptr < k_ptr and nums[k_ptr] == nums[k_ptr - 1]:
                        k_ptr -= 1
                    j_ptr += 1
                    k_ptr -= 1
                elif sums < 0:
                    j_ptr += 1
                else:
                    k_ptr -= 1
            
        return ans
