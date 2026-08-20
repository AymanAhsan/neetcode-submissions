class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = m - 1
        col = n - 1
        cache = [[None] * (col + 1) for _ in range(row + 1)]
        def search(i, j):
            if i == row and j == col:
                return 1
            if i > row or j > col:
                return 0
            if cache[i][j] is not None:
                return cache[i][j]
            
            cache[i][j] = search(i + 1, j) + search(i, j + 1)
            return cache[i][j]
        return search(0, 0)
        
        