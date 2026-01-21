from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
            else:
                ans.append(n - ((n + 1) & (-n - 1)) // 2)
        return ans

# 測試區
if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 5, 7]
    print(f"Input:  nums = {nums}")
    print(f"Output: {sol.minBitwiseArray(nums)}")