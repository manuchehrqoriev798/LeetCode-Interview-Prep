# BFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        q = deque([root])

        while q:
            level = []
            levelSize = len(q)
            for i in range(levelSize):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if level:
                res.append(level[-1])
        
        return res



class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        res = []
        if not root:
            return res

        q = deque([root])

        while q:
            levelSize = len(q)
            for i in range(levelSize):
                node = q.popleft()
                if i == qlen - 1:  # This condition ensures we only add the rightmost element in each level
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res





class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []

        q = deque([root])

        while q:
            rightSide = None
            levelSize = len(q)
            for i in range(levelSize):
                node = q.popleft()
                if node:
                    rightSide = node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)    
            if rightSide:
                res.append(rightSide.val)
        
        return res





class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, depth):
            if not node:
                return []
            if depth == len(res):
                res.append(node.val)
            # Traverse right first to get the rightmost element at each level
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        res = []
        dfs(root, 0)
        return res













# DFS 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, depth):
            if not node:
                return []
            if depth != len(res):
                res.append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        res = []
        dfs(root, 0)
        return res




class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, depth):
            if not node:  
                return []
            if depth == len(res):  # If the current depth equals the length of the result list, it means we've reached a new level of the tree that hasn't been added to the result list yet.
                res.append(node.val)  # So, we append the value of the current node to the result list.
            else:
                res[depth] = node.val  # If we've already added a node at this depth, we update it with the current node's value.
            dfs(node.left, depth + 1)  # We first traverse the left subtree.
            dfs(node.right, depth + 1) 

        res = [] 
        dfs(root, 0) 
        return res  


























# LeftSide viev of the tree 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []

        q = deque([root])

        while q:
            levelSize = len(q)
            level = []
            for i in range(levelSize):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(level[0])
        
        return res



class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []

        q = deque([root])

        while q:
            levelSize = len(q)
            leftSide = None
            for i in range(levelSize):
                node = q.popleft()
                leftSide = node
                if node:
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
            if leftSide:
                res.append(leftSide.val)
        
        return res


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        def dfs(node, depth):
            if not node:
                return
            if depth == len(res):
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        res = []
        dfs(root, 0)
        return res