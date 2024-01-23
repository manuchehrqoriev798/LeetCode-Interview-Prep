note: Order Traversal
class Solution:
    def orderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return

            # res.append(node.val)  # Preorder Traversal: Append the current node's value before visiting its children.
            dfs(node.left)
            # res.append(node.val)  # In-order Traversal: Append the current node's value during its visit.
            dfs(node.right)
            # res.append(node.val)  # Postorder Traversal: Append the current node's value after visiting its children.

        res = []
        dfs(root)
        return res

# class Solution:
#     def orderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []

#         res = []
#         queue = deque([root])

#         while queue:
#             node = queue.popleft()

#             # Preorder Traversal: Append the current node's value before enqueueing its children.
#             res.append(node.val)

#             if node.left:
#                 queue.append(node.left)

#             # In-order Traversal: Append the current node's value after enqueueing its left child.
#             res.append(node.val)

#             if node.right:
#                 queue.append(node.right)

#             # Postorder Traversal: Append the current node's value after enqueueing its right child.
#             res.append(node.val)

#         return res
