# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        q = deque([root])
        total = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()

                if low <= node.val <= high:
                    total += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return total