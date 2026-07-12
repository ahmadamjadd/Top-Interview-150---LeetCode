class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_val):
            if not node:
                return 0
            
            is_good = 1 if node.val >= max_val else 0
            current_max = max(max_val, node.val)
            
            return is_good + dfs(node.left, current_max) + dfs(node.right, current_max)
            
        return dfs(root, root.val)
