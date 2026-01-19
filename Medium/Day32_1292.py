# main.py
from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n = len(mat)
        m = len(mat[0])

        preSum = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                preSum[i + 1][j + 1] = (
                    preSum[i][j + 1]
                    + preSum[i + 1][j]
                    - preSum[i][j]
                    + mat[i][j]
                )

        def exists(side: int) -> bool:
            for i in range(n - side + 1):
                for j in range(m - side + 1):
                    total = (
                        preSum[i + side][j + side]
                        - preSum[i][j + side]
                        - preSum[i + side][j]
                        + preSum[i][j]
                    )
                    if total <= threshold:
                        return True
            return False

        left, right = 1, min(n, m)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if exists(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans


if __name__ == "__main__":
    mat = [
        [1, 1, 3, 2, 4, 3, 2],
        [1, 1, 3, 2, 4, 3, 2],
        [1, 1, 3, 2, 4, 3, 2]
    ]
    threshold = 4

    sol = Solution()
    result = sol.maxSideLength(mat, threshold)
    print(result)  # 預期輸出：2
