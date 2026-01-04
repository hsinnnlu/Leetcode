from math import isqrt
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0

        for n in nums:
            cnt = 0      # 因數個數
            s = 0        # 因數總和

            for d in range(1, isqrt(n) + 1):
                if n % d == 0:
                    cnt += 1
                    s += d

                    if d != n // d:
                        cnt += 1
                        s += n // d

                    if cnt > 4:
                        break

            if cnt == 4:
                ans += s

        return ans


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([21, 4, 7]),
        ([21, 21]),
        ([1, 2, 3, 4, 5]),
    ]

    for nums in tests:
        result = sol.sumFourDivisors(nums)
        print(f"Input: {nums}")
        print(f"Output: {result}")
        