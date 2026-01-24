def minPairSum(nums):
    nums = sorted(nums)
    n = len(nums)
    ans = 0

    for i in range(n // 2):
        pair_sum = nums[i] + nums[n - i - 1]
        ans = max(ans, pair_sum)

    return ans


def main():
    nums = [3, 5, 2, 3]

    result = minPairSum(nums)
    print("Input:", nums)
    print("Minimized maximum pair sum:", result)


if __name__ == "__main__":
    main()
