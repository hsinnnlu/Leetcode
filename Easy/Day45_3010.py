from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] + nums[1] + nums[2]
        
        num1 = 50
        num2 = 50

        for i in range(1, len(nums)):
            if nums[i] < num1:
                num2 = num1
                num1 = nums[i]
            elif num1 <= nums[i] < num2:
                num2 = nums[i]
        
        return nums[0] + num1 + num2


if __name__ == "__main__":
    sol = Solution()

    nums1 = [1,2,3,12]
    print(sol.minimumCost(nums1))  # 6

    nums2 = [5,4,3]
    print(sol.minimumCost(nums2))  # 12

    nums3 = [10,3,1,1]
    print(sol.minimumCost(nums3))  # 12
