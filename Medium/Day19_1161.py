from queue import Queue
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = Queue()
        q.put(root)

        level = 1
        max_sum = float('-inf')
        ans_level = 1

        while not q.empty():
            size = q.qsize()
            cur_sum = 0

            for _ in range(size):
                node = q.get()
                cur_sum += node.val

                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)

            if cur_sum > max_sum:
                max_sum = cur_sum
                ans_level = level

            level += 1

        return ans_level


# ---------- 建立 Binary Tree（寫死測資） ----------
def build_tree():
    values = ["1", "7", "0", "7", "-8", "null", "null"]

    root = TreeNode(int(values[0]))
    q = Queue()
    q.put(root)

    i = 1
    while not q.empty() and i < len(values):
        node = q.get()

        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            q.put(node.left)
        i += 1

        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            q.put(node.right)
        i += 1

    return root


# ---------- main ----------
if __name__ == "__main__":
    root = build_tree()

    sol = Solution()
    result = sol.maxLevelSum(root)
    print(result)   # 預期輸出：2
