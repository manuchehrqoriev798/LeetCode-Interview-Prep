class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        
        q = deque([root])

        res = []

        while q:
            node = q.popleft()

            if node:
                res.append(node.val)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        res.sort()

        if k <= len(res):
            return res[k - 1]
        else:
            return None







class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None
        
        counter = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            counter += 1

            if counter == k:
                return cur.val
            
            cur = cur.right
        
        return None
        
        
        
        
   