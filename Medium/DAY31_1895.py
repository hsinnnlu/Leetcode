# main.py
from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        def Ismagicsquare(i, j, side):
            # first row sum
            total = 0
            for a in range(side):
                total += grid[i][j + a]

            # rows and columns
            for a in range(side):
                row = 0
                col = 0
                for b in range(side):
                    row += grid[i + a][j + b]
                    col += grid[i + b][j + a]
                if row != total or col != total:
                    return False

            # diagonals
            dia1 = 0
            dia2 = 0
            for a in range(side):
                dia1 += grid[i + a][j + a]
                dia2 += grid[i + side - 1 - a][j + a]

            if dia1 != total or dia2 != total:
                return False

            return True

        height = len(grid)
        width = len(grid[0])
        side = min(height, width)

        while side > 1:
            for i in range(height - side + 1):
                for j in range(width - side + 1):
                    if Ismagicsquare(i, j, side):
                        return side
            side -= 1

        return 1


if __name__ == "__main__":
    grid = [
        [7, 1, 4, 5, 6],
        [2, 5, 1, 6, 4],
        [1, 5, 4, 3, 2],
        [1, 2, 7, 3, 4]
    ]

    ans = Solution().largestMagicSquare(grid)
    print(ans)
