from typing import List

class Solution:
    def isMagicSquare(self, grid, row, col):
        s = set()

        # check number (1~9 and distinct)
        for i in range(3):
            for j in range(3):
                num = grid[row + i][col + j]
                if num in s or num < 1 or num > 9:
                    return False
                s.add(num)

        flag = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]

        # check rows and columns
        for i in range(3):
            rowsum = 0
            colsum = 0
            for j in range(3):
                rowsum += grid[row + i][col + j]
                colsum += grid[row + j][col + i]
            if rowsum != flag or colsum != flag:
                return False

        # check diagonals
        dia1 = 0
        dia2 = 0
        for i in range(3):
            dia1 += grid[row + i][col + i]
            dia2 += grid[row + i][col + 2 - i]

        if dia1 != flag or dia2 != flag:
            return False

        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        cnt = 0

        for i in range(row - 2):
            for j in range(col - 2):
                if self.isMagicSquare(grid, i, j):
                    cnt += 1
        return cnt


if __name__ == "__main__":
    sol = Solution()

    grid = [
        [4, 3, 8, 4],
        [9, 5, 1, 9],
        [2, 7, 6, 2],
        [4, 3, 8, 4],
        [9, 5, 1, 9],
        [2, 7, 6, 2]
    ]

    result = sol.numMagicSquaresInside(grid)
    print("Number of magic squares:", result)  # Expected: 2
