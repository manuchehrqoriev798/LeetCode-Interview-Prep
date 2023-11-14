# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS
        # def is_valid_bst_helper(node, lower_limit, upper_limit):
        #     if not node:
        #         return True

        #     if not (lower_limit < node.val < upper_limit):
        #         return False

        #     # Check the left subtree with updated upper limit
        #     left_valid = is_valid_bst_helper(node.left, lower_limit, node.val)

        #     # Check the right subtree with updated lower limit
        #     right_valid = is_valid_bst_helper(node.right, node.val, upper_limit)

        #     # Return True only if both subtrees are valid
        #     return left_valid and right_valid

        # return is_valid_bst_helper(root, float('-inf'), float('inf'))
    



        # BFS
        if not root:
            return True

        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            node, lower_limit, upper_limit = queue.popleft()

            if not (lower_limit < node.val < upper_limit):
                return False

            if node.left:
                queue.append((node.left, lower_limit, node.val))

            if node.right:
                queue.append((node.right, node.val, upper_limit))

        return True