# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if  len(inorder) == 0 or len(postorder) == 0:
            return None
        rootlength = inorder.index(postorder[-1])
        root = TreeNode(postorder[-1])
        root.left = self.buildTree(inorder[:rootlength],postorder[:rootlength])
        root.right = self.buildTree(inorder[rootlength+1:],postorder[rootlength:-1])
        return root
if __name__ == "__main__":
    solution = Solution()
    list1 = [9,3,15,20,7]
    list2 = [9,15,7,20,3]
    print(solution.buildTree(list1,list2))
