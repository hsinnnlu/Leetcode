from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i in s:
                return i
            s.add(i)


if __name__ == "__main__":
    s = Solution()

    tests = [
        [1, 2, 3, 3],
        [2, 1, 2, 5, 3, 2],
        [5, 1, 5, 2, 5, 3, 5, 4]
    ]

    for t in tests:
        print(t, "->", s.repeatedNTimes(t))
