class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        f_sum = float('-inf')  # Handles trees where all nodes are negative

        def dfs(node):
            nonlocal f_sum
            if not node:
                return 0

            # 1. Compute max path sum for left and right subtrees; ignore if negative
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))

            # 2. Update global max path sum WITH a split at the current node
            current_path_sum = node.val + left_max + right_max
            f_sum = max(f_sum, current_path_sum)

            # 3. Return max path sum WITHOUT a split to the parent node
            return node.val + max(left_max, right_max)

        dfs(root)
        return f_sum
