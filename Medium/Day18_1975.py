from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        minnum = 10**5
        sumnum = 0
        negative = 0

        for i in range(n):
            for j in matrix[i]:
                if j < 0:
                    sumnum += -j
                    negative += 1
                else:
                    sumnum += j
                minnum = min(minnum, abs(j))

        if negative % 2 != 0:
            sumnum -= 2 * minnum

        return sumnum


# ===== 測試資料直接寫在這裡 =====
if __name__ == "__main__":
    sol = Solution()

    matrix1 = [
        [1, -1],
        [-1, 1]
    ]
    print("Test 1 Output:", sol.maxMatrixSum(matrix1))  # expected 4

    matrix2 = [
        [1, 2, 3],
        [-1, -2, -3],
        [1, 2, 3]
    ]
    print("Test 2 Output:", sol.maxMatrixSum(matrix2))  # expected 16
