from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity = sorted(capacity, reverse=True)
        total = 0

        for i in range(len(apple)):
            total += apple[i]

        ans = 0
        for i in range(len(capacity)):
            if total <= 0:
                break
            total -= capacity[i]
            ans += 1

        return ans


if __name__ == "__main__":
    s = Solution()
    apple = [1, 8, 3, 3, 5]
    capacity = [3, 9, 5, 1, 9]
    print(s.minimumBoxes(apple, capacity))
