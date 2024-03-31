# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        
        if not root1:
            return root2
        
        if not root2:
            return root1

        new_root = TreeNode(root1.val + root2.val)

        new_root.left = self.mergeTrees(root1.left, root2.left)
        new_root.right = self.mergeTrees(root1.right, root2.right)

        return new_root






class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None

        if not root1:
            return root2

        if not root2:
            return root1

        new_root = TreeNode(root1.val + root2.val)
        q = deque([(root1, root2, new_root)])

        while q:
            for i in range(len(q)):
                node1, node2, merged_node = q.popleft()

                if node1.left or node2.left:
                    if node1.left and node2.left:
                        left_child = TreeNode(node1.left.val + node2.left.val)
                        merged_node.left = left_child
                        q.append((node1.left, node2.left, left_child))
                    elif node1.left:
                        merged_node.left = node1.left
                    else:
                        merged_node.left = node2.left

                if node1.right or node2.right:
                    if node1.right and node2.right:
                        right_child = TreeNode(node1.right.val + node2.right.val)
                        merged_node.right = right_child
                        q.append((node1.right, node2.right, right_child))
                    elif node1.right:
                        merged_node.right = node1.right
                    else:
                        merged_node.right = node2.right

        return new_root