class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None:
            return 0

        self.res = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            len_island = 1
            while q:
                row, col = q.popleft()
                directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows)
                        and c in range(cols)
                        and (r, c) not in visit
                        and grid[r][c] == 1):
                            q.append((r, c))
                            visit.add((r, c))
                            len_island += 1
            self.res = max(self.res, len_island)
        for r in range(rows):
            for c in range(cols):
              while grid[r][c] == 1 and (r, c) not in visit:
                bfs(r, c)
        return self.res