from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)
        lastnum = digits[i - 1] + 1

        if lastnum // 10 == 0:
            digits[i - 1] += 1
            return digits

        arr = [0] * (i + 1)
        arr[i] = lastnum % 10
        i -= 1
        flag = 1

        while flag == 1:
            if i < 1:
                num = flag
            else:
                num = digits[i - 1] + flag
            arr[i] = num % 10
            flag = num // 10
            i -= 1

        if i != 0:
            for j in range(i, 0, -1):
                arr[j] = digits[j - 1]

        if arr[0] == 1:
            return arr
        return arr[1:]


if __name__ == "__main__":
    s = Solution()

    tests = [
        [9],
        [1, 2, 3],
        [9, 9, 9],
        [2, 4, 9, 3, 9],
        [0]
    ]

    for t in tests:
        print(t, "->", s.plusOne(t.copy()))
