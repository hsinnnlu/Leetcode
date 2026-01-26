def minimumAbsDifference(arr):
    ans = []

    arr = sorted(arr)
    minnum = float('inf')

    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        minnum = min(minnum, diff)

    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == minnum:
            ans.append([arr[i], arr[i + 1]])

    return ans


def main():
    arr = [4, 2, 1, 3]

    print("Input array:", arr)
    result = minimumAbsDifference(arr)
    print("Result:", result)


if __name__ == "__main__":
    main()
