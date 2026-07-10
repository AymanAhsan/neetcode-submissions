class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix) - 1

        while start <= end:
            mid  = (start + end) // 2
            start_row, end_row = 0, len(matrix[mid]) - 1
            if target >= matrix[mid][start_row] and target <= matrix[mid][end_row]:
                while start_row <= end_row:
                    mid_row = (start_row + end_row) // 2
                    if target == matrix[mid][mid_row]:
                        return True
                    elif target < matrix[mid][mid_row]:
                        end_row = mid_row - 1
                    elif target > matrix[mid][mid_row]:
                        start_row = mid_row + 1
                return False
            elif target < matrix[mid][start_row]:
                end = mid - 1
            elif target > matrix[mid][end_row]:
                start = mid + 1

        return False