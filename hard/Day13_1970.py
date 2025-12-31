from collections import deque
from typing import List

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def canCross(day: int) -> bool:
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1

            q = deque()
            vis = [[False] * col for _ in range(row)]

            for j in range(col):
                if grid[0][j] == 0:
                    q.append((0, j))
                    vis[0][j] = True

            while q:
                x, y = q.popleft()
                if x == row - 1:
                    return True
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < row and
                        0 <= ny < col and
                        not vis[nx][ny] and
                        grid[nx][ny] == 0
                    ):
                        vis[nx][ny] = True
                        q.append((nx, ny))
            return False

        lo, hi, ans = 1, len(cells), 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if canCross(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans


if __name__ == "__main__":
    row = 2
    col = 2
    cells = [[1,1],[2,1],[1,2],[2,2]]
    sol = Solution()
    print(sol.latestDayToCross(row, col, cells))
