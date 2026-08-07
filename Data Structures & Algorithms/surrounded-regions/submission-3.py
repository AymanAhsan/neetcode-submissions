class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visit = set()
        if board is None:
            return None
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            q = collections.deque([(r, c)])
            visit.add((r, c))
            while q:
                row, col = q.popleft()
                directions = [[0,1], [1,0], [0,-1], [-1,0]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(rows) and nc in range(cols)
                    and board[nr][nc] == "O" and (nr, nc) not in visit):
                        visit.add((nr, nc))
                        q.append((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r == 0 or r == rows-1 or c == 0 or c == cols-1):
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visit:
                    board[r][c] = "X"