from collections import defaultdict

def minCost(grid, k):
    m, n = len(grid), len(grid[0])
    d = defaultdict(list)

    for i in range(m):
        for j in range(n):
            d[grid[i][j]].append((i, j))

    inf = float('inf')
    dp = [[inf] * n for _ in range(m)]
    dp[0][0] = 0

    def update():
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                up = dp[i-1][j] if i > 0 else inf
                left = dp[i][j-1] if j > 0 else inf
                temp = grid[i][j] + min(up, left)
                if temp < dp[i][j]:
                    dp[i][j] = temp

    update()

    keys = sorted(d, reverse=True)
    for _ in range(k):
        dist = inf
        for key in keys:
            for i, j in d[key]:
                if dp[i][j] < dist:
                    dist = dp[i][j]
            for i, j in d[key]:
                dp[i][j] = dist
        update()

    return dp[-1][-1]


def main():
    grid = [
        [1, 3, 3],
        [2, 5, 4],
        [4, 3, 5]
    ]
    k = 2

    result = minCost(grid, k)
    print(result)


if __name__ == "__main__":
    main()
