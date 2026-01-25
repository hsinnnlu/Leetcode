def minimumDifference(nums, k):
    nums = sorted(nums)
    ans = float('inf')

    for i in range(len(nums) - k + 1):
        diff = nums[i + k - 1] - nums[i]  # 已排序，不需要 abs
        ans = min(ans, diff)

    return ans


def main():
    # 測資寫死在這裡
    nums = [90, 70, 85, 60, 100]
    k = 3

    print("nums =", nums)
    print("k =", k)
    print("Minimum difference:", minimumDifference(nums, k))


if __name__ == "__main__":
    main()
