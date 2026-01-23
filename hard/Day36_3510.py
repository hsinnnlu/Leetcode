import heapq

def minimumPairRemoval(nums):
    n = len(nums)
    if n <= 1:
        return 0

    # Doubly linked list (index-based)
    prev = list(range(-1, n - 1))
    next = list(range(1, n + 1))
    next[-1] = -1

    val = nums[:]
    alive = [True] * n

    # Count initial "bad" edges (prev > curr)
    bad = 0
    for i in range(1, n):
        if nums[i - 1] > nums[i]:
            bad += 1

    # Min-heap of (sum, left_index)
    heap = []
    for i in range(n - 1):
        heapq.heappush(heap, (nums[i] + nums[i + 1], i))

    ops = 0

    while bad > 0:
        # Find the smallest valid adjacent pair
        while True:
            s, i = heapq.heappop(heap)
            j = next[i]
            if j != -1 and alive[i] and alive[j] and val[i] + val[j] == s:
                break

        # Neighbors: a - i - j - b
        a = prev[i]
        b = next[j]

        # Remove old bad edges
        if a != -1 and val[a] > val[i]:
            bad -= 1
        if val[i] > val[j]:
            bad -= 1
        if b != -1 and val[j] > val[b]:
            bad -= 1

        # Merge i and j into i
        val[i] += val[j]
        alive[j] = False
        next[i] = b
        if b != -1:
            prev[b] = i

        # Add new bad edges
        if a != -1 and val[a] > val[i]:
            bad += 1
        if b != -1 and val[i] > val[b]:
            bad += 1

        # Push new adjacent sums
        if a != -1:
            heapq.heappush(heap, (val[a] + val[i], a))
        if b != -1:
            heapq.heappush(heap, (val[i] + val[b], i))

        ops += 1

    return ops


def main():
    # 輸入格式：一行整數，用空白分隔
    # 例如：3 1 2
    nums = list(map(int, input().split()))
    print(minimumPairRemoval(nums))


if __name__ == "__main__":
    main()
