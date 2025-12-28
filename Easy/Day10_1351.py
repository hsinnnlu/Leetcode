from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    ans += n - j
                    break
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    grid1 = [[4, 3, 2, -1],
             [3, 2, 1, -1],
             [1, 1, -1, -2],
             [-1, -1, -2, -3]]
    print(sol.countNegatives(grid1))  # Expected output: 8

    # Example 2
    grid2 = [[3, 2],
             [1, 0]]
    print(sol.countNegatives(grid2))  # Expected output: 0
