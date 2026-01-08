class Solution:
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        INF = float('-inf')
        dp = [[INF] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                prod = nums1[i] * nums2[j]

                # 選 nums1[i] 和 nums2[j]
                take = prod
                if i > 0 and j > 0:
                    take = prod + max(dp[i-1][j-1], 0)

                # 不選其中一個
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])

                dp[i][j] = max(dp[i][j], take)

        return dp[n-1][m-1]


if __name__ == "__main__":
    # 🔒 測資直接寫死在這裡
    nums1 = [2, 1, -2, 5]
    nums2 = [3, 0, -6]

    sol = Solution()
    ans = sol.maxDotProduct(nums1, nums2)
    print(ans)
