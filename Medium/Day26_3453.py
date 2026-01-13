from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def calculate_area(line):
            up_area = 0.0
            down_area = 0.0

            for _, y, l in squares:
                area = l * l
                if y >= line:
                    # 整個 square 在上方
                    up_area += area
                elif y + l <= line:
                    # 整個 square 在下方
                    down_area += area
                else:
                    # square 被水平線切開
                    d_area = (line - y) * l
                    down_area += d_area
                    up_area += area - d_area

            return up_area - down_area

        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        for _ in range(60):  # 精度足夠
            line = (low + high) / 2
            if calculate_area(line) > 0:
                low = line
            else:
                high = line

        return low


if __name__ == "__main__":
    squares = [
        [0, 0, 2],   # 左下 (0,0)，邊長 2
        [1, 1, 2]    # 左下 (1,1)，邊長 2（和上面重疊）
    ]

    sol = Solution()
    ans = sol.separateSquares(squares)

    print("Separate line y-coordinate =", ans)
