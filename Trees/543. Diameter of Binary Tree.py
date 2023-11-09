# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # hight = 1 + max(left, right); becasue the hight of the Nul tree is -1 and 
        # in order to cancel it we have to put +1 to make it 0.
    
        # diameter = left + right + 2; +2 because for diameter Null there is edge which can count as 1.
        res = [0]

        def dfs(root):
            if not root:
                return -1 # for empty tree the hight is -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], left + right + 2)
            return 1 + max(left, right)
        
        dfs(root)
        return res[0]