# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])

        res = []
        while q:
            total = 0
            count = 0
            for i in range(len(q)):
                node = q.popleft()
                total += node.val
                count += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(total / count)
        
        return res

                