class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root














class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # DFS
        
        if not preorder or not inorder:
            return None

        return self.buildTreeDFS(preorder, inorder)

    def buildTreeDFS(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root_val = preorder.pop(0)
        root = TreeNode(root_val)

        # Find the index of the root value in the inorder list
        root_index = inorder.index(root_val)

        # Recursively build the left and right subtrees
        root.left = self.buildTreeDFS(preorder, inorder[:root_index])
        root.right = self.buildTreeDFS(preorder, inorder[root_index + 1:])

        return root





class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # BFS
        
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        queue = deque([(root, preorder[1:], inorder)])

        while queue:
            current, pre, ino = queue.popleft()

            root_index = ino.index(current.val)

            left_inorder = ino[:root_index]
            right_inorder = ino[root_index + 1:]

            left_preorder = pre[:len(left_inorder)]
            right_preorder = pre[len(left_inorder):]

            if left_preorder:
                current.left = TreeNode(left_preorder[0])
                queue.append((current.left, left_preorder[1:], left_inorder))

            if right_preorder:
                current.right = TreeNode(right_preorder[0])
                queue.append((current.right, right_preorder[1:], right_inorder))

        return root
