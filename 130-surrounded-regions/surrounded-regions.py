class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board:
            return

        n = len(board)
        m = len(board[0])
        seen = set()

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return

            if (i, j) in seen or board[i][j] != "O":
                return

            seen.add((i, j))

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Visit O cells on the borders
        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)

        for j in range(m):
            dfs(0, j)
            dfs(n - 1, j)

        # Capture surrounded regions
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i, j) not in seen:
                    board[i][j] = "X"