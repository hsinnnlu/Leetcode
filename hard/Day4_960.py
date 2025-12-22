from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])   # number of columns
        m = len(strs)      # number of rows
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                ok = True
                for r in range(m):
                    if strs[r][j] > strs[r][i]:
                        ok = False
                        break
                if ok:
                    dp[i] = max(dp[i], dp[j] + 1)

        mx = 0
        for v in dp:
            if v > mx:
                mx = v

        return n - mx


if __name__ == "__main__":
    # 測試用資料
    strs1 = ["babca", "bbazb"]
    strs2 = ["edcba"]
    strs3 = ["ghi", "def", "abc"]

    sol = Solution()

    print(sol.minDeletionSize(strs1))  # expected 3
    print(sol.minDeletionSize(strs2))  # expected 4
    print(sol.minDeletionSize(strs3))  # expected 0
