# main.py
from typing import List

class Solution:
    def maximizeSquareHoleArea(
        self,
        n: int,
        m: int,
        hBars: List[int],
        vBars: List[int]
    ) -> int:

        def longest(a: List[int]) -> int:
            if not a:
                return 1
            a.sort()
            best = cur = 1
            for i in range(1, len(a)):
                if a[i] == a[i - 1] + 1:
                    cur += 1
                else:
                    cur = 1
                best = max(best, cur)
            return best + 1

        side = min(longest(hBars), longest(vBars))
        return side * side


if __name__ == "__main__":
    n = 8
    m = 8
    hBars = [2, 3, 4]
    vBars = [3, 4]

    ans = Solution().maximizeSquareHoleArea(n, m, hBars, vBars)
    print(ans)
