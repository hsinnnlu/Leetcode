import heapq

def minCost(n, edges):
    # 建圖：原邊 + 反向邊(成本 2w)
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))       # 原本方向
        g[v].append((u, 2 * w))   # 反向邊（等價於在 v 用 switch）

    INF = 10**18
    dist = [INF] * n
    dist[0] = 0

    pq = [(0, 0)]  # (cost, node)

    while pq:
        cost, u = heapq.heappop(pq)

        if cost > dist[u]:
            continue

        for v, w in g[u]:
            new_cost = cost + w
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))

    return -1 if dist[n-1] == INF else dist[n-1]


def main():
    # ===== 測資寫死 =====
    n = 3
    edges = [[2, 1, 1], [1, 0, 1], [2, 0, 16]]

    print("n =", n)
    print("edges =", edges)

    result = minCost(n, edges)
    print("Minimum cost from 0 to n-1:", result)


if __name__ == "__main__":
    main()
