# main.py
from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        l = len(bottomLeft)
        maxside = 0
        
        for i in range(l - 1):
            for j in range(i + 1, l):
                x1, y1 = bottomLeft[i]
                x2, y2 = topRight[i]

                x3, y3 = bottomLeft[j]
                x4, y4 = topRight[j]
                
                overlap_w = max(0, min(x2, x4) - max(x1, x3))
                overlap_h = max(0, min(y2, y4) - max(y1, y3))

                maxside = max(maxside, min(overlap_w, overlap_h))
        
        return maxside * maxside


if __name__ == "__main__":
    bottomLeft = [
        [1, 1],
        [2, 2],
        [3, 1]
    ]
    topRight = [
        [4, 4],
        [5, 5],
        [6, 3]
    ]

    ans = Solution().largestSquareArea(bottomLeft, topRight)
    print(ans)
