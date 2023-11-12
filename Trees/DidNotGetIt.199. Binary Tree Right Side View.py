class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        res = []
        if not root:
            return res

        q = deque()
        q.append(root)

        while q:
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if i == qlen - 1:  # This condition ensures we only add the rightmost element in each level
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res




        # BFS
        res = []
        q = deque([root])
        while q:
            rightSide = None
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
                if rightSide:
                    res.append(rightSide)

        return res


        # # DFS
        # def dfs(node, depth):
        #     if not node:
        #         return
        #     if depth == len(res):
        #         res.append(node.val)
        #     # Traverse right first to get the rightmost element at each level
        #     dfs(node.right, depth + 1)
        #     dfs(node.left, depth + 1)

        # res = []
        # dfs(root, 0)
        # return res
