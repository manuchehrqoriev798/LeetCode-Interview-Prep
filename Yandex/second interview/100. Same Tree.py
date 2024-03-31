# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        q1, q2 = deque([p]), deque([q])

        while q1 and q2:

            for i in range(min(len(q1), len(q2))):
                node1, node2 = q1.popleft(), q2.popleft()

                if not node1 and not node2:
                    continue
                
                if not node1 or not node2 or node1.val != node2.val:
                    return False

                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right)
                
        return True







# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)