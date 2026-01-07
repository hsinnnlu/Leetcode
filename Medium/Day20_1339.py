from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        # DFS：把每個節點的 val 改成「子樹總和」
        def dfs(node):
            if not node:
                return 0
            node.val += dfs(node.left) + dfs(node.right)
            return node.val

        total = dfs(root)

        ans = 0
        q = deque([root])

        # BFS：嘗試把每個子樹切掉
        while q:
            node = q.popleft()
            if not node:
                continue

            current_product = (total - node.val) * node.val
            ans = max(ans, current_product)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return ans % MOD


# ---------- 建立 Binary Tree（寫死測資） ----------
def build_tree():
    # 對應 LeetCode 範例：[1,2,3,4,5,6]
    values = [1, 2, 3, 4, 5, 6]

    nodes = [TreeNode(v) for v in values]

    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[5]

    return nodes[0]


# ---------- main ----------
if __name__ == "__main__":
    root = build_tree()

    sol = Solution()
    result = sol.maxProduct(root)
    print(result)   # 預期輸出：110
