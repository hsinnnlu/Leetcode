class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)

        # dp[i][j]: s1 前 i 個字元、s2 前 j 個字元
        # 變成相同字串的最小 ASCII 刪除總和
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # 初始化：其中一個字串為空
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        # DP 填表
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + ord(s1[i - 1]),
                        dp[i][j - 1] + ord(s2[j - 1])
                    )

        return dp[n][m]


if __name__ == "__main__":
    s1 = "sea"
    s2 = "eat"

    sol = Solution()
    ans = sol.minimumDeleteSum(s1, s2)
    print("Minimum ASCII Delete Sum =", ans)

    # s1 = "delete"
    # s2 = "leet"
