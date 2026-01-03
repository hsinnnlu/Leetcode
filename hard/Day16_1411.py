class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        # dp[i][0]: ABC type at row i+1
        # dp[i][1]: ABA type at row i+1
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [6, 6]  # first row

        for i in range(1, n):
            dp[i][0] = (2 * dp[i-1][0] + 2 * dp[i-1][1]) % MOD
            dp[i][1] = (2 * dp[i-1][0] + 3 * dp[i-1][1]) % MOD

        return (dp[n-1][0] + dp[n-1][1]) % MOD


if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    n = 1
    print("Input:", n)
    print("Output:", sol.numOfWays(n))
    print()

    # Test case 2
    n = 5000
    print("Input:", n)
    print("Output:", sol.numOfWays(n))
