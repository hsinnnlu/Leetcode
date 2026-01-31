def nextGreatestLetter(letters, target):
    low = 0
    high = len(letters) - 1
    c = 0
    minc = "z"

    while low <= high:
        mid = (low + high) // 2
        if letters[mid] > target:
            high = mid - 1
            minc = min(letters[mid], minc)
            c += 1
        else:
            low = mid + 1

    if c == 0:
        return letters[0]
    return minc


def main():
    letters = ["c", "f", "j"]
    target = "a"
    print(nextGreatestLetter(letters, target))

    letters = ["c", "f", "j"]
    target = "c"
    print(nextGreatestLetter(letters, target))

    letters = ["x", "x", "y", "y"]
    target = "z"
    print(nextGreatestLetter(letters, target))


if __name__ == "__main__":
    main()
