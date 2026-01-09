from typing import Optional


# Binary Tree Node 定義
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return (None, 0)

            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)

            if left_depth > right_depth:
                return (left_node, left_depth + 1)
            elif right_depth > left_depth:
                return (right_node, right_depth + 1)
            else:
                return (node, left_depth + 1)

        return dfs(root)[0]


if __name__ == "__main__":
    
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.right.right = TreeNode(8)

    sol = Solution()
    ans = sol.subtreeWithAllDeepest(root)

    # 印出答案節點的值
    if ans:
        print("Root of smallest subtree containing all deepest nodes:", ans.val)
    else:
        print("Tree is empty")
