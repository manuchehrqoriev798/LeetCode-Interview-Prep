class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def lowestCommonAncestor(self, a: 'Node', b: 'Node') -> 'Node':
        pointerA, pointerB = a, b
        
        while pointerA != pointerB:
            if pointerA:
                pointerA = pointerA.parent
            else:
                pointerA = b

            if pointerB:
                pointerB = pointerB.parent
            else:
                pointerB = a

            
        return pointerA
