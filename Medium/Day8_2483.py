class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        county = [0] * (n + 1)
        countn = [0] * (n + 1)

        # prefix sums
        for i in range(n):
            county[i + 1] = county[i]
            countn[i + 1] = countn[i]
            if customers[i] == 'Y':
                county[i + 1] += 1
            else:
                countn[i + 1] += 1

        ans = 0
        min_penalty = float('inf')

        for i in range(n + 1):
            penalty = countn[i] + (county[n] - county[i])
            if penalty < min_penalty:
                min_penalty = penalty
                ans = i

        return ans


if __name__ == "__main__":
    sol = Solution()

    # 測試案例
    test_cases = [
        "YYNY",     # 預期 2
        "NNNN",     # 預期 0
        "YYYY",     # 預期 4
        "YNYN",     # 預期 1
        "",         # 預期 0
    ]

    for customers in test_cases:
        result = sol.bestClosingTime(customers)
        print(f"customers = '{customers}', best closing time = {result}")
