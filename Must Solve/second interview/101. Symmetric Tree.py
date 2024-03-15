class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(left, right):
            if not left and not right:
                return True
            if left and right and left.val == right.val:
                return (dfs(left.left, right.right) and 
                    dfs(left.right, right.left))
            return False

        return dfs(root, root)

        

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        q = deque([root, root]) 

        while q:
            node1 = q.popleft()
            node2 = q.popleft()

            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            q.append(node1.left)
            q.append(node2.right)
            q.append(node1.right)
            q.append(node2.left)

        return True



class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([root])

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append(None)
            
            if level != level [::-1]:
                return False
        
        return True