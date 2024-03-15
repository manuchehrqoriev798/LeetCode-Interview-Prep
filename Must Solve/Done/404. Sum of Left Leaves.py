# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([root])
        count = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left and not node.left.left and not node.left.right:
                    count += node.left.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return count