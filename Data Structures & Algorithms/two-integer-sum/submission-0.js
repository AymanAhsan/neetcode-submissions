class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
         const map = new Map(); // Use Map instead of Set

        for (let i = 0; i < nums.length; i++) {
            const difference = target - nums[i];
            if (map.has(difference)) {
                return [map.get(difference), i]; // Return indices of the two numbers
            } else {
                map.set(nums[i], i); // Store the number and its index
            }
        }
    }

}
