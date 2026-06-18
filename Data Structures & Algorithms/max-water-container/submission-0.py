class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr1, ptr2, = 0, len(heights) - 1
        max_area = 0
        while ptr2 > ptr1:
            area = (ptr2 - ptr1) * min(heights[ptr1], heights[ptr2])
            if area > max_area:
                max_area = area
            if min(heights[ptr1], heights[ptr2]) == heights[ptr1]:
                ptr1 += 1
            elif min(heights[ptr1], heights[ptr2]) == heights[ptr2]:
                ptr2 -= 1
        return max_area
        
        