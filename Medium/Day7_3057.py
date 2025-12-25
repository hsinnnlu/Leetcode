from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = sorted(happiness, reverse=True)

        count = 1

        for i in range(1, len(happiness)):
            if count < k:
                if happiness[i] - count > 0:
                    happiness[i] -= count
                else:
                    happiness[i] = 0
                count += 1
            else:
                happiness[i] -= k
                if happiness[i] < 0:
                    happiness[i] = 0

        return sum(happiness[0:k])


if __name__ == "__main__":
    sol = Solution()

    happiness = [1, 2, 3]
    k = 2
    result = sol.maximumHappinessSum(happiness, k)

    print(result)
