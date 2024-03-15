# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def dfs(node, lower_limit, upper_limit):
            if not node:
                return True

            if not (lower_limit < node.val < upper_limit):
                return False

            left_valid = dfs(node.left, lower_limit, node.val)

            right_valid = dfs(node.right, node.val, upper_limit)

            return left_valid and right_valid

        return dfs(root, float('-inf'), float('inf'))