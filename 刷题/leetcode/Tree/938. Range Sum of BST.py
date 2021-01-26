class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.sums = 0
        self.helper(root, L, R)
        return self.sums

    def helper(self,root, L, R):
        if not root:
            return
        if root.val > R:
            self.helper(root.left,L,R)
        elif L <= root.val <= R:
            self.sums += root.val
            self.helper(root.left,L,R)
            self.helper(root.right, L, R)
        elif root.val < L:
            self.helper(root.right,L,R)

if __name__=='__main__':
    solution=Solution()
    A1 = TreeNode(10)
    A2 = TreeNode(5)
    A3 = TreeNode(None)
    A1.left=A2
    A1.right=A3
    print(solution.rangeSumBST(A1,5,10))