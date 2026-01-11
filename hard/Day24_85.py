from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])
        height = [0] * m
        max_area = 0

        for i in range(n):
            # 更新 histogram 高度
            for j in range(m):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0

            # 計算當前 histogram 的最大矩形
            stack = []
            for k in range(m + 1):
                cur_height = height[k] if k < m else 0

                while stack and cur_height < height[stack[-1]]:
                    h = height[stack.pop()]
                    left = stack[-1] if stack else -1
                    width = k - left - 1
                    max_area = max(max_area, h * width)

                stack.append(k)

        return max_area


if __name__ == "__main__":
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]

    sol = Solution()
    print("Maximal Rectangle Area =", sol.maximalRectangle(matrix))
